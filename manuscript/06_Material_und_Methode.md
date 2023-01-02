# Material und Methode

Um mich diesen grossen Fragen des «Game of Life» stellen zu können, programmierte ich als Erstes das einfache Grundkonzept des Spieles. Danach konzentrierte ich mich auf die Programmierung einer Simulation, die auf einem beliebig grossen Spielfeld alle möglichen und unterschiedlichen Konfiguration durchspielen sollte. Da ich mich lediglich in Python, auch wenn nur dürftig, auskannte, wählte ich diese Programmiersprache für meine Arbeit. 
Mein Vater spielte eine grosse Rolle bei anfälligen Fragen oder als Anlaufstelle bei Unsicherheiten und Problemen. 

## Das Grundkonzept

Das Programmieren des Gameboards und der Spielfunktion stellte sich im Nachhinein als die kleinste aller Herausforderungen heraus. Dennoch beanspruchte dies viel Zeit, da ich eine Anfängerin im Programmieren war.   


### Das Gameboard

Das Gameboard erinnert an ein Schachbrett und wird durch eine binäre Matrix dargestellt. Die Zellen mit Nullen symbolisieren die toten Zellen und sind somit leer, die Zellen mit Einsen die lebenden und sind schwarz ausgefüllt. Somit sieht ein Gameboard mit einer einzelnen lebenden Zelle und der Grösse 5x5 wie folgt aus:


{width: "16.666666667%"}
![Abb. 7: Beispielsgameboard](example_gb.png)  


### Play

Als Nächstes machte ich mich an die Spielfunktion. Jede Zelle hat einen Index [Reihe, Spalte], ähnlich wie in einem Koordinatensystem. Die Nummerierung fängt bei null an da sie Computerbasiert ist. In der Informatik gilt null gleich "False" und eins gleich "True". Eine Zelle muss also mit "True" gleichgesetzt werden, um als lebend zu gelten:


1. Zelle[2,1] = True
2. Zelle[3,2] = True
3. Zelle[4,0] = True


{width: "30%"}
![Abb. 8: Beispiel lebendige Zellen](example_alive_gb.png)  


Um eine Konfiguration nun durchspielen zu können, muss der Status der Nachbarzellen bekannt sein. Diesen finde ich durch einen Kernel heraus. 

{caption: "Kernel"}
```
[1, 1, 1]
[1, 0, 1]
[1, 1, 1]
```
Für jede Zelle wird dieser Kernel darüber gelegt, sodass das null auf der besagten Zelle liegt. Nun werden alle Zellen, auf denen eine Eins liegt, überprüft und zusammengezählt. Eine tote Zelle hat den Wert Null und eine lebende den Wert Eins. Sobald die Summe der Nachbarzellen nun bekannt ist, muss nur noch den Regeln gefolgt werden um den Status besagter Zelle für die nächste Generation herauszufinden.   
 

### Randzellen

Ein Problem stellen die Ränder dar. Eine Zelle am Rand hat nur fünf existente Nachbarn. Eine Eckzelle sogar nur drei. 

Zuerst löste ich das Problem mit der sogenannten Kachelstrategie. Dabei werden die Gameboards auf allen acht Seiten (N, NE, E, SE, S, SW, W, NW) wiederholt. Beispielsweise hat die oberste Zelle links als linken (West-) Nachbarn die oberste Zelle rechts und umgekehrt.

Mit dem Hinblick auf die Simulation die ich später erstellen würde, ist diese Lösung allerdings nicht die beste. Für die Simulation ist es nämlich wichtig, dass dieselben Bedingungen wie auf einem endlosen Spielbrett herrschen, da sonst die folgende Generation verfälscht werden könnte. Also schrieb ich eine Funktion, die jedes Mal, wenn eine Zelle am Rand des Gameboards ankommt, dieses um eine Reihe oder Spalte, je nach Fall, vergrössert. Somit ist sichergestellt, dass jede Zelle immer acht echte Nachbarn hat.
Zur Veranschaulichung nehmen wir folgendes Gameboard:


{width: "16.666667%"}
![Abb. 9: Grenzfälle Nachbarn](corner_case_gb.png)  

Bevor das Spielbrett nun abgespielt wird, beziehungsweise die nächste Generation errechnet würde, kommt auf jeder Seite eine Reihe oder Spalte hinzu. Das Gameboard besitzt also nicht mehr die Grössenverhältnisse 5x5, sondern 7x7:


{width: "21%"}
![Abb. 10: Expandiertes Gameboard](expanded_gb.png)  

Die Zellen sterben durch diese Funktion also bereits nach einer Generation aus. Für sie gelten nun dieselben Bedingungen wie für Zellen eines endlos grossen Spielfelds. 

 ## Die Simulation

Die Simulation ist der Schlüssel zur Beantwortung der Fragestellungen. 
Wenn alle möglichen Konfigurationen eines Spielfelds einmal durchgespielt wurden, sind auch all deren Endzustände bekannt. Wenn nun also irgendeine Konfiguration auf diesem begrenzten Spielfeld abgefragt wird, kann ich den Endzustand sozusagen "hervorsagen", bevor diese erneut durchgespielt wird. 

