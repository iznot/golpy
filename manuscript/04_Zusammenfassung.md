# Zusammenfassung

In dieser Arbeit befasse ich mich mit Conway's "Game of Life". Dieses "No player, never ending Game" bringt verschiedene ungelöste Probleme mit sich. Die theoretische Informatik befasst sich damit, dass der Spielverlauf einer Konfiguration nicht vorhergesagt werden kann. Daraus ergeben sich zwei Probleme: 

1. Es existiert kein bekannter Algorithmus, der als Input eine Konfiguration nimmt und als Output deren Spielklasse wiedergibt.
1. Es existiert kein bekannter Algorithmus, der als Input zwei Konfigurationen nimmt und als Output sagt, ob die eine aus der anderen entstehen wird oder nicht.



Im Verlauf dieser Arbeit versuchte ich diese Probleme zu umgehen, indem ich eine Simulation programmierte, die alle möglichen Konfigurationen auf einem begrenzten Gameboard durchspielt. Diese werden, je nach dem daraus entstehenden Objekt, nach Spielklasse gefiltert und abgespeichert.

Nun kann für jede Konfiguration auf diesem begrenzten Gameboard gesagt werden, zu welcher Spielklasse sie gehört. Dadurch, dass das Spiel bekannt ist, kann eine Konfiguration mit einer anderen verglichen und mit Sicherheit gesagt werden, ob die eine aus der anderen entstehen wird oder nicht. 

Da die Anzahl möglicher Konfigurationen mit grösserem Gameboard massiv steigt, konnte ich alle Konfigurationen bis zu einem 5x5 grossen Spielfeld abspielen lassen. Dadurch ist die Aussagekraft der Resultate limitiert. 

Ausserdem sind beide Probleme durch die Methode der Simulation nicht gelöst. Zum einen sind die Fragen nicht für *alle* Konfigurationen beantwortet. Zum anderen müssen die Konfigurationen tatsächlich durchgespielt werden. Die Simulation sagt also einen Spielverlauf nicht wirklich voraus. 

Der Python Sourcecode zu dieser Arbeit ist verfügbar auf <https://github.com/iznot/golpy>.

Die Datenanalyse ist unter folgendem Link zu finden:
TODO Link einfügen

