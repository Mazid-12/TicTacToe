dict = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

def get_board(dict):  
    print(f" {dict[1]} | {dict[2]} | {dict[3]}")
    print("---+---+---")
    print(f" {dict[4]} | {dict[5]} | {dict[6]}")
    print("---+---+---")
    print(f" {dict[7]} | {dict[8]} | {dict[9]}")

def check_win(dict):
    if dict[1] == dict[2] == dict[3] != ' ' or dict[1] == dict[4] == dict[7] != ' ' or dict[1] == dict[5] == dict[9]!= ' ' or dict[3] == dict[5] == dict[7] != ' ' or dict[7] == dict[8] == dict[9] != ' ' or dict[3] == dict[6] == dict[9] != ' ' or dict[4] == dict[5] == dict[6] != ' ' or dict[2] == dict[5] == dict[8] != ' ':
        return True
    else:
        return False
    
def play_round(dict, player):
#for player in ['X', 'O']:
    while True:
        try:
            player_choice = int(input(f'Player {player} Enter your choice (1-9): '))
            if player_choice <= 9 and player_choice >= 1:
                #new_dict = place_piece(player, dict, player_choice)  

                
                    if dict[player_choice] == ' ':
                        dict[player_choice] = player
                        get_board(dict)
                        return dict
                    else:
                        print('This spot is occupied!')         
            else:
                print('Only integers from 1 to 9')
        except ValueError:
            print('Only integer allowed!') 
            
def continue_play(dict):
    win = check_win(dict)
    for round in range(3):
        for player in ['X', 'O']:
            new_dict = play_round(dict, player)
            #print(new_dict)
            win = check_win(new_dict)
            print(win)
            if win == True:
                return f'Player {player}, you win!'
    else:          
        print('ok, time to move markers!')
        for round in range(10):
            for player in ['X', 'O']:
                new_dict = move_marker(dict, player)
                win = check_win(new_dict)
                if win == True:
                    return f'Player {player}, you win!'
                
def move_marker(dict, player):
    while True:
        try:
            old_spot = int(input(f'Player {player} Where is the marker you want to move: '))
            new_spot = int(input(f'Player {player} Where do you want to move it to: '))

            if old_spot >=1 and old_spot <= 9 and new_spot >=1 and old_spot <= 9:
                    
                    if dict[old_spot] == player and dict[new_spot] == ' ':
                        dict[old_spot] = " "
                        dict[new_spot] = player
                        get_board(dict)
                        return dict            
                    else:
                        print('There is mistake in your choices')
            else:
                print('Only integers from 1 to 9')
        except ValueError:
            print ('Only integers allowed!')
            
print(continue_play(dict))