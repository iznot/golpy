# Resultate

## Allgemeine Resultate

Die Simulation speichert nur die Konfigurationen ab, die zuvor noch nicht in anderer Form abgespielt wurden, also an anderer Position oder gespiegelt. Ich konnte die Simulation nur auf einem 5x5 grossen Gameboard abspielen lassen, da die 6x6 Simulation zu einem viel späteren Zeitpunkt als der Abgabetermin fertig geworden wäre. Die 5x5 Simulation konnte überhaupt nur durch parallele Prozesse, unterteilt nach genauer Grösse des Gameboards und Anzahl lebender, abgespielt werden.


{width: "60%"}
![Abb. 14: Säulendiagramm zu Objekten](occurence_of_objects.png)   

Am häufigsten kommen statische und selbst auslöschende Objekte vor, mit Abstand am seltensten gleitende. Überlebende Objekte kommen am zweithäufigsten vor.

Auch kam heraus, dass die meisten oszillierenden Objekte eine Periodizität von 2 haben. Mit einer Periodizität von drei existieren 5474 oszillierende Objekte, mit 15 wurden nur noch 14 abgespeichert. Diese 14 Anfangskonfiguration sind alle unterschiedlich, entwickeln sich jedoch zu dem genau gleichen Objekt. All diese Anfangskonfigurationen haben zwischen 12 und 16 lebende Zellen. 
Gleitende Objekte haben hier alle eine Periodizität von 4.

{width: "60%"}
![Abb. 14: Säulendiagramm zu Objekten nach Lebenden](objects_compared_alive.png)  

Des Weiteren fand ich heraus, dass auf einem 5x5 Gameboard kein gleitendes Objekt entstehen kann, wenn die Startkonfiguration weniger als fünf oder mehr als 22 lebende Zellen hat. Ein oszillierendes oder statisches Objekt kann bereits bei drei lebenden Zellen entstehen, letzteres sogar, wenn das gesamte Gameboard nur aus lebenden Zellen besteht.     

## Aufgabenbezogene Resultate

Das erste Problem,

1. Es existiert kein Algorithmus, der bestimmen kann, zu welchem Objekt die Anfangskonfiguration mutieren wird.

kann meine erste Funktion lösen, indem sie die gegebene Konfiguration mit den getesteten Anfangskonfigurationen abgleicht. Sobald eine Übereinstimmung gefunden wird, ist bekannt, welcher Objektgruppe die Konfiguration angehört.


Das zweite Problem,

1. Es existiert kein Algorithmus, der für alle Konfigurationen bestimmen kann, ob die eine aus der anderen entstehen wird.

kann meine zweite Funktion lösen, indem sie die zu vergleichende Konfiguration mit den getesteten Anfangskonfigurationen abgleicht. Sobald eine Affinität gefunden wird, gleicht sie die zu vergleichende Konfiguration mit den Generationen der übereinstimmenden Anfangskonfiguration ab. Falls hierbei eine Affinität gefunden wird, kann die zu testende Konfiguration aus der zu vergleichenden Konfiguration entstehen, ansonsten nicht.   

