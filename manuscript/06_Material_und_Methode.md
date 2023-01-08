# Material und Methode

Um mich diesen grossen Fragen des "Game of Life" widmen zu können, programmierte ich als Erstes das einfache Grundkonzept des Spieles. Danach konzentrierte ich mich auf die Programmierung einer Simulation, die auf einem beliebig grossen Spielfeld alle möglichen und unterschiedlichen Konfiguration durchspielen sollte. Da ich mich lediglich in Python, (wenn auch nur dürftig), auskannte, wählte ich diese Programmiersprache für meine Arbeit. 
Mein Vater spielte eine grosse Rolle bei allfälligen Fragen oder als Anlaufstelle bei Unsicherheiten und Problemen. 

## Das Grundkonzept

Das Programmieren des Gameboards und der Spielfunktion stellte sich im Nachhinein als die kleinste aller Herausforderungen heraus. Dennoch beanspruchte dies viel Zeit, da ich eine Anfängerin im Programmieren war.   


### Das Gameboard

Das Gameboard erinnert an ein Schachbrett - wobei es keine schwarzen und weissen Felder gibt, sondern nur quadratische Häuschen. Im Programmiercode wird das Gameboard durch eine Matrix dargestellt. 

### Die Konfiguration

Die Konfiguration setzt sozusagen die lebenden Zellen auf das Gameboard. Dies wird mit einer binären Matrix programmiert. Die Zellen mit Nullen symbolisieren die toten Zellen und sind somit leer, die Zellen mit Einsen die lebenden. Diese werden schwarz ausgefüllt dargestellt. Somit sieht ein Gameboard mit einer einzelnen lebenden Zelle und der Grösse 5x5 wie folgt aus:


{width: "16.666666667%"}
![Abb. 7: Beispielsgameboard](example_gb.png)  

{pagebreak}

### Spielzug (Play)

Als Nächstes machte ich mich an die Spielfunktion. Jede Zelle hat einen Index [Zeile, Spalte], ähnlich wie in einem Koordinatensystem, wobei der Ursprung oben links liegt. Die Nummerierung fängt bei null an (wie in Python üblich). In der Informatik gilt 0 gleich "False" und 1 gleich "True". Eine Zelle muss also mit "True" gleichgesetzt werden, um als lebend zu gelten:


1. Zelle[2,1] = True
2. Zelle[3,2] = True
3. Zelle[4,0] = True


{width: "30%"}
![Abb. 8: Beispiel lebendige Zellen](example_alive.png)  


Um eine Konfiguration nun durchspielen zu können, muss der Status der Nachbarzellen bekannt sein. Diesen finde ich durch folgenden Kernel heraus:

{id: kernel}
```text
[1, 1, 1]
[1, 0, 1]
[1, 1, 1]
```
Für jede Zelle wird dieser Kernel darüber gelegt, sodass die Null auf der besagten Zelle liegt. Nun werden alle Zellen, auf denen im Kernel eine Eins liegt, überprüft und zusammengezählt. Eine tote Zelle hat den Wert Null und eine lebende den Wert Eins. Sobald die Summe der Nachbarzellen nun bekannt ist, muss nur noch den Regeln gemäss der Status besagter Zelle der nächsten Generation ermittel werden.   
 
Diese Kernel-Funktion wird in Python in der Bibliothek `scipy` durch die Funktion `convolve` zur Verfügung gestellt.

