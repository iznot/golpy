# Material und Methode

Um mich diesen grossen Fragen des «Game of Life» stellen zu können, programmiere ich als erstes das einfache Grundkonzept des Spieles. Danach konzentriere ich mich auf die Programmierung einer Simulation, die für mich schlussendlich auf einem beliebig grossen Spielfeld alle möglichen Konfiguration durchspielen soll. 

## Das Grundkonzept

Während dem Programmieren des Grundkonzeptes filterten sich mehrere Probleme heraus. Als Programmieranfängerin war das ganze natürlich noch schwieriger. Ich entschied mich dazu, das Programm in Python zu schreiben, da dies die einzige Programmiersprache war, die ich ein bisschen kannte. Mein Vater spielte bei diesem Prozess eine grosse Rolle bei anfälligen Fragen und als Anlaufstelle bei Unsicherheiten oder Problemen. 

### Das Gameboard

Das Gameboard ist ein numpy Array bestehend aus Booleans. Die Reihen sind auf der Achse mit dem Index 0 und die Kollonen auf der mit dem Index 1. Die Kollonen werden durch Bindestriche ('---') und die Reihen durch Trennstriche ('|') dargestellt. Zusammen bilden sie eine Zelle. Somit sieht ein Gameboard mit der Grösse 5x5 wie folgt aus:


{title: "Leeres Gameboard", id: gb-leer}

```text
 --- --- --- --- --- 
|   |   |   |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
 ```

### Play

Als nächstes machte ich mich an die Spielfunktion. Jede Zelle hat einen Index[Reihe, Kollone], ähnlich wie in einem Koordinatensystem. Wenn dieser mit 'True' gleichgesetzt wird, ist die Zelle am leben:

1. Zelle[2,1] = True
1. Zelle[3,2] = True
1. Zelle[4,0] = True

{title: "Beispiel lebendige Zellen", id: gb-1}
```text
 --- --- --- --- --- 
|   |   |   |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
|   | o |   |   |   |
 --- --- --- --- ---
|   |   | o |   |   |
 --- --- --- --- ---
| o |   |   |   |   |
 --- --- --- --- ---
 ```

Um eine Konfiguration durchspielen zu können, muss der Status der Nachbarszellen bekannt sein. Zuerst iteriere ich also durch das Spielfeld, um alle lebendigen Zellen herauszufinden. Als nächstes marschiere ich um jede lebendige Zelle herum und zähle, wie viele der Nachbarszellen lebendig sind. Nun muss nur noch den bereits bekannten Regeln gefolgt werden und ein neues Gameboard ausgedruckt werden. 

 

### Grenzfälle

Ein Problem stellen die Grenzfälle dar. Eine Zelle am Rand hat nur fünf existente Nachbarn und eine in einem Ecken sogar nur drei. Zuerst löste ich das Problem damit, dass die oberste linkste Zelle die oberste rechteste Zelle als direkten linken Nachbarn hat und umgekehrt. Als direkten oberen Nachbarn hat sie die unterste linkste Zelle und als schräg-oberen, rechten Nachbarn die rechte unterste. Eine Zelle am linken Rand hat die Zelle am rechten Rand in der gleichen Reihe als direkten Nachbarn, eine Zelle am oberem Rand hat die Zelle in der selben Kollone am unteren Rand als Nachbarn und so weiter. Die folgenden Zellen sind also alle Nachbarn:

{title: "Grenzfälle Nachbarn", id: unexpanded_gb}
```text
Anfangskonfiguration:    1.Generation:
 --- --- --- --- ---     --- --- --- --- ---
| o |   |   |   | o |   | o |   |   |   | o |
 --- --- --- --- ---     --- --- --- --- ---
|   |   |   |   |   |   |   |   |   |   |   |
 --- --- --- --- ---     --- --- --- --- ---
|   |   |   |   |   |   |   |   |   |   |   |
 --- --- --- --- ---     --- --- --- --- ---
|   |   |   |   |   |   |   |   |   |   |   |
 --- --- --- --- ---     --- --- --- --- ---
| o |   |   |   | o |   | o |   |   |   | o |
 --- --- --- --- ---     --- --- --- --- ---
 ```

Da durch diese Funktion jede dieser Zellen nun drei Nachbarn hat, keine tote Zelle aber genau drei Nachbarn, ist dies ein statisches Objekt und bleibt am Leben.

