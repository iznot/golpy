{#glossar}
# Glossar

Angegeben wird für jeden Begriff zuerst eine Erklärung, sowie zusätzlich ein Bezug auf den Python-Code falls sinnvoll.

Gameboard
: Das Spielbrett des Conway's Game of Life. In meiner Arbeit habe ich mit 5x5 Gameboards gearbeitet.
: `play.print_gameboard(configuration)`

Konfiguration
: Ein bestimmtes Gameboard mit festgelegten lebenden und toten Zellen, sowie der relativen Position (siehe unten)
: `play.create_configuration(input_array = None, rows = None, cols = None, origin=(0,0))`

Grundkonfiguration
: Die Konfiguration, die übrig bleibt, wenn vom Rand des Gameboards alle nicht lebenden Zeilen und Spalten abgeschnitten werden.
: `manipulation.get_base_configuration(configuration)?`


Relative Position
: Die Position der Grundkonfiguration auf dem begrenzten Gameboard. Diese wird zum Beispiel bei der Reduktion auf die Grundkonfiguration gesetzt.

Anfangskonfiguration
: Eine Konfiguration bevor sie je abgespielt wurde. Die Anfangskonfiguration wird dann simuliert.

Spielzug (Play)
: Ein Spielzug bezeichnet die Anwendung der Spielregeln auf eine Konfiguration. Durch einen Spielzug entsteht aus einer Konfiguration eine neue Konfiguration.
: `play.play(configuration)`

Die n. Generation
: Die Konfiguration, die nach dem n. nacheinander folgenden Spielzug aus der Anfangskonfiguration entsteht. 

Endzustand
: Entsteht nach einer gewissen Anzahl von Spielzügen eine Grundkonfiguration, die im Spielverlauf bereits einmal entstanden ist, hat das Spiel den Endzustand erreicht. Ist der Endzustand erreicht, ist das Spiel zu Ende.

Spiel
: Werden auf eine Anfangskonfiguration wiederholt Spielzüge ausgeführt, bis der Endzustand erreicht ist, so sprechen wir von einem Spiel.
: `game.play_full_game(start_configuration, max_runs)`

Simulation
: Die Spiele aller möglichen Anfangskonfigurationen auf einem Gameboard einer bestimmten Grösse (hier 5x5).
: `simulation.generate_simulation(gameboard_shape, alive_count, max_runs, folder = "sim", debug = False)`

Maximale Zahl
: Die zuvor festgelegte Anzahl an Spielzügen, nach deren Erreichen die Simulation abbricht, falls der Endzustand noch nicht erreicht worden ist.

Spielklassen
: Spiele können in verschiedene Klassen eingeteilt werden, je nachdem, wie sich die Konfigurationen über den Spielverlauf entwickeln. Unterschieden werden folgende Spielklassen: statisch, oszillierend, gleitend, selbst auslöschend, überlebend.
: `game.check_exit_criteria(game)`

Objekt
: Stereotype Konfigurationen, die in Simulationen immer wieder auftauchen, werden als Objekte bezeichnet. Die Literatur hat für einige Objekte gängige Namen festgelegt: Gleiter, Tümmler, Blinker, Uhr, Fresser, Segler, etc. Objekte verhalten sich nach Spielklassen, d.h. statisch, oszillierend, gleitend, selbst auslöschend, überlebend. In einer Konfiguration können grundsätzlich auch mehrere Objekte vorkommen. Zum Beispiel eine Kanone, die immer wieder Gleiter schiesst. In meiner Arbeit habe ich nicht zwischen Objekt und Grundkonfiguration unterschieden.

Periodizität
: Die Anzahl an Generationen, bis wieder dieselbe Grundkonfiguration entsteht. Dies ist nur bei gleitenden und oszillierenden Spielen relevant. 

Doppelgänger
: Zwei identische Grundkonfigurationen mit unterschiedlichen Positionen auf dem Gameboard.

Affine Konfigurationen
: Zwei Konfigurationen sind affin, wenn die relative Konfiguration der einen durch mindestens eine der folgenden Operationen in die relative Konfiguration der anderen transformiert werden kann:
- horizontale Spiegelung
- vertikale Spiegelung
- Drehung um 90 Grad
- Drehung um 180 Grad
- Drehung um 270 Grad
: `gameboard_manipulation.get_configuration_variations(configuration)`