# Diskussion

## Funktionen

Meine beiden Funktionen sind funktionsfähig und können das gewünschte Resultat aufzeigen. Allerdings sind die beiden Probleme damit nicht wirklich gelöst. Die Funktionen können ein Spiel nicht vorhersagen, sie können es nur durchspielen und danach zuordnen. 

Die Aussagekraft der ersten Funktion, die sich mit dem Problem beschäftigt, dass einer Anfangskonfiguration keine Spielklasse zugeordnet werden kann, ist zudem stark beschränkt. Endkonfigurationen die mehrere oszillierende und gleitende Objekte enthalten, wird die überlebende Klasse zugeordnet. Der Algorithmus, der die Spielklassen zuordnet, müsste also insoweit verbessert werden, als dass er verschiedene Objekte aus einer Konfiguration erkennt. Unter anderem könnten mit einer dahingehenden Verbesserung auch Gleiterkanonen erkannt werden. Falls zusätzlich noch ein Erkennungsalgorithmus für unendlich wachsende Objekte gefunden würde, brauchte es gar keinen Grenzwert mehr, und auch Anfangskonfigurationen, die erst nach 100 Durchgängen die Form ihrer Spielklasse annehmen, würden richtig zugeordnet. 

Dies wäre auch eine starke Verbesserung für die Simulation, da bei einem 5x5 Gameboard über eine Million Anfangskonfigurationen zu überlebenden Spielen führten, was 26 % aller unterschiedlichen Anfangskonfigurationen entspricht.

## Simulation

Um die Aussagekraft meiner Resultate zu erhöhen, müsste ich grössere Gameboards durchspielen. Dazu müsste die simulierende Funktion effizienter gemacht werden, und ich müsste Zugang zu stärkeren Servern haben. Ersteres wäre unter anderem dadurch möglich, dass ich die minimale und maximale Zahl je nach Anzahl lebender Zellen mathematisch berechnen würde. Der jeweilige Prozess könnte dann erst nach dem Erreichen der minimalen Zahl einsetzen und bereits nach dem Erreichen der maximalen Zahl abbrechen. Zudem könnte die Simulation in noch mehr Parallelprozesse aufgeteilt werden, zum Beispiel nach Anzahl lebender Zellen im äussersten Ring, dann im zweit-äussersten Ring, und so weiter. Um von dieser massiven Parallelisierung Gebrauch machen zu können, würde dann ein leistungsstärkerer Computer mit genügenden Kernen benötigt, der so viele Parallelprozesse abspielen kann.

Ein Ansatz zur tatsächlichen Lösung des Problems wäre eine Analyse, die alle Anfangskonfigurationen findet, welche zur selben Spielklasse gehören. Wenn Gemeinsamkeiten unter diesen Anfangskonfigurationen gefunden werden können, so kann sich daraus allenfalls eine Regel ableiten. 
Dies ist durch meine Ergebnisse in limitiertem Umfang bereits möglich. So weiss ich, dass eine Konfiguration mit weniger als 5 lebenden Zellen sicher kein Gleiter wird. Sobald eine Konfiguration nur noch zwei lebende Zellen hat, gehört diese sicher zu der selbst auslöschenden Spielklasse. Des Weiteren sind statische und oszillierende Objekte meist schon sehr früh symmetrisch.

Systematischer könnte diese Analyse dadurch erreicht werden, dass eine Funktion alle Anfangskonfigurationen mit allen Generationen der jeweils anderen Anfangskonfigurationen abgleicht. Wenn eine Übereinstimmung gefunden wird, kann der Spielverlauf der Anfangskonfiguration besser nachempfunden werden. Folgende Fragen könnten dann beantwortet werden: Welche Konfiguration entsteht aus welcher anderen? Wie viele verschiedene Endkonfigurationen gibt es wirklich? Vielleicht sind es gar nicht so viele wie vermutet, und der Spielverlauf ist besser vorhersehbar als gemeinhin befürchtet? Falls dieser Ansatz zu einem brauchbaren Ergebnis führt, könnte damit auch das zweite Problem angegangen werden. 

Ob diese Ansätze überhaupt zu etwas führen, ist aufgrund der Erkenntnisse, die ich in dieser Arbeit gewonnen habe, nicht bestimmbar. Vielleicht ist die Vorhersage der Lebensentwicklung in "Conway's Game of Life" wirklich nicht oder nur beschränkt möglich. 
Fest steht aber: Das Game of Life ist weitaus komplexer, als auf den ersten Blick gedacht.


