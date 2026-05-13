import random
def print_board(dict):  
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

def validate_input(player_input):
    try:
        input = int(player_input)
        if input <=9 and input>= 1:
            return True
        else: 
            return False
    except ValueError:
        return False

def place_marker(dict, player, choice):
    if dict[int(choice)] == ' ':
        dict[int(choice)] = player
        return dict
    else:
        return False
    
def move_marker(dict, player, old_spot, new_spot):
    if dict[new_spot] == ' ':
        dict[old_spot] = ' '
        dict[new_spot] = player
        return dict
    else:
        return False
    

def play_ai(dict):
    choice_list = []
    for key in dict:
        if dict[key] == ' ':
            choice_list.append(key)
    choice = random.choice(choice_list)
    return choice
    
def main():
        board_dictionary = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
        print_board(board_dictionary)
        for round in range(3):
            for player in ['X', 'O']:
                while True:
                    player_choice = input(f'Player {player} Enter your choice (1-9): ')
                    is_valid = validate_input(player_choice)
                    if not is_valid:
                        print('The input is invalid!')
                        continue
                    new_dictionary = place_marker(board_dictionary, player, player_choice)
                    if new_dictionary != False:
                        print_board(new_dictionary)
                        has_won = check_win(new_dictionary)
                        if has_won:
                            return f'Game Over! Player {player} won!'
                        break
                    else:
                       print('This spot is occupied!')                   
        else:          
            for round in range(3):
                for player in ['X', 'O']:
                    while True:
                        old_spot = int(input(f'Player {player} Where is the marker you want to move: '))
                        new_spot = int(input(f'Player {player} Where do you want to move it to: '))
                        old_isvalid = validate_input(old_spot)
                        new_isvalid = validate_input(new_spot)
                        if not old_isvalid and not new_isvalid:
                            print('The input is invalid!')
                            continue
                        if board_dictionary[old_spot] != player:
                            print('The old spot is occupied by your opponent or empty')
                            continue
                        new_dictionary = move_marker(board_dictionary, player, old_spot, new_spot)
                        if new_dictionary != False:
                            print_board(board_dictionary)
                            has_won = check_win(board_dictionary)
                            if has_won:
                                return f'Game Over! Player {player} won!'        
                            break      
                        else:
                            print('The new spot is not empty')
            else:
                return f"Game Over! It's a draw"

while True:
    input("Press ENTER to start the game==")
    result = main()
    print(result)
    restart = input('Do you want to play again (0 to leave): ')
    if restart == '0':
        break