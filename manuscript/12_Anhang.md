# Anhänge

## Referenzen

- **Golpy{#golpy}: Die gesamte Arbeit, inklusive Sourcecode, ist verfügbar unter <https://github.com/iznot/golpy>.
- Die Sourcecode Dokumentation zu dieser Arbeit ist online verfügbar unter <https://iznot.github.io/golpy/>.
- Ein Dashboard mit den Resultaten der Simulation ist verfügbar unter <https://app.powerbi.com/viewr=eyJrIjoiNzFiNGFlYjgtZTk0Yi00NTgwLThiZDUtZDQ4MWI1ZGU1MjUzIiwidCI6ImJlZTU0ZGU1LTQ3NDQtNGU0Ny04YTIwLWVhOGI4NDJiOTE5ZCJ9&pageName=ReportSection>.
- Das CSV-Files mit den simulierten Spielen sind verfügbar unter <https://github.com/iznot/golpy/tree/master/sim>
  
## Verwendete Tools

Ich verwendete Python 3.10.5.

Ich arbeitete mit Visual Studio Code (VSC).

Im Verlauf dieser Arbeit verwendete ich folgende Programmierbibliotheken:
- numpy 1.23.1
- joblib 1.2.0
- scipy 1.9.3
- mkdocs 1.4.2

## Reproduktion der Resultate

Um die Resultate dieser Arbeit zu reproduzieren müssen folgende Schritte ausgeführt werden:

### Voraussetzungen

1. git installiert
2. Python installiert
3. Windows Computer (nur zum Ausführen der Powershell Skripte und zur Analyse in PowerBI notwendig)
4. PowerBI Desktop installiert (da die Datenmenge zu gross ist für Excel)
   
### Schritte

1. iznot/golpy von GitHub klonen <https://github.com/iznot/golpy.git>
2. benötigte Programmierbibliotheken installieren, z.B. durch Ausführen von `./scripts/pip.ps1`
3. in `simulation.py` in der `main` Funktion die gewünschten Dimensionen des Gameboards konfigurieren
4. `simulation.main` in Python ausführen
5. durch Ausführen des Skripts `./scripts/combine_csv.ps1` die erstellten CSV-Files zusammenfügen
6. das kombinierte CSV-File in PowerBI importieren

## GUI

Bemerkung: Die GUI-Anwendung von golpy wurde von Christoph Glur mit tkinter entwickelt. 

### Voraussetzungen

golpy ist lokal installiert und lauffähig (siehe Voraussetzungen oben).

### Schritte

1. Die `main` Funktion in `gui.py` ausführen.

{width: "60%"}
![Screenshot des Grafischen User Interfaces (GUI) von golpy](screenshot_gui.png)  

## Erklärung

„Ich erkläre hiermit, dass ich die vorliegende Maturaarbeit selbständig und ohne unerlaubte fremde Hilfe erstellt habe und dass alle 
Quellen, Hilfsmittel und Internetseiten wahrheitsgetreu verwendet wurden und belegt sind.“

{width: "10%"}
![Unterschrift, Anaïs Glur](Unterschrift.png)  