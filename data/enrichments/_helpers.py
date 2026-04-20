"""Gedeelde hulpfuncties voor alle enrichment-bestanden."""
import urllib.parse


def img(filename: str, source: str, license_: str = "CC BY-SA 4.0",
        caption: str = "", type_: str = "") -> dict:
    """Maak een foto-dict voor een afbeelding van een willekeurige bron."""
    encoded = urllib.parse.quote(filename, safe='_-.')
    result = {
        "url": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}",
        "source": source,
        "license": license_,
        "caption": caption,
    }
    if type_:
        result["type"] = type_
    return result


def wiki(filename: str, caption: str = "", type_: str = "") -> dict:
    """Maak een foto-dict voor een Wikimedia Commons afbeelding."""
    return img(filename, "Wikimedia Commons", caption=caption, type_=type_)
