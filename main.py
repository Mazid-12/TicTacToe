dict = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
def get_board(dict):  
    print(f" {dict[1]} | {dict[2]} | {dict[3]}")
    print("---+---+---")
    print(f" {dict[4]} | {dict[5]} | {dict[6]}")
    print("---+---+---")
    print(f" {dict[7]} | {dict[8]} | {dict[9]}")

def play_aturn(player, dictionary):
    player_choice = input('Enter your choice: ')
    for key in dictionary:
        if key == int(player_choice):
            dictionary[key] = player
    new_dictionary = dictionary

    return new_dictionary

dyc = play_aturn('O', dict)
get_board(dyc)



    