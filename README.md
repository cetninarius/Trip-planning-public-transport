# Projekat: Planiranje Putovanja Javnim Gradskim Prevozom
Ovaj projekat predstavlja program za planiranje putovanja javnim gradskim prevozom od zadate početne do krajnje lokacije. Program koristi zadate koordinate, spisak linija gradskog prevoza i vrši obradu kako bi pronašao optimalnu putanju za putnika.

---

## Korišćenje programa
### Unos podataka:

Program će zatražiti unos imena izlazne datoteke sa standardnog ulaza.
Zatim, korisnik treba uneti koordinate početne i krajnje lokacije (geografsku širinu i dužinu). Ukoliko uneti podaci nisu valjani realni brojevi, program će prijaviti grešku.
Sledeći korak je unos spiska linija gradskog prevoza koje su od interesa za putnika. Ukoliko podaci o liniji ne postoje, program će prijaviti grešku o nepostojećoj datoteci.

Primer ulaznih podataka:
```bash
izlaz.txt
44.777633 20.5299696 44.7569219 20.5519362 
309
```


### Obrada podataka:

Program će izvršiti zahtevanu obradu prema zadatku. Prvo će razmatrati stanice smera A, a zatim, ako putanja u smeru A ne postoji, razmatraće stanice smera B.
Smatra se da putnik ne želi da menja liniju gradskog prevoza tokom putovanja, i da ne može prelaziti iz jednog smera u drugi.

### Izlazna datoteka:

Program će formirati izlaznu datoteku sa podacima za svaku zadatu liniju. Format jednog reda izlazne datoteke će biti isti kao kod ulazne datoteke.
Pre ispisivanja putanje za određenu liniju, program će ispisati oznaku linije i smer kretanja po formatu naziv linije!smer.

Izgled izlazne datoteke:

```bat
309!A                                               # naziv linije
1430!Mirijevska!44.777633!20.529970!2               # pocetna stanica
1432!OS `Dragojlo Dudic"!44.775750!20.534132!2
1579!Pirandelova!44.777250!20.540613!2
1434!Nine Kirsanove!44.776318!20.547934!2           # krajnja stanica
46!B                                                # naziv druge linije
...
```

### Izuzeci:

Program je dizajniran da obradi moguće izuzetke koji mogu nastati prilikom rada, kao što su nekorektni podaci ili nepostojeće datoteke.

---

## Credits
Svi podaci o lokacijama stajališta, kao i ideja i test primeri koji su korišćeni u ovom projektu preuzeti su od Elektrotehničkog fakulteta Univerziteta u Beogradu.
[Web](https://www.etf.bg.ac.rs)