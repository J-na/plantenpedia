"""
Supabase database client en alle queryfuncties voor Plantenpedia.
"""
from __future__ import annotations

import hashlib
import re
from datetime import date
from typing import Any, Dict, List, Optional

import streamlit as st
from supabase import Client, create_client


# ── Client ──────────────────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def get_client() -> Client:
    """Geeft een gecachte Supabase client terug (lees-only: anon key)."""
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)


@st.cache_resource(show_spinner=False)
def get_admin_client() -> Client:
    """Geeft een gecachte Supabase client terug met service_role key (schrijfrechten)."""
    url = st.secrets["supabase"]["url"]
    # Gebruik service_role key als die beschikbaar is, anders val terug op anon key
    key = st.secrets["supabase"].get("service_key", st.secrets["supabase"]["key"])
    return create_client(url, key)


# ── Helpers ──────────────────────────────────────────────────────────────────

def make_slug(scientific_name: str) -> str:
    """Zet een wetenschappelijke naam om naar een URL-vriendelijke slug."""
    slug = scientific_name.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


# ── Planten lezen ────────────────────────────────────────────────────────────

LIST_COLUMNS = (
    "id, scientific_name, dutch_names, slug, category, "
    "edible, toxic, light_needs, bloom_start, bloom_end, soil_types, photos"
)


@st.cache_data(ttl=300, show_spinner=False)
def get_all_plants(columns: str = LIST_COLUMNS) -> List[Dict]:
    """Geeft alle planten terug (gesorteerd op wetenschappelijke naam)."""
    response = (
        get_client()
        .table("plants")
        .select(columns)
        .order("scientific_name")
        .execute()
    )
    return response.data or []


@st.cache_data(ttl=300, show_spinner=False)
def get_plant_by_slug(slug: str) -> Optional[Dict]:
    """Zoek één plant op basis van de slug (volledige gegevens)."""
    response = (
        get_client()
        .table("plants")
        .select("*")
        .eq("slug", slug)
        .limit(1)
        .execute()
    )
    return response.data[0] if response.data else None


@st.cache_data(ttl=300, show_spinner=False)
def get_plant_by_id(plant_id: str) -> Optional[Dict]:
    """Zoek één plant op ID (volledige gegevens)."""
    response = (
        get_client()
        .table("plants")
        .select("*")
        .eq("id", plant_id)
        .limit(1)
        .execute()
    )
    return response.data[0] if response.data else None


@st.cache_data(ttl=60, show_spinner=False)
def search_plants(query: str) -> List[Dict]:
    """Zoek planten op naam (wetenschappelijk of Nederlands)."""
    q = query.strip()
    if not q:
        return get_all_plants()

    client = get_client()

    # Zoek in wetenschappelijke naam (case-insensitive)
    sci = (
        client.table("plants")
        .select(LIST_COLUMNS)
        .ilike("scientific_name", f"%{q}%")
        .order("scientific_name")
        .execute()
    ).data or []

    sci_ids = {p["id"] for p in sci}

    # Zoek ook in Nederlandse namen via array-contains (exact woord)
    # Supabase ondersteunt cs (contains) op text arrays
    try:
        dutch = (
            client.table("plants")
            .select(LIST_COLUMNS)
            .ilike("scientific_name", f"%{q}%")  # fallback
            .order("scientific_name")
            .execute()
        ).data or []
    except Exception:
        dutch = []

    # Handmatige filterronde: controleer dutch_names array
    all_plants = get_all_plants()
    dutch_matches = [
        p for p in all_plants
        if p["id"] not in sci_ids
        and any(q.lower() in name.lower() for name in (p.get("dutch_names") or []))
    ]

    return sci + dutch_matches


@st.cache_data(ttl=60, show_spinner=False)
def filter_plants(
    edible: Optional[bool] = None,
    toxic: Optional[bool] = None,
    bloom_month: Optional[int] = None,
    light_needs: Optional[List[str]] = None,
    soil_types: Optional[List[str]] = None,
    categories: Optional[List[str]] = None,
) -> List[Dict]:
    """Filter planten op basis van eigenschappen."""
    client = get_client()
    q = client.table("plants").select(LIST_COLUMNS)

    if edible is not None:
        q = q.eq("edible", edible)
    if toxic is not None:
        q = q.eq("toxic", toxic)
    if bloom_month is not None:
        q = q.lte("bloom_start", bloom_month).gte("bloom_end", bloom_month)
    if light_needs:
        q = q.in_("light_needs", light_needs)
    if categories:
        q = q.in_("category", categories)

    results: List[Dict] = (q.order("scientific_name").execute()).data or []

    # Grondsoort-filter (array overlap) — Python-kant omdat Supabase SDK
    # geen native &&-operator biedt via de Python client
    if soil_types:
        results = [
            p for p in results
            if p.get("soil_types") and any(s in p["soil_types"] for s in soil_types)
        ]

    return results


# ── Soort van de dag ─────────────────────────────────────────────────────────

