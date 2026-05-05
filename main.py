dict = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
def get_board(spot, player, dict):  

    for key in dict:
        if key == spot:
            dict[key] = player
  
    print(f" {dict[1]} | {dict[2]} | {dict[3]}")
    print("---+---+---")
    print(f" {dict[4]} | {dict[5]} | {dict[6]}")
    print("---+---+---")
    print(f" {dict[7]} | {dict[8]} | {dict[9]}")

    return dict

dyc = get_board(5, 'X', dict)
get_board(4, "O", dyc)

#i am able to print a board and also place my players in the squares. A board is reusable, permitting the game to continue.
 


