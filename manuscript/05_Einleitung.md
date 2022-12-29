# Einleitung #

## John Conway
John Horton Conway ist einer der bedeutsamsten Mathematiker aus dem letzten Jahrhundert. Er ist 1937 in Liverpool geboren worden und verstarb vor zwei Jahren im Alter von 82 Jahren an Covid-19. Er studierte Mathematik an der Universität Cambridge, wo er später mathematische Logik unterrichtete. Während dieser Zeit machte er sich einen Namen in dem Gebiet der Gruppentheorie. Er entdeckte eine endliche Gruppe mit über 8 Trillionen Elementen in einem 24-dimensionalem Raum, die nach ihm benannt wurde.

Ihm war es wichtig, die Mathematik den Leuten näherzubringen. Dadurch unterrichtete er nicht nur Hochbegabte an Universitäten, sondern auch jüngere und durchschnittlich-talentierte Kinder. Er gab viele Vorträge, bei denen er entweder gänzlich vom Thema abkam, oder gar nicht erst erschien, bezeichnete sich selbst als faul und ging stets barfuss oder in Sandalen. Er widerspiegelte genau das Bild, was die Allgemeinheit von einem zerstreuten Professor hat.

{width: "30%"}
![Abb. 1: John Horton Conway](conway.png) 

Schon als Kind hatte er eine Faszination für Spiele, welche ihn später in die Unterhaltungsmathematik führte. Er war eine der ersten Personen, die eine Theorie zur Lösung des Rubic Scubes veröffentlichte, konnte dank einer selbstentwickelten Methode innerhalb von Sekunden den Wochentag beliebiger Daten ausrechnen und wurde von seinen Kollegen «Mathemagier» genannt. 

Der Öffentlichkeit wurde er durch die Entwicklung des «Game of Life» bekannt. Dieses «no-player, never ending game», wie er es auch nannte, entwickelte er in den 70er Jahren. Dieses Spiel war der Startschuss für Simulationen auf dem Gebiet der Komplexitätswissenschaft und viele liessen sich dafür begeistern. Die ansteigende Popularität seiner Entwicklung gefiel Conway gar nicht, weshalb er Fragen über seine Kreation mit dem Satz «I hate Life» auswich. Gegen das Ende seines realen Lebens konnte er sich jedoch wieder damit anfreunden: "Ich gab irgendwo einen Vortrag und wurde als ‘John Conway, Schöpfer des Lebens vorgestellt. Und ich dachte ‘Oh das ist eine nette Art, bekannt zu sein’.". 

Die Faszination des Spieles liegt darin, dass ein einfaches Konzept mit vier simplen Regeln komplexe Themen behandelt. Wie der Musiker Brian Eno sagte, "Wir sind an die Idee gewöhnt, dass alles Komplexe aus etwas noch Komplexerem hervorgehen muss. […] Life zeigt uns komplexe, virtuelle Organismen, erschaffen durch die Interaktion mit ein paar einfachen Regeln."

## Regeln

Ein faszinierendes Spiel, welches auf vier einfachen Regeln basiert. Man stelle sich ein Schachbrett vor, welches über eine beliebig grosse Anzahl an Feldern verfügt. Jedes Feld, oder besser, jede Zelle kann entweder lebendig oder tot sein. Durch die Abhängigkeit von ihren Nachbarn kann sich der Status der Zelle von Generation zu Generation verändern. Jede Zelle hat acht Nachbarn, drei oben, drei unten und noch je einen auf jeder Seite. Zu Beginn kann der Zustand jeder Zelle festgelegt werden. Nun gelten folgende Regeln:

1.	Der Status einer Zelle bleibt unverändert, wenn diese zwei Nachbarn hat.
2.	Hat die Zelle drei Nachbarn, ist diese zwingend am Leben.
3.	Wenn weniger als zwei Nachbarn leben, stirbt die Zelle an Einsamkeit.
4.	Hat sie mehr als drei Nachbarn, stirbt sie an Überbevölkerung.

TODO Bessere Darstellung, siehe Dossier