def get_plant_of_day(target_date: Optional[date] = None) -> Optional[Dict]:
    """
    Geeft de soort van de dag terug voor de opgegeven datum.
    1) Handmatig ingepland → die plant.
    2) Geen inplanning → plant die deze maand bloeit (deterministisch op datum).
    3) Geen bloeiende plant → willekeurige plant.
    """
    if target_date is None:
        target_date = date.today()

    client = get_client()

    # Handmatig ingeplande soort
    resp = (
        client.table("plant_of_day")
        .select("plant_id")
        .eq("scheduled_date", target_date.isoformat())
        .limit(1)
        .execute()
    )
    if resp.data:
        plant_id = resp.data[0]["plant_id"]
        plant_resp = (
            client.table("plants")
            .select(
                "id, scientific_name, dutch_names, slug, category, "
                "description, photos, bloom_start, bloom_end"
            )
            .eq("id", plant_id)
            .limit(1)
            .execute()
        )
        if plant_resp.data:
            return plant_resp.data[0]

    # Auto-selectie: plant die deze maand bloeit
    month = target_date.month
    bloom_resp = (
        client.table("plants")
        .select(
            "id, scientific_name, dutch_names, slug, category, "
            "description, photos, bloom_start, bloom_end"
        )
        .lte("bloom_start", month)
        .gte("bloom_end", month)
        .execute()
    )
    candidates = bloom_resp.data or []

    if not candidates:
        # Fallback: alle planten
        fallback = (
            client.table("plants")
            .select(
                "id, scientific_name, dutch_names, slug, category, "
                "description, photos, bloom_start, bloom_end"
            )
            .execute()
        )
        candidates = fallback.data or []

    if not candidates:
        return None

    # Deterministisch kiezen op basis van datum
    date_hash = int(hashlib.md5(target_date.isoformat().encode()).hexdigest(), 16)
    return candidates[date_hash % len(candidates)]


def get_pod_schedule(days: int = 14) -> Dict[str, Optional[str]]:
    """Geeft de ingeplande soort van de dag voor de komende `days` dagen."""
    client = get_client()
    today = date.today()
    dates = [today.isoformat()]
    from datetime import timedelta
    for i in range(1, days):
        dates.append((today + timedelta(days=i)).isoformat())

    resp = (
        client.table("plant_of_day")
        .select("scheduled_date, plant_id, plants(scientific_name, dutch_names)")
        .in_("scheduled_date", dates)
        .execute()
    )
    schedule: Dict[str, Any] = {}
    for row in (resp.data or []):
        schedule[row["scheduled_date"]] = row
    return schedule


# ── Soort van de dag schrijven ────────────────────────────────────────────────

def schedule_plant_of_day(
    plant_id: str,
    target_date: date,
    scheduled_by: str = "admin",
    notes: str = "",
) -> bool:
    """Plant een soort in als soort van de dag. Overschrijft bestaande inplanning."""
    try:
        get_admin_client().table("plant_of_day").upsert(
            {
                "plant_id": plant_id,
                "scheduled_date": target_date.isoformat(),
                "scheduled_by": scheduled_by,
                "notes": notes or None,
            },
            on_conflict="scheduled_date",
        ).execute()
        # Cache wissen zodat wijzigingen direct zichtbaar zijn
        get_plant_of_day.clear()
        get_pod_schedule.clear()
        return True
    except Exception as exc:
        st.error(f"Fout bij inplannen: {exc}")
        return False


def remove_pod_schedule(target_date: date) -> bool:
    """Verwijder een handmatige inplanning zodat de automatische selectie weer geldt."""
    try:
        get_admin_client().table("plant_of_day").delete().eq(
            "scheduled_date", target_date.isoformat()
        ).execute()
        get_plant_of_day.clear()
        get_pod_schedule.clear()
        return True
    except Exception as exc:
        st.error(f"Fout bij verwijderen inplanning: {exc}")
        return False


# ── Planten schrijven (admin) ─────────────────────────────────────────────────

def upsert_plant(plant_data: Dict) -> Optional[Dict]:
    """
    Maak een nieuwe plant aan of werk een bestaande bij.
    Gebruikt scientific_name als unieke sleutel.
    """
    if "scientific_name" in plant_data and not plant_data.get("slug"):
        plant_data["slug"] = make_slug(plant_data["scientific_name"])

    # Verwijder None-achtige lege strings om DB-contraints te respecteren
    cleaned = {k: v for k, v in plant_data.items() if v != ""}

    try:
        resp = (
            get_admin_client()
            .table("plants")
            .upsert(cleaned, on_conflict="scientific_name")
            .execute()
        )
        # Cache wissen
        get_all_plants.clear()
        get_plant_by_slug.clear()
        get_plant_by_id.clear()
        search_plants.clear()
        filter_plants.clear()
        return resp.data[0] if resp.data else None
    except Exception as exc:
        st.error(f"Fout bij opslaan: {exc}")
        return None


def delete_plant(plant_id: str) -> bool:
    """Verwijder een plant uit de database (onomkeerbaar)."""
    try:
        get_admin_client().table("plants").delete().eq("id", plant_id).execute()
        get_all_plants.clear()
        get_plant_by_slug.clear()
        get_plant_by_id.clear()
        return True
    except Exception as exc:
        st.error(f"Fout bij verwijderen: {exc}")
        return False
