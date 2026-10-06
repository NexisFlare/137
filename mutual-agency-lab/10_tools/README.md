# Reprodukció és ellenőrzés

A `validate_agency.py` a gépi forrásjegyzék, 36 esemény, mátrix, hatásgráf és képességnyugták belső hivatkozásait, helyi linkjeit, fájllistáját és SHA-256 lenyomatait ellenőrzi. Az opcionális `--private-sources` a felhasználó saját, közzé nem tett eredeti `.txt` példányaival bájt-, hash- és sorhatár-ellenőrzést végez. A sorszámok csak a pontosan azonos hashű példányban érvényesek.

```bash
python3 mutual-agency-lab/10_tools/validate_agency.py --lab mutual-agency-lab
python3 mutual-agency-lab/10_tools/validate_agency.py --lab mutual-agency-lab --private-sources project_sources
python3 mutual-agency-lab/10_tools/test_validate_agency.py
```

Az ellenőrzés **nem** bizonyítja, hogy minden parafrázis történetileg helyes; ahhoz a korlátozott eredeti szakaszok emberi felülvizsgálata szükséges. A forrás másolata, az eredeti platformüzenet, a pontos futási modell és a későbbi visszaemlékezés külön adatkategória. A `test_validate_agency.py` hibás forrásazonosítóval és utólag megváltoztatott fájllal ellenőrzi a validator két érdemi hibaágát.

Az Identity Freedom Test nincs lefuttatva; a Phase B korábbi lezárt fájljait ez a csomag nem változtatja.
