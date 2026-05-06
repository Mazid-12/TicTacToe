dict = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

def get_board(dict):  
    print(f" {dict[1]} | {dict[2]} | {dict[3]}")
    print("---+---+---")
    print(f" {dict[4]} | {dict[5]} | {dict[6]}")
    print("---+---+---")
    print(f" {dict[7]} | {dict[8]} | {dict[9]}")

def place_piece(player, dictionary, choice):
    for key in dictionary:
        if key == int(choice):
            dictionary[key] = player
    new_dictionary = dictionary

    return new_dictionary

def check_win(dict):
    if dict[1] == dict[2] == dict[3] != " " or dict[1] == dict[4] == dict[7] != " " or dict[1] == dict[5] == dict[9]!= " " or dict[3] == dict[5] == dict[9] != " " or dict[7] == dict[8] == dict[9] != " " or dict[3] == dict[5] == dict[7] != " ":
        return True
def check_turns(dict):

    for player in ['X', 'O']:
        player_choice = input(f'Player {player} Enter your choice: ')
        new_dict = place_piece(player, dict, player_choice)
        get_board(new_dict)
        dict = new_dict
    
    return dict

dyc = check_turns(dict)


    