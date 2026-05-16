import random

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
