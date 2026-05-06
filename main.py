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
    if dict[1] == dict[2] == dict[3] != ' ' or dict[1] == dict[4] == dict[7] != ' ' or dict[1] == dict[5] == dict[9]!= ' ' or dict[3] == dict[5] == dict[9] != ' ' or dict[7] == dict[8] == dict[9] != ' ' or dict[3] == dict[5] == dict[7] != ' ':
        return True
    else:
        return False
    
def play_round(dict, player):
    #for player in ['X', 'O']:
    player_choice = input(f'Player {player} Enter your choice: ')
    new_dict = place_piece(player, dict, player_choice)
    get_board(new_dict)
    dict = new_dict
    
    return dict


def continue_play(dict):
    #print(type(dict[1]))
    win = check_win(dict)
    #print(win)
    while win == False:
        for player in ['X', 'O']:
            new_dict = play_round(dict, player)
            print(new_dict)
        win = check_win(new_dict)
        #print(win)

    else:
        print('You win!')
    
continue_play(dict)
        
'''def pos(val1, val2):
    if val1 == val2 != ' ' or val1 == 4 != ' ':
        return True
res = pos(4, 4)
print(res)'''
    