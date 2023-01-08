# Zusammenfassung

In dieser Arbeit befasse ich mich mit Conway's "Game of Life". Dieses "No player, never ending Game" bringt verschiedene ungelöste Probleme mit sich. Die theoretische Informatik befasst sich damit, dass der Spielverlauf einer Konfiguration nicht vorhergesagt werden kann. Daraus ergeben sich zwei Probleme: 

1. Es existiert kein bekannter Algorithmus, der als Input eine Konfiguration nimmt und als Output deren Spielklasse wiedergibt.
2. Es existiert kein bekannter Algorithmus, der als Input zwei Konfigurationen nimmt und als Output sagt, ob die eine aus der anderen entstehen wird oder nicht.

Im Verlauf dieser Arbeit versuchte ich diese Probleme zu umgehen.
Zum einen tat ich dies durch zwei Funktionen. Die erste spielt die gegebene Konfiguration durch und ordnet diesem Spiel eine Spielklasse zu, nähert sich also dem ersten Problem. Die zweite Funktion hat als Input eine zu testende und eine zu vergleichende Konfiguration. Sie spielt die zu vergleichende Konfiguration durch und gleicht deren Generationen auf Affinität mit der zu testenden Konfiguration ab. Diese nähert sich also dem zweiten Problem.

Der zweite Ansatzpunkt war eine Simulation. Ich programmierte eine Simulation, die alle möglichen Konfigurationen auf einem begrenzten Spielfeld durchspielte, deren Spielklasse zuordnete und abspeicherte. Dadurch war es mir möglich, die einzelnen Spiele zu analysieren und nach Auffälligkeiten zu suchen.   

Da die Anzahl möglicher Konfigurationen mit grösserem Gameboard massiv steigt, konnte ich mit der Simulation alle Konfigurationen bis zu einem 5x5 grossen Spielfeld abspielen lassen. Dadurch ist die Aussagekraft der Resultate limitiert. 

Meine beiden Funktionen sind funktionsfähig und können das gewünschte Resultat aufzeigen, die Probleme sind dadurch allerdings nicht wirklich gelöst. Die Funktionen können ein Spiel nicht vorhersagen, sie können es nur zuordnen oder abgleichen. 

Der Python Sourcecode zu dieser Arbeit ist verfügbar auf <https://github.com/iznot/golpy>.

Die Datenanalyse ist unter folgendem Link zu finden:
<https://app.powerbi.com/viewr=eyJrIjoiNzFiNGFlYjgtZTk0Yi00NTgwLThiZDUtZDQ4MWI1ZGU1MjUzIiwidCI6ImJlZTU0ZGU1LTQ3NDQtNGU0Ny04YTIwLWVhOGI4NDJiOTE5ZCJ9&pageName=ReportSection>