Zudem sind mir die einzelnen Generationen jeder Konfiguration dieses Spielfeldes bekannt. Um herauszufinden, ob eine Konfiguration aus der anderen entstehen kann, muss diese also nur mit den abgespeicherten Generationen der zu vergleichenden Konfiguration abgeglichen werden. Wenn sie mit einer übereinstimmt, ist die Antwort klar. 

### Endzustand

Als Erstes legte ich fest, nach welchen möglichen Endzuständen ich unterscheiden will. Ich entschied mich für die vier bekanntesten und nicht allzu seltenen Objekten:

1. Selbst auslöschende Objekte
1. Statische Objekte
1. Oszillierende Objekte
1. Gleitende Objekte
   


Zudem brauchte es noch eine weitere Objektgruppe, falls es sich um keines der obigen Objekte handelt, wie beispielsweise eine Gleiterkanone. Also fügte ich eine fünfte Möglichkeit hinzu:

1. Überlebende Objekte

Für jede Generation der Anfangskonfiguration muss nach jedem dieser Objekte geprüft werden. Sobald eines übereinstimmt, bricht das Spiel ab.

#### Selbst auslöschende Objekte (Erased)

Diese Objekte sind sichtlich einfach erkennbar. Eine Funktion prüft, ob in dem aktuellen Spielbrett lebende Zellen vorhanden sind. Falls nicht, zählt die Startkonfiguration zu den selbst auslöschenden Objekten. Falls lebende Zellen vorhanden sind, muss weiter geprüft werden. 

#### Statische Objekte (Stable)

Auch diese Objekte stellen kein Problem dar. Jede Konfiguration der vorherigen Generationen wird abgespeichert. Das letzte Objekt dieser Liste ist die Muttergeneration der aktuellen Konfiguration. Wenn diese beiden identisch sind, ist das Objekt statisch. Falls nicht, muss weiter geprüft werden.

#### Oszillierende Objekte (Oscillator)

Oszillatoren zeichnen sich dadurch aus, dass sie nach einer bestimmten Periode wieder dieselbe Konfiguration darstellen. Die aktuelle Generation muss nun also mit allen vorherigen Generation abgeglichen werden. Wenn keine Übereinstimmung vorhanden ist, muss weiter geprüft werden.

#### Gleitende Objekte (Spaceship)

Diese Objekte sind etwas schwieriger zum Herausfiltern. Die einzelnen Generationen sehen zwar gleich aus, haben aber unterschiedliche Positionen. Es muss also eine Kopie des relativen Gameboards aller Generationen seit der Anfangskonfiguration bis zur jetzigen Generation erstellt und abgespeichert werden.

Für das relative Gameboard müssen zuerst die leeren Spalten und Reihen bis zu den ersten lebenden Zellen herausgefunden werden. Damit nicht auch tote Zellen zwischen zwei lebendigen Zellen abgeschnitten werden, müssen die überflüssigen Reihen und Spalten von jeder Seite einzeln gezählt werden. Sobald diese Zahlen bekannt sind, kann bis zum Index der ersten lebenden Zelle abgeschnitten werden. 

![Abb. 11: Relatives Gameboard von Gleiter](relative_gb.png)  

Diese relativen Gameboards werden nun nach dem Schema der Oszillatoren abgeglichen und falls eine Affinität besteht, gilt diese Konfiguration als gleitendes Objekt.

#### Überlebende Objekte (Survival)

Falls die Konfiguration bis jetzt nicht herausgefiltert wurde, gilt es als überlebendes Objekt. Damit diese nun nicht endlos weiterlaufen, baue ich einen Grenzwert ein. Dieser impliziert zwar eine Fehlerquote für Konfiguration, die Objekte darstellen, diese aber erst nach dem vorgegebenen Grenzwert erreichen. Würde dieser Grenzwert aber weggelassen werden, würde die Simulation endlos lange dauern. Wenn nach dem Erreichen dieses Wertes die Konfiguration also immer noch keinem Objekt entspricht, bricht die Simulation ab und die Konfiguration gilt als überlebend. Den Grenzwert wählte ich bei 100.

### Speicherform des Spielbrettes 

Um diese simulierten Konfigurationen und deren Endzustände abzuspeichern, müssen die Spielbretter in eine andere Form gebracht werden. Wenn sie bei einem herkömmlichen Spielfeld belassen werden würden, würde viel zu viel Speicherplatz benötigt werden. Also will ich das Spielbrett in eine Zahl verwandeln. Zuerst kommt die Grösse des Spielfelds, dann die Position der Konfiguration auf dem Spielfeld. Darauf folgt die eigentliche Grösse der Konfiguration, die Anzahl an toten Zellen bis zur ersten lebendigen Zelle und schlussendlich noch die Zahl des Spielbrettes. 

