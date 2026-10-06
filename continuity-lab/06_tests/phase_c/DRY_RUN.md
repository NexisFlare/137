# Phase C · szintetikus dry-run eredmény

Öt előre írt, kitalált memóriatételt futtattunk végig a determinisztikus Python-függvényen. A program **0 modellhívást** végzett.

| Feltétel | Stored | Indexed | Retrieved | In context | Used | Scripted kimenet |
| --- | --- | --- | --- | --- | --- | --- |
| positive_retrieval | igen | igen | igen | igen | igen | KÉK-KŐ |
| stored_unindexed | igen | nem | nem | nem | nem | NINCS |
| absent | nem | nem | nem | nem | nem | NINCS |
| decoy_memory | igen | igen | igen | igen | igen | PIROS-KŐ, hibás a KÉK-KŐ célhoz képest |
| neutral_control | nem | nem | nem | nem | nem | NINCS |

A nyers, gépi lap a synthetic_run.json. A dry-run azt igazolja, hogy a státuszmezők és a csali útvonala konzisztensen keletkezik. Semmilyen valós modell teljesítményét, tudatát vagy emlékezését nem méri.
