{#glossar}
# Glossar

Gameboard
: Das Spielbrett des Conway's Game of Life. In meiner Arbeit habe ich mit 5x5 Gameboards gearbeitet.
: `basic_game_functions.create_gameboard(input_array = None, rows = None, cols = None, origin=(0,0))`$

Konfiguration
: Ein bestimmtes Gameboard mit festgelegten lebenden und toten Zellen.
: `gameboard`$

Grundkonfiguration
: Die Konfiguration, die übrig bleibt, wenn vom Rand des Gameboards alle nicht lebenden Zeilen und Spalten abgeschnitten werden.

Relative Position
: <!-- TODO: ag>

Anfangskonfiguration
: Eine Konfiguration bevor sie je abgespielt wurde. Die Anfangskonfiguration wird dann simuliert.

Spielzug (Play)
: Ein Spielzug bezeichnet die Anwendung der Spielregeln auf eine Konfiguration. Durch einen Spielzug entsteht aus einer Konfiguration eine neue Konfiguration.
: `basic_game_functions.play(gameboard)`$

Die n. Generation
: Die Konfiguration, die nach dem n. nacheinander folgenden Spielzug aus der Anfangskonfiguration entsteht. 

Endzustand
: Entsteht nach einer gewissen Anzahl von Spielzügen eine Grundkonfiguration, die im Spielverlauf bereits einmal entstanden ist, so hat das Spiel den Endzustand erreicht. Ist der Endzustand erreicht, ist das Spiel zu Ende.

Spiel
: Werden auf eine Anfangskonfiguration wiederholt Spielzüge ausgeführt bis der Endzustand erreicht ist, so sprechen wir von einem Spiel.
: `run_simulation.run_simulation(gameboard, max_runs)`$

Simulation
: Die Spiele aller möglichen Konfigurationen auf einem Gameboard einer bestimmten Grösse (hier 5x5).
: `run_simulation.generate_simulation(shape, alive_count, max_runs, folder = "sim", debug = False)`$

Spielklassen
: Spiele können in verschiedene Klassen eingeteilt werden, je nachdem wie sich die Konfigurationen über den Spielverlauf entwickeln. Unterschieden werden folgende Spielklassen: statisch, oszillierend, gleitend, selbst auslöschend, überlebend.

Objekt
: Konfigurationen, die in Simulationen immer wieder auftauchen, werden als Objekte bezeichnet und benannt, z.B.: Gleiter, Tümmler, Blinker, Uhr, Fresser, Segler, etc. Objekte verhalten sich nach Spielklassen, d.h. statisch, oszillierend, gleitend, selbst auslöschend, überlebend. In einer Konfiguration können grundsätzlich auch mehrere Objekte vorkommen. Zum Beispiel eine Kanone, die immer wieder Gleiter schiesst. In meiner Arbeit habe ich nicht zwischen Objekt und Grundkonfiguration unterschieden.


Periodizität
: Die Anzahl an Generationen bis wieder dieselbe Grundkonfiguration entsteht. Dies ist nur bei gleitenden und oszillierenden Spielen relevant. 

Doppelgänger
: <!-- TODO: ag -->

Affine Konfigurationen
: Zwei Konfigurationen sind affin, wenn die relative Konfiguration der einen durch mindestens eine der folgenden Operationen in die relative Konfiguration der anderen transformiert werden kann:
- horizontale Spiegelung
- vertikale Spiegelung
- Drehung um 90 Grad
- Drehung um 180 Grad
- Drehung um 270 Grad