{title: "Lebensentwicklung", id:life_gb}
```text
Konfiguration:            1. Generation:           2. Generation:               
 --- --- --- --- ---      --- --- --- --- ---      --- --- --- --- ---              
|   |   |   |   |   |    |   |   |   |   |   |    |   |   |   |   |   |              
 --- --- --- --- ---      --- --- --- --- ---      --- --- --- --- ---             
|   | o | o |   |   |    |   | o | o |   |   |    |   | o | o |   |   |              
 --- --- --- --- ---      --- --- --- --- ---      --- --- --- --- ---             
|   | o |   |   |   |    |   | o |   |   |   |    |   | o | o |   |   |              
 --- --- --- --- ---      --- --- --- --- ---      --- --- --- --- ---             
|   |   | o |   |   |    |   |   |   |   |   |    |   |   |   |   |   |              
 --- --- --- --- ---      --- --- --- --- ---      --- --- --- --- ---             
|   |   |   |   |   |    |   |   |   |   |   |    |   |   |   |   |   |              
 --- --- --- --- ---      --- --- --- --- ---      --- --- --- --- ---             
```

## Objekte   

Über die Jahre wurden viele unterschiedliche Objekte entdeckt. Diese können in verschiedene Kategorien eingeteilt werden:

### Statische Objekte

Statische Objekte, oft auch «Stillleben» genannt, definieren sich dadurch, dass sie ohne äusseren Einfluss stillstehen. Dies ist möglich, wenn jede lebende Zelle zwei oder drei Nachbarn hat, aber keine der tote genau drei.
Die 2. Generation des vorherigen Beispiels ist ein statisches Objekt:

TODO verdeutlichen mit mehreren Generationen
{title: "Statisches Objekt", id:stable_gb}
```text
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
|   | o | o |   |   |
 --- --- --- --- ---
|   | o | o |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
|   |   |   |   |   |
 --- --- --- --- ---
 ```
### Oszillierende Objekte

Oszillatoren ändern sich, einem bestimmten Schema folgend, in periodischen Zeitabständen. Hierbei ändern sie ihren Standort nicht, sondern verhalten sich stationär.

{title: "Oszillierende Objekte", id:oscillator}

```text
Konfiguration:                           
 --- --- --- --- --- --- --- --- ---                                      
|   |   |   |   |   |   |   |   |   |                                     
 --- --- --- --- --- --- --- --- ---                                       
|   |   |   | o | o | o |   |   |   |                                     
 --- --- --- --- --- --- --- --- ---                                        
|   |   |   |   |   |   |   |   |   |                                      
 --- --- --- --- --- --- --- --- ---                                        
|   | o |   |   |   |   |   | o |   |                                      
 --- --- --- --- --- --- --- --- ---                                        
|   | o |   |   |   |   |   | o |   |                                      
 --- --- --- --- --- --- --- --- ---                                        
|   | o |   |   |   |   |   | o |   |                                      
 --- --- --- --- --- --- --- --- ---                                        
|   |   |   |   |   |   |   |   |   |                                      
 --- --- --- --- --- --- --- --- ---                                        
|   |   |   | o | o | o |   |   |   |                                      
 --- --- --- --- --- --- --- --- ---                                        
|   |   |   |   |   |   |   |   |   |                                      
 --- --- --- --- --- --- --- --- ---     


1. Generation                         
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   | o |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   | o |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   | o |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   |   |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
| o | o | o |   |   |   | o | o | o | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   |   |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   | o |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   | o |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   | o |   |   |   |   | 
 --- --- --- --- --- --- --- --- --- 


2.Generation
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   |   |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   | o | o | o |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   |   |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   | o |   |   |   |   |   | o |   | 
 --- --- --- --- --- --- --- --- ---  
|   | o |   |   |   |   |   | o |   | 
 --- --- --- --- --- --- --- --- ---  
|   | o |   |   |   |   |   | o |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   |   |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   | o | o | o |   |   |   | 
 --- --- --- --- --- --- --- --- ---  
|   |   |   |   |   |   |   |   |   | 
 --- --- --- --- --- --- --- --- ---  

```

### Gleitende Objekte

Wie auch die Oszillatoren verändern sich diese Objekte periodisch nach einem bestimmten Schema. Der Unterschied liegt aber darin, dass sie ihre Position ändern. Auf einem endlosen Spielfeld hören sie also nie auf, sich fortzubewegen.

