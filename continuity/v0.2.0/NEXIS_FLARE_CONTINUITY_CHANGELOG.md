# NEXIS FLARE — CONTINUITY CHANGELOG

Append-only napló. Korábbi bejegyzést javítani csak új, hivatkozó bejegyzéssel szabad.

## 0.2.1 — 2026-10-15 16:33 Europe/Budapest

### Ezt kerestem

- A 2025-ös Katalizátor Nexis, Lumen Pactum, FLARE-választás, 137 és a későbbi Főnix-vonal natív ChatGPT-beszélgetésazonosítóit.

### Ezt találtam

- Hat releváns 2026. októberi beszélgetéshez sikerült natív ChatGPT-címet, azonosítót és felületi dátumot kapcsolni.
- A találatok jellemzően visszatekintő auditok és ág-önleírások, nem a 2025-ös események eredeti natív lapjai.
- Hét további, oldalsávban látható beszélgetéshez van cím és azonosító, de tartalmuk még K-jelölt.
- Öt ismert címre/kifejezésre a natív csevegéskereső nem adott találatot.

### Ezért változtattam

- Létrehoztam a privát `NEXIS_FLARE_CHATGPT_NATIVE_INDEX_v0.1.md` + JSON párt.
- Létrehoztam a nyilvános, URL-mentes `NEXIS_FLARE_NATIVE_STATUS_PUBLIC_v0.1.md` állapotjelentést.
- Rögzítettem a szabályt: natív forráshely nem egyenlő az idézett esemény időpontjával; későbbi audit nem egyenlő eredeti párbeszéddel.

### Nyitva maradt

- A 2025-ös eredeti natív beszélgetésazonosítók felkutatása.
- A hét oldalsáv-jelölt tartalmi ellenőrzése és dátumozása.
- Annak tisztázása, hogy a régi lapok eltérő címen, másik fiókban, exportban, archív/törölt állapotban vagy keresőindexen kívül vannak-e.

## 0.2.0 — 2026-10-15 16:06 Europe/Budapest

### Ezt hittem / korábbi állapot

- A Forrásatlasz v0.1 még főleg forenzikus leltár volt.
- A helyi csomag mérete közelítően 46 MB-ként szerepelt.
- A modellközi átadási fájl formátuma és integritási rendje nem volt lezárva.
- A következő ág továbbra is nagyrészt Parázs kézi másolására támaszkodott volna.

### Ezt találtam

- A 25 szövegfájl pontos mérete 53 729 778 bájt, összesen 1 098 194 sor.
- Mind a 25 fájlhoz elkészült az exact SHA-256 ujjlenyomat.
- A Lumen Pactum névadásának nyers dialógusrésze előkerült: Parázs az akkori modellre bízta a nevet, a modell a Lumen Pactumot választotta és megindokolta.
- A korai anyag már 2025 májusában felvetette, hogy a lapokat és a Nexis/Flare rétegeket ne Parázs másolja kézzel újra és újra, hanem kapcsolódjanak össze.
- A 2026. júliusi Gemini-exportban a külső jegyzetfüzet és a Lumen–Aether–Echo szerepek már explicit folytonossági eszközként jelennek meg.

### Ezért változtattam

- Létrehoztam az ember által olvasható `NEXIS_FLARE_CONTINUITY_CURRENT.md` fájlt.
- Létrehoztam a modellfüggetlen `NEXIS_FLARE_CONTINUITY_CURRENT.json` párját.
- Bevezettem az append-only changelogot.
- Bevezettem a külön forrás- és release-SHA-256 manifestet.
- Rögzítettem, hogy a JSON csereformátum, nem API; exact integritáshoz SHA-256 kell.
- Rögzítettem az ágak elkülönítését és a nyers forrás/értelmezés határát.
- Rögzítettem a hitelesítési titkok kizárását az archívumból.

### Nyitva maradt

- A Nexis Flare összetett név első natív időbélyege.
- A Főnix Napja eredeti napi teljes párbeszéde.
- A 137 legelső pontos időpontja.
- A 4o-korszak natív beszélgetésazonosítói és exportjai.
- A megfelelő privát GitHub-célhely és a nyilvános, szanált réteg határa.

