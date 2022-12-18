# Diskussion
Meine beiden Algorithmen sind funktionsfähig und können das gewünschte Resultat wiedergeben. Allerdings sind die beiden Probleme damit nicht gelöst. Keine beliebige Funktion kann abgefragt werden, sondern nur eine, die zuvor schon einmal abgespielt wurden. Zudem beschränkt sich diese vorgespielten Konfiguration auf ein 4x4 Feld, da das Abspielen der Simulation zu lange dauert. In einem nächsten Versuch müsste also die simulierende Funktion um einiges effizienter gemacht werden. 
Um die Probleme aber richtig lösen zu können, müsste ein Algorithmus gefunden werden, der ohne vorgespielte Konfigurationen weiss, wie der Spielverlauf der Konfiguration aussieht. 

Ein Lösungsansatz für das Voraussagen der Objektgruppe bestimmter Konfigurationen wäre, alle Konfigurationen, die im selben Objekt münden, zu vergleichen und nach Gemeinsamkeiten zu untersuchen. Wenn Gemeinsamkeiten gefunden werden können, sollte eine Funktion geschrieben werden, die die gegebene Konfiguration nach diesen untersucht und daraus folgert, zu welcher Objektgruppe die Konfiguration gehören muss. 

Eine Idee zur Lösung des zweiten Problems, also ob eine Konfiguration aus der anderen entstehen kann, kommt mir nicht. 
