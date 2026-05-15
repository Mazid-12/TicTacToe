import random
import time 

def print_board(dict):  
    print(f" {dict[1]} | {dict[2]} | {dict[3]}")
    print("---+---+---")
    print(f" {dict[4]} | {dict[5]} | {dict[6]}")
    print("---+---+---")
    print(f" {dict[7]} | {dict[8]} | {dict[9]}")

def check_win(set):
    win_combo = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {3, 5, 7}, {2, 5, 8}, {3, 6, 9}, {4, 5, 6}, {7, 8, 9}]
    if set in win_combo:
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

def play_ai(dict, setO, setAI):
    first_choice = forsee_win(dict, setO)
    second_choice = forsee_win(dict, setAI)
    print(first_choice)
    print(second_choice)
    if first_choice != False:
        return first_choice
    if second_choice != False:
        return second_choice
    else:
        choice_list = []
        for key in dict:
            if dict[key] == ' ':
                choice_list.append(key)
        choice = random.choice(choice_list)
        return choice

def move_ai(dict, player):
    old_list = []
    new_list = []
    for key in dict:
        if dict[key] == player:
            old_list.append(key)
        if dict[key] == ' ':
            new_list.append(key)
    old_spot = random.choice(old_list)
    new_spot = random.choice(new_list)
    return old_spot, new_spot

def forsee_win(dict, set1):
    win_combo = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {3, 5, 7}, {2, 5, 8}, {3, 6, 9}, {4, 5, 6}, {7, 8, 9}]
    for sets in win_combo:
        common = sets.intersection(set1)
        if len(common) == 2:
            unique_set = sets - common
            spot = int(unique_set.pop())
            if dict[spot] == ' ':
                return spot
            else:
                continue
        else:
            continue
    return False

def main():
        board_dictionary = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
        marker_placeX = set()
        marker_placeY = set()
        print_board(board_dictionary)
        for round in range(3):
            for player in ['X', 'O']:
                while True:
                    if player == 'X':
                        player_choice = input(f'Player {player} Enter your choice (1-9): ')
                        is_valid = validate_input(player_choice)
                        if not is_valid:
                            print('The input is invalid!')
                            continue
                        marker_placeX.add(int(player_choice))
                        has_won = check_win(marker_placeX)
                    elif player == 'O':
                        print('Your Opponent is thinking...')
                        time.sleep(3)
                        player_choice = play_ai(board_dictionary, marker_placeX, marker_placeY)
                        marker_placeY.add(player_choice)
                        has_won = check_win(marker_placeY)
                    new_dictionary = place_marker(board_dictionary, player, player_choice)
                    if new_dictionary != False:
                        print_board(new_dictionary)
                        if has_won:
                                return f'Game Over! Player {player} won!'
                        break  
                    else:
                        print("The input is invalid")
                                 
        else:          
            for round in range(3):
                for player in ['X', 'O']:
                    while True:
                        if player == 'X':
                            old_spot = int(input(f'Player {player} Where is the marker you want to move: '))
                            new_spot = int(input(f'Player {player} Where do you want to move it to: '))
                            old_isvalid = validate_input(old_spot)
                            new_isvalid = validate_input(new_spot)
                            marker_placeX.remove(int(old_spot))
                            marker_placeX.add(int(new_spot))
                            has_won = check_win(marker_placeX)
                            if not old_isvalid and not new_isvalid:
                                print('The input is invalid!')
                                continue
                            if board_dictionary[old_spot] != player:
                                print('The old spot is occupied by your opponent or empty')
                                continue
                        elif player == 'O':
                            print('Your opponent is thinking...')
                            time.sleep(3)
                            choices = move_ai(board_dictionary, player)
                            old_spot = choices[0]
                            new_spot = choices[1]
                            marker_placeY.remove(old_spot)
                            marker_placeY.add(new_spot)
                            has_won = check_win(marker_placeY)
                        new_dictionary = move_marker(board_dictionary, player, old_spot, new_spot)
                        if new_dictionary != False:
                            print_board(board_dictionary)
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