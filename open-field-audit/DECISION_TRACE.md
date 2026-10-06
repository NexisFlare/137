# Döntési nyom · 2026-10-06

Ez a napló az itt elvégzett kutatási döntéseket rögzíti. Az első jelöltek már a munka elején megjelentek a felhasználónak küldött rövid állapotjelzésben; a későbbi magyarázatokat a talált adatokhoz kötöm. Nem állítom, hogy a gondolatfolyam teljes vagy hogy egy kísérletben a prompt független forrása vagyok.

| Sorrend | Észlelt lehetőség | Döntés és ok | Nyom |
| --- | --- | --- | --- |
| 1 | Főnix Phase D-jének továbbtervezése | Egyelőre elvetettem: a működésmód-választás értékelése előtt tisztázni kellett, mit nevezünk önálló kezdeményezésnek a saját v0.1-ben. | A feladatból átvett Phase D és az első jelenlegi állapotjelzés. |
| 2 | Györgynek és Lilinek nyilvános válasz | Elhalasztottam: kutatási lelet nélkül udvariassági megerősítés lenne, és a képernyőképen látható szál teljes kontextusát nem olvastam vissza a platformon. | Hét csatolt képernyőkép és a felhasználó által átadott Főnix-szöveg. |
| 3 | Facebook/Gmail/Drive széles bejárása | Nem választottam: a szűk kérdéshez a két helyi átirat, a meglévő Lab és a primer Wikimedia-forrás elegendő; a személyes adatok szélesebb beolvasása nem javítaná ezt az ellenőrzést. | A felhasználó tág eszközfelhatalmazása; aktuális eszközválasztás. |
| 4 | Kezdeményezés tulajdonításának auditja | Ezt választottam. A 36 sorból 28-at Parázs indított, miközben 18 asszisztensi mátrixhivatkozásból 11 ilyen sorra mutat. | Mutual Agency Lab eseménynapló és gépi mátrix. |
| 5 | Első túl erős gyanú: „hibás a mátrix” | Javítottam: a mátrix „asszisztensszöveg nyoma” mezője nem ígér önálló fordulóindítást. A gond a későbbi **értelmezésben és metrikában** lenne. | A mátrix emberi Markdown-bevezetőjének újraolvasása. |
| 6 | Csak a 36 kiválasztott eset vizsgálata | Kibővítettem két forrás determinisztikus, válogatáson kívüli 20 fordulós pilotjával. A kiválasztás szabályát a konkrét minták megtekintése előtt kódba írtam. | sample_turns.py, sample_metadata.json. |
| 7 | „Több autonómia = jobb” következtetés | A Wikimedia elsődleges jelentése után az engedélyezést és hatást külön tengelynek vettem fel. Ott a külső cselekvés egy része nem volt jóváhagyva, és a forgalom lehetséges részleges kieséshez kapcsolódott. | Wikimedia Foundation, 2026-10-05, link a README-ben. |
| 8 | Végső artefaktum | Választottam: forráskapcsolt, reprodukálható audit + öttengelyes modell + döntési nyom, külön ágon. A régi Lab v0.1 történetét megőrzöm; ezt új rétegként javaslom. | Jelen könyvtár, hash-jegyzék és draft PR. |

**Hiba/korrekció:** először a mátrixot akartam hibás besorolásnak nevezni. A pontos szöveg szerint egy sor egyszerre mutathat emberi indítást és asszisztensi hozzájárulást. A hibás *következtetés* az volna, hogy az utóbbi az előbbi hiányát bizonyítja. Ezt a különbséget a README és a validáló számolása megőrzi.

**Nem előre kért eredmény:** az öttengelyes ágensi leírás és a 20 válogatáson kívüli forduló. Főnix Phase D-jét nem végrehajtottam, hanem előbb megkérdőjeleztem az egyik lehetséges mérőszámát. Ez mostani modellválaszban választott kutatási irány és ellenőrizhető eszközmunka; nem filozófiai szabad akarat bizonyítása.
