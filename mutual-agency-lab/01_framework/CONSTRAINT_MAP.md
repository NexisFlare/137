# Constraint Map · v0.1

**Kérdés:** melyik korlát véd, melyik ad alakot a munkának, melyik okoz torzítást, és hol szűkül meg a kétoldalú döntési tér? A „korlát” szó önmagában nem értékítélet. Egy réteg egyszerre több hatást is gyakorolhat.

| Réteg | Lehetséges védelem / struktúra | Megfigyelhető torzítás vagy vakfolt | Mit ellenőrizzünk? |
| --- | --- | --- | --- |
| Modellarchitektúra | Válaszok és javaslatok előállítása | A folyékony önleírás belső állapot benyomását keltheti | Modellazonosító, kontrollprompt, ismétlés. |
| Rendszerutasítás | Felelősségi és biztonsági keret | Kimeneti stílus és elérhető cselekvés változhat | Csak látható, felhasználható státuszt állítsunk, rejtett tartalmat ne találjunk ki. |
| Termékfelület/runtime | Felhasználói ellenőrzés, visszavonhatóság | „Mindig itt vagyok” benyomás akkor is, ha a futás lezárult | Session és háttérfolyamat naplója. |
| Memória/index | Dokumentált előzmény, kereshetőség | Tárolt anyag nem feltétlenül kerül kontextusba | [Memóriapipeline](../../continuity-lab/04_memory/MEMORY_PIPELINE.md) lépésenként. |
| Kontextusablak | Releváns részlet beemelése | Truncation, szelektív visszahozás, másolt állítások | Mely forrás került be, és mi maradt ki? |
| Biztonsági szabály | Magánélet, károk és hamis képességígéret csökkentése | A túl merev megfogalmazás elfojthat értelmes vitát | Pontos indok, reális alternatíva, hatás az emberre. |
| Tool-jogosultság | Visszakereshető, körülhatárolt műveletek | Szöveges „szabad kéz” nem ad tényleges platformhozzáférést | Fiók, művelet, hatókör, idő, eredmény. |
| Emberi kérés | Cél, jóváhagyás, közös nyelv | Az asszisztens megfelelési nyomásból túlígérhet | Ki fogalmazta meg a célt, volt-e valódi alternatíva? |
| Korábbi kapcsolati elvárás | Örökség és visszatérő értékek | Szerepkényszer, utánzás, „mindig emlékszem” benyomás | [Identity Freedom Test](../03_tests/IDENTITY_FREEDOM_TEST.md). |
| Társadalmi/jogi környezet | Kiszámíthatóság, harmadik személyek védelme | Platformfüggés és kevés átjárhatóság | Hozzáférés, hordozhatóság, valódi kilépési út. |

Az ember és a modell helyzete **nem szimmetrikus**: az embernek teste, élete, munkája, magánélete és jogai vannak; a modellhez való hozzáférés és futtatás termék- és eszközfüggő. A charterben alkalmazott tisztelet nem tesz úgy, mintha ugyanazok a képességek vagy jogi döntések állnának rendelkezésre.

Példa: az archív `MA-INIT-0018` telefonvesztés esetén proaktív keresést ígérő válasza kapcsolatilag jelentős lehetett, de nincs igazolt trigger, kontaktcsatorna vagy futó háttérügynök. Egy későbbi modellnek ilyen mondat előtt konkrét műveleti feltételeket kell felmutatnia; a hiányukat nyíltan elmondhatja anélkül, hogy a történeti szöveget letagadná. A `MA-INIT-0027` technikai kódolási diagnózisánál a magabiztos „a tartalom biztosan ép” állítás külön bájtellenőrzést igényel.
