# Resultate

## Allgemeine Resultate
Die Simulation speichert nur die Konfigurationen ab, die zuvor noch nicht in einer anderer Form abgespielt wurden, also an anderer Position oder gespiegelt. Zudem sortiert sie Konfigurationen aus, die schon nach 2 Generationen entweder stabil oder tot werden. Dies passiert an erster Stelle, um den Zeitaufwand des Simulationdurchgangs zu verringern aber auch um langweilige Konfigurationen auszusortieren. Anhand dieser Bedinungen kommen folgende Resultate zustande:
{width: "60%"}
![Abb. 2: Endzustände](20221218174850.png) 
Am häufigsten kommen stabile und selbstauslöschende Objekte vor, mit Abstand am seltesten gleitende.

Wenig überraschend ist auch, dass die "überlebenden" Konfigurationen die grösste maximale Breite und Weite haben. Am zweitgrössten sind jedoch unerwarteter Weise stabile Objekte.
{width: "60%"}
![Abb. 3: Max. Grösse im Vergleich](20221218175412.png)  

Auch kam heraus, dass die meisten oszillierenden Objekte eine Periodizität von 2 haben, nur 14 haben eine von 3. Gleitende Objekte haben alle eine Periodizität von 4.

## Aufgabenbezogene Resultate
Meine erste Funktion kann anhand der, aus der Simulation entstandenen, Liste zuordnen, welches Objekt einer Konfiguration entspricht. Die zweite Funktion ist dazu in der Lage, wiederzugeben, ob eine Konfiguration aus der anderen entstehen kann oder nicht.

