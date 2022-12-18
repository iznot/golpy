# Zusammenfassung
In dieser Arbeit befasse ich mich mit Conway's "Game of Life". Dieses "No player, never ending Game" bringt verschiedene ungelöste Probleme mit sich. Die theoretische Informatik befasst sich damit, dass der Spielverlauf einer Konfiguration nicht vorhergesagt werden kann. Daraus folgen zwei Probleme: 

1. Es besteht kein Algorithmus, der als Input eine Konfiguration hat und als Output das daraus entstehende Objekt wiedergibt.
1. Es besteht kein Algorithmus, der als Input zwei Konfigurationen hat und als Output sagt, ob die eine aus der anderen entstehen wird oder nicht.

Im Verlauf dieser Arbeit versuche ich diese Probleme zu lösen, in dem ich eine Simulation programiere, die alle möglichen Konfigurationen auf einem begrenzten Spielfeld durchtestet. Diese werden nach dem daraus entstehenden Objekt gefiltert und abgespeichert.

Nun kann für jede Konfiguration auf diesem begrenzten Spielfeld gesagt werden, zu welcher Gruppe von Objekten sie gehört. Dadurch, dass der Spielverlauf bekannt ist, kann eine Konfiguration mit einer anderen verglichen werden und mit Sicherheit gesagt werden, ob die eine aus der anderen entstehen wird oder nicht. 

Da die simulierende Funktion nicht sehr effizient ist, kann ich nur alle Konfigurationen auf einem 4x4 grossen Spielfeld abspielen lassen. Dadurch ist die bestehende Informationsbreite dürftig. Die beiden Probleme können nicht mit einer Simulation gelöst werden, da die Fragen nicht für alle Konfigurationen beantwortet sind und sie vorher zuerst durchgespielt werden müssen. Die Simulation sagt einen Spielverlauf nicht voraus, sondern hat sich das Wissen darüber schon vorher angeeignet. 