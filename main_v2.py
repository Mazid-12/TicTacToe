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
    
def validate_input(dict, player_input):
    try:
        input = int(player_input)
        if input <=9 and input>= 1:
            return True
        else: 
            return False
    except ValueError:
        return False
def main():
    board_dictionary = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    input("Press ENTER to start the game.")

    for round in range(3):
        for player in ['O', 'X']:
            while True:
                player_choice = int(input(f'Player {player} Enter your choice (1-9): '))
                is_valid = validate_input(player_choice)
                if not is_valid:
                    ('The input is invalid!')
                if board_dictionary[player_choice] == ' ':
                    board_dictionary[player_choice] = player
                    print_board(board_dictionary)
                    has_won = check_win(board_dictionary)
                    if has_won:
                        return f'Game Over! Player {player} won!'
        else:
            return "It's a draw"
    
                    

