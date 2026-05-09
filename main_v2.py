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
