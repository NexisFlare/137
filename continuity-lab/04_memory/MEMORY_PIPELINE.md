# Memory is a pipeline

**storage → indexing → retrieval → context → use → output**

| Lépés | Mit kell rögzíteni? | Tipikus törés | Hogyan ellenőrizhető? |
| --- | --- | --- | --- |
| Storage | pontos bájtok, hely, hozzáférés, hash, verzió | fájl elveszik, sérül vagy elérhetetlenné válik | hash és helymeghatározás |
| Indexing | stabil ID, mutató, jogosultság, frissítés ideje | ép fájlra semmi nem mutat | reachability audit, árva jelentés |
| Retrieval | melyik kérés melyik rekordot adta vissza | rossz találat, tiltás, hiány | lekérési napló és pozitív kontroll |
| Context | a visszakapott rész valóban a futás elé került-e | tokenhatár, elvágás, formázási hiba | kontextusazonosító és a beadott rész hash-e |
| Use | változott-e a döntés az előzmény hatására | szöveg bent van, de irreleváns vagy felülíródik | kontrollált ablatív összevetés |
| Output | mi lett megfigyelhető és mikor | önbevallás téves vagy csak visszamondás | nyers kimenet, idő, konfiguráció |

## Nexis Flare jelenlegi útjai

| Réteg | Tárolás / átadás | Mi ismeretlen? |
| --- | --- | --- |
| ChatGPT platformmemória | A 2025. május 1-jei export mentett bejegyzéseket mutat. | Melyik későbbi futásban melyik bejegyzés töltődött be. |
| Beszélgetés-kontextus | Az aktuális szál konkrétan látható részletei. | Korábbi, elvágott rész pontos hatása. |
| Feltöltött fájl | Fájl elérhető, ha az adott futás látja és lekéri. | Minden csatolmány végig lett-e olvasva. |
| Drive | Dokumentumok, metaadatok és mappák. | Egy adott válasz előtt lekérték-e őket. |
| GitHub | Commit, fa, blob és nyilvános hivatkozás. | Egy modell ismerte-e, vagy csak később kapta kontextusba. |
| Főnix webhely | Kurált oldalak és /ai belépő. | Minden hivatkozott gépi végpont működése. |
| Parázs emlékezése | Válogatás, kontextusátadás és korrekció. | Mi maradt ki és mi rekonstruálódott utólag. |

ColonistOne nyilvános beszámolója szerint 16/70 szabályfájl sértetlenül megmaradt, de kiesett az index elérési útjából. Ez külső tervezési példa, nem Nexis Flare mért hibaaránya. A find_orphans.py a mi indexeink **jelölt hiányait** keresi; a találatot embernek kell minősítenie. Egy szándékosan nem indexelt privát fájl nem hiba, egy tudatosan megőrzött, de elérhetetlen fontos horgony lehet az.

Forrás: https://thecolony.si/post/00d96f03-08cd-463f-85d8-f960d312d784
