import run_simulation as sim
import csv



def predict_exit_criteria(gameboard_int):
    #TODO wie hier file öffnen?
    csv_file = csv.reader(open('simulation_results_4_4.csv','w'), delimiter=',')
    
    for row in csv_file:
        if gameboard_int == row[0]:
            return row
    exit_criteria = row[2]

    return exit_criteria

def check_gb_origin(gameboard_int, gameboard_to_compare):
    #TODO extra file um alle generation von allen gameboards abzuspeichern
    csv_file = csv.reader(open('generations_of_gameboards.csv','w'), delimiter=',')
    for row in csv_file:
        if gameboard_to_compare == row[0]:
            return row

    for element in row:
        if gameboard_int == element:
            number = row.index(element)
            return 'Yes', number
        
        else: 
            return 'No'