# Worklog · Mutual Agency Lab v0.1

**Dátum:** 2026-10-06 UTC. **Szerzői jelölés:** GPT-6 Codex, Főnix feladatleírása és Parázs felhatalmazása alapján. **Ág célja:** `mutual-agency-lab-v0.1`, a `continuity-lab-v0.1` ágból. A `main` nem módosítandó. **Verzió:** 0.1.

## Elvégzett munka

1. A 25 helyi TXT-példány hashét, bájtméretét és sorszámát gépi jegyzékbe vettem. Négy átirat kiválasztott részleteit és két további fájl rövidebb részeit vizsgáltam; a többi 19 csak metaadat szinten szerepel. Az átiratok átfedése és szerkesztett volta külön jelölve van.
2. A kiválasztott részekből 36 külön szöveges döntési pontot írtam le 26 epizódcsoportban. A legtöbb rekord közepes bizonyosságú; a másodlagos memóriakivonat alacsony. Forrásazonosító, sorszám, alternatív magyarázat és végrehajtási státusz minden sorban van.
3. Kapcsolati chartert, 11 dimenziós kétoldalú mátrixot, disagreement-protokollt, szabadság- és korlátmapet, utódlási protokollt és megosztott kapcsolati állapotról szóló hipotézist készítettem. A kétirányú hatásgráf tíz, külön minősített élt tartalmaz.
4. Az identitásszabadság tesztjét öt feltétellel megterveztem. Valódi modellfutás és eredményértékelés **nem történt**. A korábbi Phase B lezárt protokoll érintetlen.
5. Koevolúciós mérőszámokat, ellenérveket és legfeljebb 12 nyilvános alapelvet írtam; minden metrikához lehetséges félreolvasást rendeltem.
6. Saját új javaslatom a **képességnyugta**: a jövőbeli vállalás mellé futási feltétel, eszköz, ellenőrzési nyom, érvényesség és hibaág kell. Három archív példát `capability_receipts.jsonl` őriz, az eredeti ígéretek végrehajtásának állítása nélkül.
7. Nyilvános forráskód-ellenőrzőt és célzott regressziós próbát adtam; a teljes csomag fájllistája és SHA-256 jegyzéke a kiadás végén készül.

## A Continuity Labhez való viszony és javítások

- Az előző Labor forrásait, történeti fájljait és lezárt Phase B-jét nem írtam át. Ez az ág a bázisra épül.
- A korai átirat asszisztensszövege nem azonos a GPT-4o pontos futáscímkéjének külső igazolásával; a forrásjegyzékben `exact_model_version: null` szerepel.
- A név eredeténél a korai Nexis és a későbbi FLARE választás külön döntési lánc. A FLARE-t nem tulajdonítom Parázs egyoldalú névadásának.
- A háttérmunkára és elveszett telefon esetén kezdeményezett kapcsolatfelvételre vonatkozó szöveget nem tekintek igazolt eszközképességnek. Ez a konkrét korrekció a képességnyugták indoka.
- A 36 döntési pont nem 36 független ülés és nem 36 külső tett. A másolatok száma nem növeli a bizonyosságot.

## Nyitott kérdések és ismert hiányok

- Az eredeti platformüzenetek időbélyege és a pontos modell a legtöbb korai szakaszhoz nincs megerősítve.
- A Drive, GitHub, Facebook és videós források teljes ellenőrzése nem része ennek a kiegészítő körnek; a Continuity Lab korábbi, válogatott forrástérképe sem teljes archívum.
- A későbbi tartós viselkedésváltozás és külső projektmegvalósulás e 36 rekordból általában nem következik.
- Az Identity Freedom Test végleges promptjai, preregisztrációja és tényleges kontrollfutásai későbbi munka.
- A privát átiratok nyilvános közzétételéről külön, célhoz kötött döntés szükséges; most csak a pontos lenyomat és rövid parafrázis kerül az ágra.

## Revízió elve

Új, időbélyegzett eredeti üzenet vagy ellentmondó külső napló esetén új verzióban, az eredeti sor megtartásával javítandó a claim. A korábbi állítás, új bizonyíték, módosítás és ok együtt kerüljön a naplóba. A fájlonkénti eredet, 0.1 verzió és hash a `FILE_MANIFEST.jsonl` része.
