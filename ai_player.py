import random

def play_ai(dict, setX, setAI):
    first_choice = forsee_win(dict, setX)
    second_choice = forsee_win(dict, setAI)
    #print(first_choice)
    #print(second_choice)
    if second_choice != False:
        return second_choice
    if first_choice != False:
        return first_choice
    else:
        choice_list = []
        for key in dict:
            if dict[key] == ' ':
                choice_list.append(key)
        choice = random.choice(choice_list)
        return choice

def move_ai(dict, player, setX, setAI):
    old_list = []
    gap_spots = create_gap(dict, setX, player)
    print(gap_spots)
    for key in dict:
        if dict[key] == player:
            old_list.append(key)
    new_spot = play_ai(dict, setX, setAI)    
    if gap_spots != False:
        for spot in gap_spots:
            old_list.remove(spot)
        print(old_list)
        old_spot = random.choice(old_list)
    else:
        old_spot = random.choice(old_list)

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

def create_gap(dict, setX, player):
    win_combo = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {3, 5, 7}, {2, 5, 8}, {3, 6, 9}, {4, 5, 6}, {7, 8, 9}]
    danger_spots = []
    for win_set in win_combo:
        common_set = win_set.intersection(setX)
        if len(common_set) == 2:
            for spot in common_set:
                print(spot)
                win_set.remove(spot)
            danger_spot = win_set.pop()
            if dict[danger_spot] == player:
                danger_spots.append(danger_spot)
    if len(danger_spots) == 0:
        return False
    else:
        return danger_spots