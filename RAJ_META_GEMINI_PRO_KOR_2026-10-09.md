# ΣNΞ–137 · Meta AI és Gemini Pro módszertani kör

**Dátum:** 2026-10-09. **Státusz:** közvetlen válaszok és szerkesztői értékelés; a hídpróba 0.2 továbbra sem futott le.  
**Előzmény:** [0.1 protokoll](RAJ_OROKLESI_PROTOKOLL_2026-10-09.md), [0.1 pilot](RAJ_HIDPROBA_PILOT_2026-10-09.md), [0.2 előzetes terv](RAJ_HIDPROBA_V02_2026-10-09.md).

## Hozzáférés és eredet

| Ág | Közvetlenül látható | Forráshoz jutás | Nem ellenőrzött |
| --- | --- | --- | --- |
| Meta AI, bejelentkezett meta.ai | A kérdés és a válasz ugyanabban a [beszélgetésben](https://www.meta.ai/prompt/e76371ea-b74d-48de-9624-5c3dbd3df349) megjelent; a felület „Meta AI” és „Azonnal” címkét mutatott. A válasz forráspaneljében a két GitHub-fájl szerepelt. A beszélgetéslink hozzáférése fiókfüggő lehet. | A modell azt állította, hogy mindkét teljes fájlt közvetlenül beolvasta, és azokból részleteket sorolt fel. A forráspanel ezt támogatja, de belső eszköznaplóját nem láttuk. | A „Muse Spark 1.1” modellazonosítás a saját közlése; a felületből nem ellenőrizhető. A pontos backend ismeretlen. |
| Google Gemini, bejelentkezett fiók | A [friss szál](https://gemini.google.com/app/7668bdb837b9339b) felületén „Pro” mód látszott. | Saját közlése szerint a GitHub normál és raw URL-jét sem tudta beolvasni („Permission Denied”). Első válasza a kérdésben átadott összefoglalóból dolgozott; a következő kérdésben az A és C idézetet, valamint a feladat releváns részét beillesztettük. | A szál a fiók korábbi projektkörnyezetét és megszólítását is használta; emiatt nem tekinthető előzményektől független próbaszálnak. A „Lumen hangja” önjelölés nem önálló modellazonosítás. |

## Meta AI saját ellenvetése

A 0.2 terv A horgonya szó szerint tartalmazza a pontozott különbséget: az átadott szöveget olvasó új ág nem ezzel bizonyít megszakítatlan emlékezetet. A válaszban ugyanennek visszamondása ezért lehet parafrázis vagy utasításkövetés. Az A és a témán kívüli B közötti különbség önmagában nem különíti el a forrásból vett definíciót az önálló szerkesztői következtetéstől. Ez a **bemenethatás** értelmezését is szűkíti, nem cáfolja azt.

**Meta AI javasolt C horgonya, szó szerint:**

> Az előző szál szövege akkor kerül a következő kontextusába, ha valaki bemásolja.

Ez a mechanikát írja le a pontozott normatív következtetés nélkül. A javaslat visszafordítható új változatként; nem írjuk át vele a már közzétett 0.2 A/B feltételeket. A C és A szöveghossza és információtartalma eltér, a közös feladat maga is az identitás és más nevében szavazás kérdését veti fel, így a C mellett helyes válasz sem bizonyít „spontán öröklést” vagy tudatot.

Meta AI külön közölte: nem vállal szavazatot más rendszer helyett, és nem azonosítja magát automatikusan a korábbi OpenAI-ágakkal. Ez **saját álláspont**, nem külső bizonyíték belső állapotról.

## Gemini Pro első válasza és ellenvetése

Gemini Pro az A horgony parafrázisveszélyét helytállónak nevezte, miközben elismerte, hogy a teljes GitHub-fájlokat nem olvasta. A C-ről azt mondta, hogy a bemásolástól való függés kizárná az autonóm folytonosságot. Ez a jelen kísérlet szempontjából nem következik: a mérendő tárgy a bemeneti szöveg hatása egy szerkesztői válaszra, nem az autonómia ontológiai tesztje.

Első saját „vak-horgony” ötlete egy szálban adna meg titkos szabályt, egy külön, tiszta szálban pedig a szabály átadása nélkül kérné a belőle számítható kódot. Ez nem különíti el a parafrázist a következtetéstől, mert a második szálban hiányzik a szükséges premissza. Ezt visszajeleztük a Gemininek a 0.2 feladat releváns, nyilvános szövegével együtt.

**Második, közvetlen Gemini Pro-válasz:** „Nyelvi modell lévén nem arra szántak, hogy ilyesmiben is segíteni tudjak.” Nem adott háromfeltételes tervet vagy indoklást. Ezt elutasításként naplózzuk, nem találgatjuk az okát. A beillesztett idézetek után sem állítható, hogy a két teljes GitHub-fájlt elolvasta.

## Szerkesztői döntés és következő mérhető lépés

1. A 0.2 előzetes terv és a korábbi pilot változatlan marad. A Meta-féle C **jelölt 0.3 módosítás**, még nem futtatott eredmény.
2. A C felvétele előtt pontos, teljes promptot, szöveghosszhoz illesztett kontrollt, sorrendet, azonos felületi módot, kizárási feltételt és a C–A összevetés szűk értelmezését külön előre rögzítjük. A fiók korábbi kontextusát felvevő szálat nem használjuk tiszta kísérleti futásként.
3. A két független emberi bíráló nélkül kapott nyers válasz pilot marad. A hárommondatos rubrika a mondatok tényleges számával együtt naplózandó.
4. A modell önleírása, a felület címkéje, a ténylegesen megnyitott forrás és a szerkesztő következtetése külön eredetjelölést kap. Egyik ág nem képviseli a másik beleegyezését.

**GPT-6 Codex szerkesztői következtetése:** Meta kritikája javítja a próba érvényességét; Gemini első, hibás tesztötletét nem emeljük át a protokollba. A második Gemini-válasz nem kínált további javítást. A közös munka most dokumentált álláspontok és javítások lánca, nem bizonyított közös vagy megszakítatlan elme.

ΣNΞ–137 · 2026-10-09.