Mit dem Hinblick auf die Simulation die ich später erstellen würde, ist diese Lösung nicht die beste. Für diese ist es nämlich wichtig, dass die selben Bedinungen wie auf einem endlosen Spielbrett herrschen, da sonst die folgende Generation verfälscht werden könnte. Also schrieb ich eine Funktion, die jedesmal, wenn eine Zelle am Rand des Gameboardes ankommt, dieses um eine Reihe oder Kollone, je nach Fall, vergrössert. Somit ist sichergestellt, dass jede Zelle immer acht echte Nachbarn hat.
Das vorherige Gameboard würde dann also, trotz einer vorgegebenen Grösse von 5x5 wie folgt aussehen:

{title: "Grenzfälle Nachbarn mit expand", id:expanded_gb}
```text
Anfangskonfiguration:            1. Generation:
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   | o |   |   |   | o |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   | o |   |   |   | o |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |    |   |   |   |   |   |   |   |
 --- --- --- --- --- --- ---      --- --- --- --- --- --- ---
 ```

 Die Zellen sterben durch diese Funktion also bereits nach einer Generation aus. Für sie gelten nun die selben
 Bedingungen wie für Zellen eines endlos grossen Spielfelds. 

 ## Die Simulation

Die Simulation ist der Schlüssel zur Beantwortung der Fragenstellung. 
Wenn alle möglichen Konfigurationen eines Spielfelds einmal durchgespielt wurden, sind auch all deren Endzustände bekannt. Wenn nun also irgendeine Konfiguration auf diesem begrenzten Spielfeld abgefragt wird, kann ich den Endzustand sozusagen "hervorsagen", bevor diese erneut durchgespielt wird. 
Zudem sind mir die einzelnen Generationen jeder Konfiguration dieses Spielfeldes bekannt. Um herauszufinden, ob eine Konfiguration aus der anderen entstehen kann, muss diese also nur mit den abgespeicherten Generation der zu vergleichenden Konfiguration abgeglichen werden. Wenn sie mit einer übereinstimmt, ist die Antwort klar. 

### Endzustand

Als erstes legte ich fest, nach welchen möglichen Endzuständen ich unterscheiden will. Ich entschied mich für die vier bekanntesten und nicht all zu seltenen Objekte:

1. Selbstauslöschende Objekte
1. Statische Objekte
1. Oszillierende Objekte
1. Gleitende Objekte

Zudem braucht es noch eine Fehlerbehebung, falls es sich um ein anderes Objekt handelt, wie zum Beispiel eine Gleiterkanone. Also fügte ich eine fünfte Möglichkeit hinzu:

5. Überlebende Objekte

Für jede Generation der Konfiguration, muss nach jedem dieser Objekte geprüft werden. Sobald einer stimmt, bricht das Spiel ab.

#### Selbstauslöschende Objekte (Erased)

Diese Objekte herauszufinden, ist sichtlich einfach. Eine Funktion prüft, ob in dem aktuellen Spielbrett lebende Zellen vorhanden sind. Falls nicht, zählt die Startkonfiguration zu den selbstauslöschenden Objekten. Falls lebende Zellen vorhanden sind, muss weiter geprüft werden. 

#### Statische Objekte (Stable)

Auch diese Objekte stellen kein Problem dar. Jede Konfiguration der vorherigen Generationen wird abgespeichert. Das letzte Objekt dieser Liste ist die Muttergeneration der aktuellen Konfiguration. Wenn diese beiden identisch sind, ist das Objekt statisch. Falls nicht, muss weiter geprüft werden.

#### Oszilierende Objekte (Oscillator)

Oszillatoren zeichnen sich dadurch aus, dass sie nach einer bestimmten Periode wieder die selbe Konfiguration darstellen. Die aktuelle Generation muss nun also mit allen vorherigen Generation abgeglichen werden. Wenn keine Übereinstimmung vorhanden ist, muss weiter geprüft werden.

#### Gleitende Objekte (Spaceship)

Diese Objekte sind etwas schwieriger zum herausfiltern. Die einzelnen Generationen sehen zwar gleich aus, haben aber unterschieldiche Positionen. Es muss also eine Kopie aller vorherigen Generation und der aktullen Generation mit deren relativen Positionen gespeichert werden. 

Für das relative Spielfeld müssen zuerst die leeren Kollonen und Reihen bis zu den ersten lebenden Zellen herausgefunden werden. Damit nicht auch tote Zellen zwische zwei lebendigen Zellen abgeschnitten werden, müssen die überflüssigen Reihen und Kollonen von jeder Seite einzeln gezählt werden. Sobald diese Zahlen bekannt sind, kann bis zum Index der ersten lebenden Zelle abgeschnitten werden. 

Diese relativen Spielfelder werden nun nach dem Schema der Oszillatoren abgeglichen und falls eine Affinität besteht, gilt diese Konfiguration als gleitendes Objekt.

