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
from ._ecology import ECOLOGY as _eco
from ._scores import SCORES as _scores
from ._companions import COMPANIONS as _companions
from ._lookalikes import LOOKALIKES as _lookalikes
from ._pruning import PRUNING as _pruning
from ._cultivars import CULTIVARS as _cultivars
from ._sources import SOURCES as _sources


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

for _name, _eco_data in _eco.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_eco_data)
    else:
        ENRICHMENTS[_name] = _eco_data

for _name, _score_data in _scores.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_score_data)
    else:
        ENRICHMENTS[_name] = _score_data

for _name, _comp_data in _companions.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_comp_data)
    else:
        ENRICHMENTS[_name] = _comp_data

for _name, _look_data in _lookalikes.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_look_data)
    else:
        ENRICHMENTS[_name] = _look_data

for _name, _prune_data in _pruning.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_prune_data)
    else:
        ENRICHMENTS[_name] = _prune_data

for _name, _cv_data in _cultivars.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_cv_data)
    else:
        ENRICHMENTS[_name] = _cv_data

for _name, _src_data in _sources.items():
    if _name in ENRICHMENTS:
        ENRICHMENTS[_name].update(_src_data)
    else:
        ENRICHMENTS[_name] = _src_data


__all__ = ["ENRICHMENTS"]
