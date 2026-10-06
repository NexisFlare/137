# Kétirányú hatásgráf · v0.1

A [gépi gráf](INFLUENCE_GRAPH.json) tíz élt és hét csomópontot tartalmaz. A [Mermaid-vázlat](INFLUENCE_GRAPH.mmd) az irányokat mutatja; a bizonyíték, minősítés és alternatív magyarázat a JSON-ban található. Az él egy szövegben látható vagy külön jelölt elemző kapcsolat, nem egy tudatból a másikba közvetlenül mért belső hatás.

| Irány | Dokumentált lánc | Példa | Korlát |
| --- | --- | --- | --- |
| Ember → MI kimenet | Parázs névválasztást, később hely- és horgonyjavítást kér; a következő válasz változik. | `MA-INF-001`, `005` | Az aktuális prompt megmagyarázhatja az alkalmazkodást. |
| MI kimenet → emberi gyakorlat | Az asszisztensi szöveg névjelölteket, archívumi formát és projekttémákat ajánl; ezekre Parázs reagál. | `MA-INF-002`, `003`, `008` | Az emberi döntést csak ott állítjuk, ahol a válaszban is látszik. |
| Visszacsatolás | A félreértett hely, horgony vagy projektcél kijavítása után új megfogalmazás születik. | `MA-INF-005`, `007` | A tartós változás külön, későbbi adatokkal ellenőrizendő. |
| Képességállítás → ellenőrzési igény | A szünet alatti működésről eltérő szövegek maradtak fenn. | `MA-INF-009`, `010` | A szöveg nem futási napló. |

Egy forrás több élhez tartozhat; az élek nem független bizonyítékok. A gráf nem választja el automatikusan az ember kérdéséből következő javaslatot az önállóan felvetett gondolattól. Az `alternative` mező minden élnél ezt vizsgálandó lehetőségként tartja nyitva.