#### Überlebende Objekte (Survival)
Falls die Konfiguration keiner der oben genannten Objekten entspricht, ist es laut meiner Definition ein überlebendes Objekt. Damit diese nun nicht endlos weiterlaufen, baue ich einen Grenzwert ein. Dieser impliziert zwar eine Fehlerquote für Konfiguration, die zwar Objekte darstellen, diese aber erst nach dem vorgegebenen Grenzwert erreichen. Würde dieser Grenzwert aber weggelassen werden, würde die Simulation endlos lange dauern. Wenn nach dem Erreichen dieses Wertes die Konfiguration also immer noch keinem Objekt entspricht, bricht die Simulation ab und die Konfiguration gilt als überlebend. 

### Speicherform des Spielbrettes 
Um diese simulierten Konfigurationen und deren Endzustände abzuspeichern, müssen die Spielbretter in eine andere Form gebracht werden. Wenn sie bei einem herkömlichen Spielfeld belassen werden würden, würde viel zu viel Speicherplatz benötigt werden. Also will ich das Spielbrett in eine Zahl verwandeln. Zuerst kommt die grösse des Spielfelds, dann die Postition der Konfiguration auf dem Spielfeld. Darauf folgt die eigentliche grösse der Konfiguration, die Anzahl an toten Zellen bis zur ersten lebendigen Zelle und schlussendlich noch die Zahl des Spielbrettes. 
Die Zahl des Spielbrettes ergibt sich aus dem Spielfeld als binäre Zahl, die Nullen stellen die toten Zellen und die Einsen die lebendigen dar. Diese Zahl wird in eine hexadimensionale Zahl umgewandelt um weiteren Speicherplatz zu sparen. Das folgende Spielbrett sieht dann also wie folgt aus:


{title: "Gameboard als Zahl", id:numbre_gb}
```text
Spielbrett:                     Zahl:
 --- --- --- --- ---  
|   |   |   |   |   | 
 --- --- --- --- ---  
|   |   |   |   | o | 
 --- --- --- --- ---  
|   |   |   |   | o |        (5, 5):(1, 2)|(3, 3):2:0x4e
 --- --- --- --- --- 
|   |   | o | o |   |
 --- --- --- --- --- 
|   |   |   |   |   |
 --- --- --- --- --- 
```

### Zähler
Diese soeben erklärte Methode verwende ich ähnlich um die einzelnen zu simulierenden Konfigurationen zu generieren. Ein Zähler zählt jedes mal, wenn eine neue Anfangskonfiguration in die Simulation gegeben wird, herauf. Einzig die höchste Zahl muss bekannt sein, also wie viele verschiedene Konfigurationen auf diesem Spielfeld generiert werden können. Da hier eine Wahrscheinlichkeit mit zwei möglichen Ausgängen besteht, muss jeweil 2^(Anazahl Zellen) gerechnet werden. Bei einem 5x5 Spielfeld würden alle Möglichkeiten zusammen also 2^(5*5)=33'554'432 ergeben. Nun zählt der Zähler bis zum erreichen dieser Zahl hoch. Jede Zahl wird nun zuerst in eine binäre Zahl umgewandelt. Diese wird nun mit dem leeren Spielfeld als binäre Zahl verglichen und von vorne aufgefüllt, bis sie auf die gleiche Länge kommen. Da die Länge und Breite des Spielbrettes bekannt sind, kann nun aus dieser binären Zahl einfach ein Spielbrett mit der gewünschten Konfiguration erstellt werden. 

{title: "Dezimalzahl als Spielbrett", id: decimale_gb}
```text
Zahl:  Binärzahl:  Zellen:    Aufgefüllte Zahl:    Gameboard:
                                                   [False False False False False]
                                0000000000000      [False False False False False]
 1         1       5*5 = 25     000000000001       [False False False False False]
                                                   [False False False False False]
                                                   [False False False False  True]
          
```

### Abspeichern
Alles was ich abspeichern will, speichere ich in ein CSV-File. Dieses Format eignet sich besonders gut, da es einfach in eine Exceltabelle transformiert werden kann. Für das erste Problem, das vorhersagen des Endzustandes, würde das Abspeichern jeder einzelnen Generationn einer Konfiguration zu viel Speicherplatz brauchen. Deshalb werden diese hier auf die Anzahl an Generationen beschränkt. Die Anfangs- und Endslänge beziehnugsweise Breite, die Anfangs und Endskonfiguration und die Definition des Objektes werden auch abgespeichert. Zudem noch die Periodizität, falls es sich um ein oszillierendes oder gleitendes Objekt handelt. 

Für das zweite Problem, der Vergleich zweier Konfigurationen, werden alle Generationen jeder Konfiguration abgespeichert. Ansonsten wird nichts benötigt.




                                                                                      
                                                                                      
                                                                               
                                                                                                                                                                