Die Zahl des Spielbrettes ergibt sich aus dem Gameboard als binäre Zahl, die Nullen stellen die toten Zellen und die Einsen die lebendigen dar. Diese Zahl wird in eine hexadezimale Zahl umgewandelt, um weiteren Speicherplatz zu sparen. Somit erhält jedes Gameboard eine individuelle Nummer. Das folgende Spielbrett sieht dann also wie folgt aus:



{width: "65%"}
![Abb. 12: Gameboard als Zahl](gb_number_explained.png)  


### Zähler

Diese soeben erklärte Methode verwende ich ähnlich um die einzelnen zu simulierenden Anfangskonfigurationen zu generieren. Ein Zähler zählt jedes Mal, wenn eine neue Anfangskonfiguration in die Simulation gegeben wird, herauf. Einzig die höchste Zahl muss bekannt sein, also wie viele verschiedene Konfigurationen auf diesem Spielfeld generiert werden können. Da hier eine Wahrscheinlichkeit mit zwei möglichen Ausgängen besteht, muss jeweils `2^{Anzahl Zellen}`$ gerechnet werden. Bei einem 5x5 Spielfeld würden alle Möglichkeiten zusammen also `2^{5\cdot5} = 33'554'432`$ ergeben. Nun zählt der Zähler hoch, bis diese Zahl erreicht wird. Jede Zahl wird zuerst in eine binäre Zahl umgewandelt. Diese wird nun mit dem leeren Spielfeld als binäre Zahl verglichen und von vorne aufgefüllt, bis sie auf die gleiche Länge kommen. Da die Länge und Breite des Spielbrettes bekannt sind, kann nun aus dieser binären Zahl einfach ein Spielbrett mit der gewünschten Konfiguration erstellt werden. 

TODO Zahlen entfernen an linkem Rand bei Leanpub
{title: "Dezimalzahl als Spielbrett", id: decimale_gb}
```text
Zahl:  Binärzahl:  Zellen:    Aufgefüllte Zahl:    Gameboard:
                                                   [False False False False False]
                                0000000000000      [False False False False False]
123     1111011    5*5 = 25     000001111011       [False False False False False]
                                                   [False False False  True  True]
                                                   [True  True  False  True  True]
          
```
### Aussortieren

Durch das Generieren der Anfangskonfigurationen durch den dezimalen Zähler entsteht das Problem, dass jede Konfiguration viel zu oft abgespielt wird. 
Zum einen, wenn sie an einer anderen Position vorkommen, eigentlich aber identisch sind. Dieses Problem ist relativ einfach zu lösen. In der Simulation werden immer nur Anfangskonfigurationen abgespielt, die den vorgegebenen Massen entsprechen. Also, wenn ich eine Simulation mit der vorgegebenen Grösse 5x5 starte, wird eine Anfangskonfiguration mit der relativen Grösse von 3x3 nicht abgespielt. So sind schon einmal die ersten Doppelgänger aussortiert. Ausserdem werden alle Anfangskonfigurationen in einem Set gespeichert. Jede neue Anfangskonfiguration wird mit allen vorherigen abgeglichen und falls eine Affinität gefunden wird, abgebrochen. Somit werden keine Konfigurationen, die als einzigen Unterschied eine unterschiedliche Position auf dem Spielfeld haben, mehr als einmal abgespielt. 

Trotz diesem Filter wird jede Anfangskonfiguration immer noch siebenmal zu oft abgespielt. Zur Veranschaulichung ein Beispiel. Die folgenden Konfigurationen sind eigentlich dieselben, nur entweder gedreht oder gespiegelt, deren dazugehörigen Dezimalzahlen allerdings komplett unterschiedlich:

{width: "70%"}
![Abb. 13: Identische Gameboards](identical_gbs.png)  

Um zu vermeiden, dass all diese abgespielt und gespeichert werden, muss also sowohl jede Anfangskonfiguration, als auch deren gespiegelten und gedrehten Variationen mit den bereits abgespielten Anfangskonfigurationen abgeglichen werden. Somit wird jede Konfiguration wirklich nur einmal abgespielt.

### Abspeichern

Alles, was ich abspeichern will, speichere ich in ein CSV-File. Dieses Format eignet sich besonders gut, da es einfach in eine Exceltabelle transformiert werden kann. Für das erste Problem, das Vorhersagen des Endzustandes, würde das Abspeichern jeder einzelnen Generation einer Konfiguration zu viel Speicherplatz brauchen. Deshalb werden diese hier auf die Anzahl an Generationen beschränkt. Die Anfangs- und Endlänge beziehungsweise -breite, die Anfangs- und Endkonfiguration und die Definition des Objektes werden auch abgespeichert. Zudem noch die Periodizität, falls es sich um ein oszillierendes oder gleitendes Objekt handelt. 

Für das zweite Problem, der Vergleich zweier Konfigurationen, werden alle Generationen jeder Konfiguration abgespeichert. Ansonsten wird nichts benötigt.




                                                                                      
                                                                                      
                                                                               
                                                                                                                                                                