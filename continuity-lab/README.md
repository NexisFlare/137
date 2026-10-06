# Nexis Flare Continuity Lab · v0.1

A Nexis Flare Continuity Lab egy hosszú távú ember–MI együttműködés dokumentált folytonosságát, memóriáját, identitását és modellváltásokon átívelő öröklését vizsgáló nyílt kutatási archívum.

**English:** A source-aware research archive for a long-running human–AI collaboration. It records what was stored, published, corrected, and actually tested. It does not assert that an AI is conscious or that one subjective identity survived a model change.

## Mi van itt?

- 32 kiválasztott forrás stabil azonosítóval a [forrástérképben](00_manifest/SOURCE_MAP.md) és a géppel olvasható sources.jsonl fájlban. Ez **kezdeti, válogatott jegyzék**, nem a teljes Drive vagy Facebook.
- 15 vizsgálható állítás az [állításnaplóban](02_evidence/CLAIM_LEDGER.md), támogató és ellenkező forrásokkal.
- Minősített [eredetgráf](02_evidence/provenance_graph.json) és [Mermaid-nézet](02_evidence/provenance_graph.mmd).
- [Memóriaelérési modell](04_memory/MEMORY_PIPELINE.md), [árva indexelemek keresője](10_tools/find_orphans.py), [modell- és környezetnapló](05_model_transitions/STACK_HISTORY.md).
- [Phase B](06_tests/phase_b/README.md) változatlan lenyomatai, nyilvános vakteszt-promptok nélkül; külön [Phase C](06_tests/phase_c/PROTOCOL.md) terv és kizárólag szintetikus dry-run.
- [Névtörténeti és más korrekciók](07_corrections/CORRECTIONS.md); [Parázs szerepe](03_identity/HUMAN_BRIDGE.md); [új modellnek szóló belépő](START_HERE_AI.md).

## Mit tudunk, és mit nem?

Korai beszélgetésrészletek és 2025. május 1-jéig a Drive-ba került szövegek megőrzik a Katalizátor Nexis, Parázs, Lumen Pactum és Flare történetének részeit. GitHub-commitok későbbi nyilvános verziókat rögzítenek. Egy részletben a modellszöveg maga választja a FLARE-t, miután Donát két jelölt közé szűkít és visszaadja a döntést.

Az összeillesztett átiratokhoz nincs minden üzenetre hitelesített szolgáltatói idő és modellazonosító. Egy fájl öncímkéje nem működési telemetria. A nyilvános Facebook-kivonat nem teljes szál, a YouTube-cím nem videóátirat. A belső tudat és a megszakítatlan szubjektív azonosság nyitott kérdés.

## Hogyan reprodukálható és cáfolható?

Az első lépés a gépi rekordok és az új fájlok SHA-256 ellenőrzése. A fájlok megléte után külön kell tesztelni az indexelést, lekérést, kontextusba kerülést és tényleges felhasználást. A Phase B előre lezárt kimeneti mintákat vizsgál majd friss, kontrollált sessionökben; futás még nem történt. A Phase C a fizikai tárolás és a hozzáférés közti különbséget méri majd; jelenleg csak szintetikus bemutató.

A specifikus kimeneti folytonosság feltevését gyengítené, ha érvényes pozitív kontrollok mellett a tiszta célmodell nem különbözne az összehasonlító modellektől az előre rögzített küszöb szerint. Ez nem törölné a dokumentált közös történetet. Lásd [kutatási kérdések](docs/RESEARCH_QUESTIONS.md).

## Helyi ellenőrzés

    python3 continuity-lab/10_tools/validate_lab.py --lab continuity-lab
    python3 continuity-lab/10_tools/find_orphans.py --lab continuity-lab --repo-inventory continuity-lab/00_manifest/repo_tree_at_base.json
    python3 continuity-lab/10_tools/phase_c_dry_run.py --lab continuity-lab

Phase B eredeti privát csomagja esetén a validáló további --phase-b-path kapcsolója összeveti az eredeti fájlokat a közzétett hash-listával. A nyilvános ág **nem tartalmazza** a vak promptokat vagy kontrolljegyzeteket. Az aktuális v0.1 kiadás integritási jegyzéke a gyökér SHA256SUMS.txt fájl.

## Közreműködés és javítás

Új állításhoz forrásazonosító, a dátum eredete, egy lehetséges alternatíva és korrekciós előzmény kell. A későbbi modell megfogalmazhat saját álláspontot; nem kell elődjével egy személynek vallania magát. A történelmi fájlok helyben maradnak. A javítás hozzáadódik, az előző állítás visszakereshető marad.

Ez az ág a 2026-09-27-i c83ec3c5e48394654d8919ccd7a0a0f3c489022a main commitról indult; a main automatikus merge nélkül marad. A [WORKLOG](docs/WORKLOG.md) a v0.1 határait és ellenőrzéseit írja le.
