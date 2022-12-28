## Wichtig

Wir benutzen github lfs (Large File Storage), um die csv Simulationsresultate zu tracken.

Man muss entweder LFS oder Github Desktop installieren, um diese Files zu pullen.

See here: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage

## Namenskonvention

Wir benutzen folgende Namenskonvention für csv Files: simulation_results_i_j_a.csv, wobei sich i, j, und a auf die Anfangskonfiguration (d.h. das Spielbrett)
beziehen, und zwar so:

- i: Anzahl Zeilen
- j: Anzahl Spalten
- a: Anzahl der lebendigen Zellen in der Anfangskonfiguration

Zum Beispiel, `simulation_results_3_4_2.csv` enthält nur Anfangsspielbretter mit Dimension 3x4 und genau 2 lebendigen Zellen.


Für unvollständige CSV Files benutzen wir den Suffix _nf, zum Beispiel simulation_results_5_6_9_nf.csv