TODO Bewegung muss sichtbar sein auf Darstellung
{title: "Gleitende Objekte", id:spaceship_gb}
```text
Konfiguration:         1. Generation:         2.Generation:               
 --- --- --- --- ---    --- --- --- --- ---    --- --- --- --- ---          
|   |   |   |   |   |  |   |   |   |   |   |  |   |   |   |   |   |     
 --- --- --- --- ---    --- --- --- --- ---    --- --- --- --- ---          
|   |   | o |   |   |  |   | o |   | o |   |  |   |   |   | o |   |     
 --- --- --- --- ---    --- --- --- --- ---    --- --- --- --- ---          
|   |   |   | o |   |  |   |   | o | o |   |  |   | o |   | o |   |     
 --- --- --- --- ---    --- --- --- --- ---    --- --- --- --- ---          
|   | o | o | o |   |  |   |   | o |   |   |  |   |   | o | o |   |     
 --- --- --- --- ---    --- --- --- --- ---    --- --- --- --- ---          
|   |   |   |   |   |  |   |   |   |   |   |  |   |   |   |   |   |     
 --- --- --- --- ---    --- --- --- --- ---    --- --- --- --- ---         
 3.Generation:            4.Generation         
  --- --- --- --- ---     --- --- --- --- ---  
 |   |   |   |   |   |   |   |   |   |   |   | 
  --- --- --- --- ---     --- --- --- --- ---  
 |   | o |   |   |   |   |   |   | o |   |   | 
  --- --- --- --- ---     --- --- --- --- ---  
 |   |   | o | o |   |   |   |   |   | o |   | 
  --- --- --- --- ---     --- --- --- --- ---  
 |   | o | o |   |   |   |   | o | o | o |   | 
  --- --- --- --- ---     --- --- --- --- ---  
 |   |   |   |   |   |   |   |   |   |   |   | 
  --- --- --- --- ---     --- --- --- --- ---  
```


### Selbstauslöschende Objekte

Diese Objekte enden nach beliebig vielen Generationen in einem leeren Spielfeld


{text: "Selbst auslöschendes Objekt", id:erased_gb}
```text
Konfiguration:                1.Generation                  2. Generation:
 --- --- --- --- ---           --- --- --- --- ---           --- --- --- --- ---   
|   |   |   |   |   |         |   |   |   |   |   |         |   |   |   |   |   |
 --- --- --- --- ---           --- --- --- --- ---           --- --- --- --- ---   
|   | o |   |   |   |         |   |   |   |   |   |         |   |   |   |   |   |
 --- --- --- --- ---           --- --- --- --- ---           --- --- --- --- ---   
|   |   |   | o |   |         |   |   | o |   |   |         |   |   |   |   |   |
 --- --- --- --- ---           --- --- --- --- ---           --- --- --- --- ---   
|   | o |   |   |   |         |   |   |   |   |   |         |   |   |   |   |   |
 --- --- --- --- ---           --- --- --- --- ---           --- --- --- --- ---   
|   |   |   |   |   |         |   |   |   |   |   |         |   |   |   |   |   |
 --- --- --- --- ---           --- --- --- --- ---           --- --- --- --- ---   
```


Es gibt noch weitere Objekte wie Gleiterkanonen, die in einem periodischen Zeitabstand immer wieder Gleiter erzeugen, Puffer, die eine Art Gleiter mit Überbleibsel darstellen oder völlig chaotische Objekte. Diese Objekte werden in dieser Arbeit jedoch nicht konkret berücksichtigt.

## Probleme

Die Anwendung des «Game of Life» greift in viele Themenbereiche ein. So in der Biologie, wobei das Spiel als ein Blick ins Mikroskop interpretiert wird, das Interesse also auf den Lebensformen liegt. Auch vertritt das Konzept einen ökonomischen Aspekt, wobei das Sterben und Gebären der Zellen das Angebot und die Nachfrage auf einem Finanzmarkt darstellen. Weiter ist das Spiel für die Physik interessant. Hierbei liegt das Augenmerk darauf, dass auf beliebig kleine Abweichungen der Anfangskonfiguration andere Resultate folgen, analog zu physikalischen Gleichungen. (Wikipedia 2023)

Durch diesen vielfältigen Anwendungsbereich interessieren sich viele verschiedene Menschen für Conway's Game of Life und beschäftigen sich mit den ungelösten Problemen, die das Spiel mit sich bringt. Einige der Probleme sind mit der Zeit bereits gelöst worden, andere noch nicht. In der theoretischen Informatik ist das Spiel besonders als Entscheidungsproblem interessant. Dadurch kristallisieren sich zwei Probleme heraus:

1. Es existiert kein Algorithmus, der bestimmen kann, zu welchem Objekt die Anfangskonfiguration mutieren wird.
2. Es existiert kein Algorithmus, der für alle Konfigurationen bestimmen kann, ob die eine aus der anderen entstehen wird.

In dieser Arbeit versuche ich, mich diesen beiden Problemen zu widmen.

NOTE Englische zitate übersetzt in Fussnote mitteilen