{#randzellen}
### Randzellen

Ein Problem stellen die Ränder dar. Eine Zelle am Rand hat nur fünf existente Nachbarn. Eine Eckzelle sogar nur drei. 

Zuerst löste ich das Problem mit der sogenannten Kachelstrategie. Dabei werden die Gameboards auf allen acht Seiten (N, NE, E, SE, S, SW, W, NW) wiederholt. Beispielsweise hat die oberste Zelle links als linken (West-) Nachbarn die oberste Zelle rechts und umgekehrt.

Mit dem Hinblick auf die Simulation, die ich später erstellen würde, ist diese Lösung allerdings nicht die beste. Für die Simulation ist es nämlich wichtig, dass dieselben Bedingungen wie auf einem endlosen Spielbrett herrschen, da sonst die folgende Generation verfälscht werden könnte. Also schrieb ich eine Funktion, die jedes Mal, wenn eine Zelle am Rand des Gameboards ankommt, dieses um eine leere Zeile oder Spalte, je nach Fall, vergrössert. Somit ist sichergestellt, dass jede Zelle immer acht echte Nachbarn hat.
Zur Veranschaulichung nehmen wir folgendes Gameboard:


{width: "16.666667%"}
![Abb. 9: Grenzfälle Nachbarn](corner_case_gb.png)  

Bevor der nächste Spielzug errechnet wird, kommt auf jeder der vier Hauptseiten eine leere Zeile oder Spalte hinzu. Das Gameboard besitzt also nicht mehr die Grössenverhältnisse 5x5, sondern 7x7:


{width: "21%"}
![Abb. 10: Expandiertes Gameboard](expanded_gb.png)  

Die Zellen sterben durch diese Funktion also bereits nach einer Generation aus. Für sie gelten nun dieselben Bedingungen wie für Zellen eines endlos grossen Spielfelds. 

## Spiel und Simulation

Ich versuchte, mich den Problemen auf zwei verschiedene Arten zu nähern. 

Zum einen tat ich dies durch zwei Funktionen. Die erste spielt die gegebene Konfiguration durch und ordnet diesem Spiel eine Spielklasse zu, nähert sich also dem ersten Problem. Die zweite Funktion hat als Input eine zu testende und eine zu vergleichende Konfiguration. Sie spielt die zu vergleichende Konfiguration durch und gleicht deren Generationen auf Affinität mit der zu testenden Konfiguration ab. Diese nähert sich also dem zweiten Problem.

Der zweite Ansatzpunkt war eine Simulation. Ich programmierte eine Simulation, die alle möglichen Konfigurationen auf einem begrenzten Spielfeld durchspielte, deren Spielklasse zuordnete und abspeicherte. Dadurch war es mir möglich, die einzelnen Spiele zu analysieren und nach Auffälligkeiten zu suchen.   


### Spielklassen

Als Erstes legte ich fest, nach welchen möglichen Spielklassen ich unterscheiden will. Dies war für die Funktion des ersten Problems und die Simulation notwendig. Ich entschied mich für die vier bekanntesten und nicht allzu seltenen Spielklassen, plus eine fünfte, die alle restlichen Fälle enthält:

1. Selbst auslöschende Objekte
2. Statische Objekte
3. Oszillierende Objekte
4. Gleitende Objekte
5. Überlebende Objekte

Die letzte Spielklasse, "Überlebende Objekte", schliesst interessante Objekte wie beispielsweise eine Gleiterkanone mit ein. 

Für jede Generation des Spiels auf eine bestimmte Anfangskonfiguration muss überprüft werden, ob das Spiel einer dieser Spielklassen angehört. Sobald Spielklassen 1 - 4 identifiziert wurden, bricht das Spiel ab, und die Endkonfiguration wird festgehalten. 

#### Selbst auslöschende Objekte (Extinct)

Diese Objekte sind sichtlich einfach erkennbar. Eine Funktion prüft, ob im aktuellen Spielbrett lebende Zellen vorhanden sind. Falls nicht, zählt die Startkonfiguration zu den selbst auslöschenden Objekten. Falls lebende Zellen vorhanden sind, muss weiter geprüft werden. 

#### Statische Objekte (Stable)

Auch diese Objekte stellen kein Problem dar. Jede Konfiguration der vorherigen Generationen wird abgespeichert. Das letzte Objekt dieser Liste ist die Muttergeneration der aktuellen Konfiguration. Wenn diese beiden identisch sind, ist das Objekt statisch. Falls nicht, muss weiter geprüft werden.

#### Oszillierende Objekte (Oscillator)

Oszillatoren zeichnen sich dadurch aus, dass sie nach einer bestimmten Periode wieder dieselbe Konfiguration darstellen. Die aktuelle Generation muss nun also mit allen vorherigen Generationen abgeglichen werden. Wenn keine Übereinstimmung vorhanden ist, handelt es sich (noch) nicht um ein oszillierendes Objekt.

Ein Problem, das sich mir dabei stellte, war, dass ein oszillierendes Objekt grösser und dann wieder kleiner werden kann. Es kann also notwendig sein, das Gameboard zu erweitern, wie oben im Abschnitt [(Randzellen)](#randzellen) beschrieben. Um jedoch zwei Generationen in einem Spiel vergleichen zu können, musste ich beim Zusammenziehen eines Objektes das Gameboard wieder auf die Grundform reduzieren.

#### Gleitende Objekte (Spaceship)

Durch die Reduktion auf die Grundform, die für oszillierende Objekte notwendig ist, ist es nicht einfach, die gleitenden Objekte von oszillierenden Objekten zu unterscheiden. Durch das Vereinfachen einer Konfiguration auf die Grundkonfiguration geht bei einem gleitenden Objekt die relative Position auf dem Gameboard verloren. Um dieses Problem zu lösen, musste ich zusätzlich zur Konfiguration noch die relative Position jeder Generation in einem Spiel speichern und vergleichen. Bleibt die relative Position über Generationen hinweg gleich, so handelt es sich um ein oszillierendes Objekt. Ändert sich die relative Position, so handelt es sich um ein gleitendes Objekt.

![Abb. 11: Grundkonfiguration des Gleiters](relative_gb.png)  

Diese Grundkonfigurationen werden nun nach dem Schema der Oszillatoren abgeglichen. Falls eine Affinität besteht, gilt diese Konfiguration als gleitendes Objekt.

#### Überlebende Objekte (Survival)

Falls der Objekttyp bis jetzt nicht identifiziert wurde, klassifiziere ich ein Spiel als überlebend. Damit diese Spiele nun nicht endlos weiterlaufen, baute ich eine maximale Zahl von erlaubten Spielzügen ein. Dieser Maximalwert impliziert eine Fehlerquote für Anfangskonfigurationen, die ein Objekt erst nach dem vorgegebenen Grenzwert erreichen. Würde dieser Grenzwert aber weggelassen werden, so wäre das Spiel endlos lang. Den Grenzwert setzte ich auf 100.

### Speicherform der Konfiguration: Das Golpy-Format 

Um die durch meine Simulation gespielten Spiele später analysieren zu können, musste ich sie in einem File abspeichern. Damit dieses nicht zu gross wird, speicherte ich jeweils nicht alle Generationen, sondern nur die Anfangskonfiguration und den Endzustand ab. Um eine Konfiguration in ein Excel schreiben zu können, muss die Konfiguration in ein Format gebracht werden, das sich dafür eignet. Eine Möglichkeit wäre, jede Konfiguration durch eine Zeile von Nullen und Einsen darzustellen. Dadurch würde jedoch viel zu viel Speicherplatz benötigt werden. Ausserdem wäre noch nicht klar, wie wir beispielsweise ein 4x5 Gameboard von einem 5x4 Gameboard unterscheiden. Also formatierte ich die Konfiguration nach folgendem Format: 

1. Zuerst kommt die Grösse des Gameboards.
2. Dann kommt die relative Position des Objekts auf dem Gameboard. 
3. Darauf folgt die Grösse der Grundkonfiguration.
4. Jetzt kommt die Anzahl an toten Zellen bis zur ersten lebendigen Zelle
5. Schlussendlich kommt noch die "Zahl" des Spielbretts. Die Zahl des Spielbretts ergibt sich aus dem Gameboard als binäre Zahl, die Nullen stellen die toten Zellen und die Einsen die lebendigen dar. Diese Zahl wird in eine hexadezimale Zahl umgewandelt, um weiteren Speicherplatz zu sparen. Somit erhält jedes Objekt eine individuelle Objektzahl im Golpy-Format. 
   
Folgendes Beispiel erläutert dieses Format:

{width: "65%"}
![Abb. 12: Gameboard im Golpy-Format](gb_number_explained.png)  



### Zähler

Eine Variation der soeben erklärten Methode der Objektzahl im Golpy-Format verwende ich auch, um die einzelnen zu simulierenden Anfangskonfigurationen zu generieren. Ein (dezimaler) Zähler zählt in einer `for` Schleife von 0 aufwärts. Einzig die höchste Zahl muss bekannt sein, also wie viele verschiedene Konfigurationen auf diesem Spielfeld maximal generiert werden können. Da es zwei mögliche Ausgänge gibt (lebendig oder tot), liegt die Anzahl von unterschiedlichen Konfigurationen bei `2^{Anzahl Zellen}`$. Bei einem 5x5 Spielfeld gibt es also `2^{5\cdot5} = 33'554'432`$ mögliche Anfangskonfigurationen.

Nun zählt der Zähler hoch, bis diese maximale Zahl erreicht wird. Jede Zahl wird zuerst in eine binäre Zahl umgewandelt. Diese wird nun mit dem leeren Spielfeld als binäre Zahl verglichen und von vorne (von links) mit Nullen aufgefüllt, bis sie auf die gleiche Länge kommen. Da die Länge und Breite des Spielbrettes bekannt sind, kann nun aus dieser binären Zahl einfach ein Spielbrett mit der gewünschten Konfiguration erstellt werden. Folgendes Beispiel veranschaulicht das:


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

Durch das Generieren der Anfangskonfigurationen durch den dezimalen Zähler entsteht das Problem, dass jede Konfiguration viel zu oft abgespielt wird, und zwar aus zwei Gründen:

1. Doppelgänger
2. affine Konfigurationen

#### Aussortieren von Doppelgängern

Das gleiche Objekt kann mehrfach auf einem Gameboard vorkommen, nämlich an einer anderen relativen Position. 

{width: "40%"}
![Abb. 13: Doppelgänger](Doppelganger_gb.png)  

Dieses Problem ist relativ einfach zu lösen. In der Simulation werden immer nur Anfangskonfigurationen abgespielt, die der vorgegebenen Zielgrösse eines Gameboards *genau* entsprechen. Wenn ich also eine Simulation mit der vorgegebenen Grösse 5x5 starte, wird eine Anfangskonfiguration mit der relativen Grösse von 3x3 gar nicht abgespielt. So sind alle 3x3 Doppelgänger aussortiert. Wird dann die 3x3 Simulation durchgespielt, so gibt es keine 3x3-Doppelgänger mehr.


#### Aussortieren von affinen Konfigurationen

Jede Konfiguration wird trotzdem noch bis zu siebenmal zu oft abgespielt, da Konfigurationen entweder durch Spiegelung, Drehung oder beides, noch nicht als gleich erkennt werden können.

{width: "70%"}
![Abb. 14: Affine Gameboards mit Zähler](identical_gbs.png)  

Diese will ich ebenfalls nicht mehrfach spielen, da ich an *unterschiedlichen* Konfigurationen interessiert bin. Ich nenne diese Konfigurationen *affine Konfigurationen*. Siehe [Glossar](#glossar).

Um zu vermeiden, dass all diese affinen Konfigurationen abgespielt und gespeichert werden, muss also jeweils die Grundkonfiguration der Anfangskonfiguration und ihre gespiegelten und gedrehten Variationen mit den bereits in einem Set gespeicherten, nicht-affinen Anfangskonfigurationen abgeglichen werden. Falls keine Affinität gefunden wird, wird diese Anfangskonfiguration auch abgespeichert, ansonsten wird das Spiel nicht durchgeführt.  


### Abspeichern

Ich speichere alle Spiele in ein CSV-File. [^footnote-2] Dieses Text-Format eignet sich besonders gut, da es sich einfach in eine Tabelle transformieren und in Excel importieren lässt. Weiter analysiert habe ich die Resultate auf Power BI, da die Datenmenge für Excel zu gross war. 

Das Abspeichern aller Generationen einer Konfiguration würde zu viel Speicherplatz brauchen. Deshalb werden diese hier auf die Anzahl an Generationen beschränkt. Die Anfangs- und Endlänge beziehungsweise -breite, die Anfangs- und Endkonfiguration und die Definition des Objektes werden auch abgespeichert. Zudem noch die Periodizität, falls es sich um ein oszillierendes oder gleitendes Objekt handelt. 

{width: "100%"}
![Abb. 15: Ausschnitt aus CSV-File in Power BI](CSV-File.png)  



[^footnote-2]: Weitere Informationen zu CSV-Files unter: <https://de.wikipedia.org/wiki/CSV_(Dateiformat)>



                                                                                      
                                                                                      
                                                                               
                                                                                                                                                                