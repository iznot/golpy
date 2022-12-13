# Outline

1. Einführung
1. Resultate
    1. resultat

TODO: Seitenumbruch?
TODO: Textanordnung nicht links


# Einleitung #
<!-- das ist ein Teil-->

## John Conway
John Horton Conway ist wohl einer der bedeutsamsten Mathematiker aus dem letzten Jahrhundert. Er wurde 1937 in Liverpool geboren und verstarb vor zwei Jahren im Alter von 82 Jahren an Covid19. Er studierte Mathematik an der Universität Cambridge, wo er später mathematische Logik unterrichtete. Während dieser Zeit machte er sich einen Namen in dem Gebiet der Gruppentheorie. Er entdeckte eine endliche Gruppe mit über 8 Trillionen Elementen in einem 24-dimensionalem Raum, die nach ihm benannt wurde.

Ihm war es wichtig, die Mathematik den Leuten näherzubringen. Dadurch unterrichtete er nicht nur Hochbegabte an Universitäten, sondern auch jüngere und normal-talentierte Kinder. Er gab viele Vorträge, bei denen er entweder gänzlich vom Thema abkam, oder gar nicht erst erschien, bezeichnete sich selbst als faul und ging stets barfuss oder in Sandalen. Er widerspiegelte wohl genau das Bild, was die Allgemeinheit von einem zerstreuten Professor hat.

{width: "30%"}
![Abb. 1: John Horton Conway](conway.png) Schon als Kind hatte er eine Faszination für Spiele, welche ihn später in die Unterhaltungsmathematik führte. Er war eine der ersten Personen, die eine Theorie zur Lösung des Rubic Scubes veröffentlichte, konnte dank einer selbstentwickelten Methode innerhalb von Sekunden den Wochentag beliebiger Daten ausrechnen und wurde von seinen Kollegen «Mathemagier» genannt. 

Der Öffentlichkeit wurde er durch die Entwicklung des «Game of Life» bekannt. Dieses «no-player, never ending game», wie er es auch nannte, entwickelte er in den 70er Jahren. Dieses Spiel war der Startschuss für Simulationen auf dem Gebiet der Komplexitätswissenschaft und viele liessen sich dafür begeistern. Unzählige versuchten das «Leben» zu hacken, in dem sie neue Lebensformen entdecken. Die ansteigende Popularität seiner Entwicklung gefiel Conway gar nicht, weshalb er Fragen über seine Kreation mit dem Satz «I hate life» auswich. Gegen das Ende seines realen Lebens konnte er sich jedoch wieder damit anfreunden: «Ich gab irgendwo einen Vortrag und wurde als ‘John Conway, Schöpfer des Lebens’ vorgestellt. Und ich dachte ‘Oh das ist eine nette Art bekannt zu sein’.». 

Die Faszination des Spieles liegt darin, dass ein einfaches Konzept mit vier simplen Regeln komplexe Themen behandelt. Wie der Musiker Brian Eno sagte, «Wir sind an die Idee gewöhnt, dass alles Komplexe aus etwas noch Komplexerem hervorgehen muss. […] Life zeigt uns komplexe, virtuelle Organismen, erschafft durch die Interaktion mit ein paar einfachen Regeln.»

## Regel

Ein faszinierendes Spiel, welches auf drei einfachen Regeln basiert. Man stelle sich ein Schachbrett vor, welches über eine beliebig grosse Anzahl an Feldern verfügt. Jedes Feld, oder besser, jede Zelle kann entweder lebendig oder tot sein. Durch die Abhängigkeit von ihren Nachbarn kann sich der Status der Zelle von Generation zu Generation verändern. Jede Zelle hat acht Nachbarn, drei oben, drei unten und noch je einen auf jeder Seite. Zu Beginn kann der Zustand jeder Zelle festgelegt werden. Nun gelten folgende Regeln:
1.	Der Status einer Zelle bleibt unverändert, wenn diese zwei Nachbarn hat.
2.	Hat die Zelle drei Nachbarn, ist diese zwingend am Leben.
3.	Wenn weniger als zwei Nachbarn leben, stirbt die Zelle an Einsamkeit.
4.	Hat sie mehr als drei Nachbarn stirbt sie an Überbevölkerung.

TODO Beispiel für Lebensentwicklung

## Objekte
Über die Jahre sind viele unterschiedliche Objekte entdeckt worden. Diese können in verschiedene Kategorien eingeteilt werden:

1. ### Statische Objekte

Statische Objekte, oft auch «Stillleben» genannt, definieren sich dadurch, dass sie ohne äussere Einflüsse stillstehen. Dies ist möglich, wenn jede lebende Zelle zwei oder drei Nachbarn hat, aber keine der tote genau drei.
TODO Beispiel für Statisches Objekt

2. ### Oszillierende Objekte

Oszillatoren ändern sich einem bestimmten Schema folgend in periodischen Zeitabständen. Hierbei ändern sie ihren Standort nicht, sondern verhalten sich stationär.
TODO Beispiel für oszillator

3. ### Raumschiff

