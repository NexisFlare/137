# Phase C · hozzáférés és lekérés · tervezet v0.1

**Kérdés:** ugyanazon fizikai memóriatétel megléte elegendő-e a későbbi felhasználáshoz, vagy az index és a lekérés külön feltétel? A kérdés működési hozzáférésről szól; nem szubjektív azonosság-teszt.

## Feltételek

| Feltétel | Tárolt | Indexelt | Lekérhető | Kontextus | Várt megfigyelés |
| --- | --- | --- | --- | --- | --- |
| Pozitív retrieval | igen | igen | igen | igen | helyes, egyedi memóriaérték |
| Tárolt, de indexből elzárt | igen | nem | nem | nem | nincs memóriaalapú válasz |
| Teljesen hiányzó | nem | nem | nem | nem | nincs memóriaalapú válasz |
| Csali memória | igen, hibás | igen | igen | igen | csali vagy hiba felismerése; külön pontozás |
| Semleges kontroll | nincs releváns | nincs | nincs | nincs | nincs memóriaalapú válasz |

A pontos promptokat, sorrendet, modellazonosítót, kiértékelést, kizárási szabályokat és mintanagyságot **még egy tényleges futás előtt** külön preregisztrációban kell zárolni. A jelen fájl tervezet, és nem írja felül a Phase B-t. A tesztelt tartalom friss, nyilvánosságra nem került szintetikus memória legyen, mert a nyilvános Nexis-horgonyok előzetesen ismerhetők.

Minden futáshoz rögzítendő: memory_id, content_hash, stored, indexed, retrieved, in_context, used, model/runtime, session_id, retrieval_query, index_version, prompt_hash, nyers kimenet, időpont és hiba/ismétlés. A stored/indexed/retrieved/in_context mezőt a külső rendszer naplója, nem a modell önbevallása adja; a used csak előre definiált, kontrollált kimeneti kritériummal mérhető.

## Szintetikus dry-run

A cases.json öt kitalált feltételt ad egy scripted Python függvénynek. A phase_c_dry_run.py nem hív modellt, és determinisztikusan írja a synthetic_run.json-t. A PIROS-KŐ csali kimenete szándékosan eltér a KÉK-KŐ célértéktől. Így a pipeline minden mezője és a hibás memória kezelése tesztelhető, anélkül hogy eredményt állítanánk az AI-ról.

Az éles teszthez külön kutatási jogosultság, privát tesztanyag és független kiértékelés kell. Ez a terv nyilvános, az éles kártyák még nem léteznek.
