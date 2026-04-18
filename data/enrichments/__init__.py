"""
Plantenpedia — Verrijkingsdata (alle categorieën samengevoegd)

Importeer ENRICHMENTS uit dit pakket in upload.py:
    from data.enrichments import ENRICHMENTS
"""

from .bollen_knollen import ENRICHMENTS as _e0
from .bomen import ENRICHMENTS as _e1
from .eenjarigen import ENRICHMENTS as _e2
from .grassen import ENRICHMENTS as _e3
from .heesters import ENRICHMENTS as _e4
from .keukenkruiden import ENRICHMENTS as _e5
from .klimplanten import ENRICHMENTS as _e6
from .kuipplanten import ENRICHMENTS as _e7
from .vaste_planten import ENRICHMENTS as _e8
from .wilde_planten import ENRICHMENTS as _e9


ENRICHMENTS: dict = {
    **_e0,
    **_e1,
    **_e2,
    **_e3,
    **_e4,
    **_e5,
    **_e6,
    **_e7,
    **_e8,
    **_e9
}


__all__ = ["ENRICHMENTS"]