Wie auch die Oszillatoren verändern sie sich periodisch nach einem bestimmten Schema. Der Unterschied liegt aber darin, dass sie ihre Position ändern. Auf einem unendlichen Spielfeld können sie sich somit unbegrenzt fortbewegen.
TODO Beispiel spaceship

4. ### Selbstauslöschende Objekte

Diese Objekte enden nach beliebeg vielen Generationen in einem leeren Spielfeld
TODO Beispiel erased



Es gibt noch weitere Objekte wie Gleiterkanonen, die in einem periodischem Zeitabstand immer wieder Gleiter erzeugen, Puffer, die eine Art Gleiter mit Überbleibsel darstellen oder völlig chaotische Objekte. Diese weiteren Objekte sind für diese Arbeit jedoch nicht relevant.

## Probleme
Der Anwendungsbereich des «Game of Life» greift viele Themenbereiche auf und löst somit auch bei vielen Menschen eine Faszination aus. Aufgrund dessen beschäftigen sich Mathematiker, Informatiker, Physiker und viele mehr mit den ungelösten Problemen, die das Spiel mit sich bringt. Einige der Probleme sind mit der Zeit bereits gelöst worden, andere noch nicht. In der Theoretischen Informatik ist das Spiel besonders als Entscheidungsproblem interessant. Es existiert keinen Algorithmus, der mit dem Input zweier Konfiguration entscheiden kann, ob die eine aus der anderen entstehen kann. Zudem ist kein Algorithmus bekannt, der bestimmen kann, was der Endzustand einer gegebenen Konfiguration ist. In dieser Arbeit versuche ich mich diesen beiden Problemen zu widmen.


# Material und Methode
Um mich diesen grossen Fragen des «Game of Life» stellen zu können, programmierte ich als erstes das einfache Grundkonzept des Spieles. Danach widmete ich mich der Programmierung einer Simulation, die für mich schlussendlich auf einem beliebig grossen Spielfeld alle möglichen Konfiguration durchspielen sollte. 

## Game of Life
Während der Programmierung des Grundkonzeptes filterten sich mehrere Probleme heraus. Als Programmieranfängerin war das ganze natürlich noch schwieriger. Zuerst machte ich mich an das Gameboard.

### Das Gameboard
Das Gameboard ist ein numpy Array bestehend aus Booleans. Die Reihen sind auf der Achse mit dem Index 0 und die Kollonen auf der mit dem Index 1. Die Kollonen werden durch Bindestriche ('---') und die Reihen durch Trennstriche ('|') dargestellt. Zusammen bilden sie nun eine Zelle. Somit sieht ein Gameboard mit der Grösse 5x5 wie folgt aus:

TODO wieso '-1?'
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

Um eine Konfiguration durchzuspielen, muss der Status der Nachbarszellen bekannt sein. Zuerst iteriere ich also durch das Spielfeld, um alle lebendigen Zellen herauszufinden. Als nächstes marschiere ich um jede lebendige Zelle herum und zähle, wie viele der Nachbarszellen lebendig sind. Nun muss nur noch den bereits bekannten Regeln gefolgt werden und ein neues Gameboard ausgedruckt werden. 

TODO gespieltes Gameboard 

### Grenzfälle

Ein Problem stellten die Grenzfälle dar. Eine Zelle am Rand hat nur fünf existente Nachbarn und eine in einem Ecken sogar nur drei. Zuerst löste ich das Problem damit, dass die oberste linkste Zelle die oberste rechteste Zelle als direkten linken Nachbarn hat und umgekehrt. Als direkten oberen Nachbarn hat sie die unterste linkste Zelle und als schräg-oberen, rechten Nachbarn din rechts untersten. Eine Zelle am linken Rand hat die Zelle am rechten Rand in der gleichen Reihe als direkten Nachbarn, eine Zelle am oberem Rand hat eine Zelle in der selben Kollone als Nachbar und so weiter. Die folgenden Zellen sind also Nachbarn:

{title: "Grenzfälle Nachbarn", id: gb-1}
```text
Generation 0:           Gen 1:
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

Mit dem Hinblick auf die Simulation die ich später erstellen würde, war diese Lösung nicht die beste. Für diese ist es nämlich wichtig, dass das Gameboard unendlich gross ist, da sonst die folgende Generation verfälscht werden könnte. Also schrieb ich eine Funktion, die jedesmal wenn eine Zelle an den Rand des Gameboardes kommt, dieses um eine Reihe oder Kollone, je nach Fall, vergrösserte. Somit ist sichergestellt, dass jede Zelle immer acht Nachbarn hat.
Das vorherige Gameboard würde dann also, trotz einer vorgegebenen Grösse von 5x5 wie folgt aussehen:








{width: "60%"}
![Beispiel: Bravo!](bspl.png)  


{title: "Wahnsinnig schönes gameboard.", id: gb-1}
```text
 --- --- --- --- --- 
|   |   |   |   |   |
 --- --- --- --- --- 
|   |   |   |   |   |
 --- --- --- --- --- 
|   |   |   |   |   |
 --- --- --- --- --- 
|   |   |   |   | o |
 --- --- --- --- --- 
|   | o | o | o | o |
 --- --- --- --- --- 
```