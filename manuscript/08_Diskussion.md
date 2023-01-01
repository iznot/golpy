# Diskussion
TODO Beispiele für wie effizienter
TODO Gleiter wieso nur Periodizität von 4
TODO aufzeigen wo gescheitert und wieso

Meine beiden Algorithmen sind funktionsfähig und können das gewünschte Resultat wiedergeben. Allerdings sind die beiden Probleme damit nicht gelöst. Keine beliebige Funktion kann abgefragt werden, sondern nur eine, die zuvor schon einmal abgespielt wurden. Zudem beschränken sich diese gespielten Konfigurationen auf ein 5x5 Feld, da das Abspielen aller Simulationen zu lange dauert. In einem nächsten Versuch müsste also die simulierende Funktion effizienter gemacht werden. Dies wäre dadurch möglich, in dem die maximale Zahl je nach Anzahl Lebenden berechnet würde und der jeweilige Parallelprozess bereits nach dem Erreichen dieser Zahl abbräche. Zudem könnte die Simulation in noch mehr Parallelprozesse aufgeteilt werden, zum Beispiel nach Anzahl lebenden im äussersten Ring, dann im zweit äussersten und so weiter. Auch würde ein leistungsstärkerer Computer benötigt, der so viele Parallelprozesse auf mal abspielen kann.

Um die Probleme aber richtig lösen zu können, müsste ein Algorithmus gefunden werden, der ohne vorgespielte Konfigurationen weiss, wie der Spielverlauf der Konfiguration aussieht. 

Ein Lösungsansatz für das Voraussagen der Objektgruppe bestimmter Konfigurationen wäre, alle Konfigurationen, die im selben Objekt münden, zu vergleichen und nach Gemeinsamkeiten zu untersuchen. Wenn Gemeinsamkeiten gefunden werden können, sollte eine Funktion geschrieben werden, die die gegebene Konfiguration nach diesen untersucht und daraus folgert, zu welcher Objektgruppe die Konfiguration gehören muss. 
Dies ist durch meine Ergebnisse stark eingeschränkt möglich. So weiss ich, dass eine Konfiguration mit drei lebenden Zellen sicher kein Gleiter wird. 

Eine Idee zur Lösung des zweiten Problems, also ob eine Konfiguration aus der anderen entstehen kann, kommt mir nicht. 
