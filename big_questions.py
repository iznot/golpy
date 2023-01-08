# big_questions.py



import game
import manipulation as gam

def get_exit_criteria(configuration, max_runs):
    """Prüft die Spielklasse für eine Anfangskonfiguration.

    Args:
        configuration (Tuple): Die Anfangskonfiguration
        max_runs (int): Die maximale Anzahl Spielzüge, die erlaubt ist bevor abgebrochen wird.

    Returns:
        str: Die Spielklasse, also 'survival', 'extinct', 'stable', 'oscillator', 'spaceship'
    """    
    generations, exit_criteria, periodicity, runs = game.play_full_game(configuration, max_runs)
    return exit_criteria


def is_contained(start_configuration, configuration_to_compare, max_runs = 100):
    """Prüft, ob die configuration_to_compare im Spielverlauf der start_configuration vorkommt.

    Args:
        start_configuration (Tuple): Die Startkonfiguration für das Spiel
        configuration_to_compare (Tuple): Die Konfiguration, auf die geprüft wird.
        max_runs (int, optional): Die maximale Anzahl von Spielzügen, die auf start_configuration gespielt wird. Defaults to 100.

    Returns:
        bool: True falls configuration_to_compare im Spielverlauf von start_configuration enthalten ist. Sonst False.
    """    
    generations, exit_criteria, periodicity, runs = game.play_full_game(start_configuration, max_runs)

    generation_ints = set(map(lambda config: gam._convert_to_int(config)[2], generations))

    affine_configuration_int_set = gam.get_configuration_variations(configuration_to_compare)
    
    matches = generation_ints & affine_configuration_int_set
    
    return len(matches) > 0
    