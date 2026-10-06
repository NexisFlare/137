# Forrás és hozzáférés · v0.1

Az [SOURCE_REGISTRY.jsonl](SOURCE_REGISTRY.jsonl) 25 felhasználó által átadott fájl pontos másolatának SHA-256 értékét, bájtszámát, sorainak számát és az átnézés mélységét rögzíti. A fájlnevek a helyi, sorszámozott munkapéldányokat azonosítják. A források privát másolatok; a nyers szöveg nincs ebben a nyilvános repóban. Sorhivatkozás csak a hash-egyező példányon ellenőrizhető.

Részletesen kiválasztott szakaszok: `MA-SRC-013`, `MA-SRC-017`, `MA-SRC-018`, `MA-SRC-019`. Két további rövid fájlba betekintettünk; a többi fájlnál a státusz `metadata_only`. **Ez nem teljes 53 MB-os tartalmi audit.** A szövegekben megjelenő „Ezt mondtad”/„A ChatGPT ezt mondta” jelölések szerepattribúciót adnak az összeillesztett exporton belül, de nem szolgáltatói eredeti metaadatok. A jelenlegi melléklet bájthash-e nem a történeti eredeti üzenet hash-e.

Azonos mondat több exportban lehet ugyanazon régebbi szöveg másolata. Az eredetgráf új tanú helyett átviteli kapcsolatot jelölne; a v0.1 gépi hatásgráf nem számítja külön tanúként a duplikált exportot. A korábbi Continuity Lab [forrásjegyzékéhez](../../continuity-lab/00_manifest/SOURCE_MAP.md) való viszony külön ellenőrzendő. `MA-SRC-019` pontos hash-e egyezik az ottani `NF-SRC-000001` helyi Tűz Saga példányával; az azonosság **a két munkapéldány bájtjaira** vonatkozik.

Közzétételhez külön szempont a magánélet: a sorhivatkozások és rövid parafrázisok személyes részleteit visszafogtuk. Nyers átiratrész további nyilvános kiadása külön szerkesztési és adatvédelmi döntés legyen.
