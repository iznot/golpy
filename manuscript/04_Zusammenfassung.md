# Zusammenfassung

In dieser Arbeit befasse ich mich mit Conway's "Game of Life". Dieses "No player, never ending Game" bringt verschiedene ungelöste Probleme mit sich. Die theoretische Informatik befasst sich damit, dass der Spielverlauf einer Konfiguration nicht vorhergesagt werden kann. Daraus folgen zwei Probleme: 

1. Es besteht kein Algorithmus, der als Input eine Konfiguration nimmt und als Output das daraus entstehende Objekt wiedergibt.
1. Es besteht kein Algorithmus, der als Input zwei Konfigurationen nimmt und als Output sagt, ob die eine aus der anderen entstehen wird oder nicht.

<!-- NOTE: ich würde eher sagen "Es existiert kein bekannter Algorithmus... -->

<!-- QUESTION: Was ist genau ein Algorithmus? Ist das Durchspielen kein Algo? Falls ja würde ich sagen: "... ausser das Spiel zu spielen.-->

Im Verlauf dieser Arbeit versuchte ich diese Probleme zu lösen <!-- NOTE: umgehen. Du löst sie ja nicht tatsächlich.-->, in dem ich eine Simulation programmierte, die alle möglichen Konfigurationen auf einem begrenzten Gameboard durchspielt. Diese werden nach dem daraus entstehenden Objekt gefiltert und abgespeichert.

Nun kann für jede Konfiguration auf diesem begrenzten Spielfeld gesagt werden, zu welcher Gruppe von Objekten sie gehört. Dadurch, dass der Spielverlauf bekannt ist, kann eine Konfiguration mit einer anderen verglichen werden und mit Sicherheit gesagt werden, ob die eine aus der anderen entstehen wird oder nicht. 

<!-- TODO: ag nochmals genau durchlesen und mit den Begriffen im Glossar abgleichen. -->

Da die Anzahl möglicher Konfigurationen mit grösserem Gameboard massiv steigt, konnte ich alle Konfigurationen bis zu einem 5x5 grossen Spielfeld abspielen lassen. Dadurch ist die Aussagekraft der Resultate limitiert. 

Ausserdem sind beide Probleme durch die Methode der Simulation nicht gelöst. Zum einen sind die Fragen nicht für *alle* Konfigurationen beantwortet. Zum anderen müssen die Konfigurationen tatsächlich durchgespielt werden. Die Simulation sagt also einen Spielverlauf nicht wirklich voraus. 