import configparser
import sys

# open yaml file
def get_turn_orders(filepath):
    config = configparser.ConfigParser()
    config.read(filepath)
    return config

def process_moves(moves_dict):
    # get the player current coords
    # calculate new seen tiles
    # add to player 
    for move in moves_dict:
        print('Found move action: ' + str(move) + ' = ' + moves_dict[move])

    pass

if __name__ == "__main__":
    turn = get_turn_orders(sys.argv[1])
    print(turn.sections())
    
    process_moves(turn['MOVEMENT'])
