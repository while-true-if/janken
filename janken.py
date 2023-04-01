import random

def argmax(l):
    max_num = l[0]
    max_indexes = []
    for i, value in enumerate(l):
        if value == max_num:
            max_indexes.append(i)
        elif max_num < value:
            max_num = value
            max_indexes = [i]
    return max_indexes

def input_int(text, l):
    num = 0
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print("Please enter a number.")
            continue
        if not num in l:
            print("The number isn't what I want. Please enter again.")
            continue
        break
    return num

computer_score, player_score = 0, 0
computer_set, player_set = 0, 0

num_of_times_player_hand = [0, 0, 0]

computer_name = input("Please enter CPU's name.\n>>> ")
player_name = input("Please enter your name.\n>>> ")

while True:
    prediction = random.choice(argmax(num_of_times_player_hand))
    computer_hand = prediction + 1 if prediction < 2 else 0
    player_hand = input_int("ROCK:0, PAPER:1, SCISSORS:2\n>>> ", range(3))
    num_of_times_player_hand[player_hand] += 1

    if player_hand == computer_hand:
        player_score += 1
        computer_score += 1
        print("引き分け")
    elif player_hand + 1 if player_hand < 2 else 0 == computer_hand:
        computer_score += 1
        print("負け")
    else:
        player_score += 1
        print("勝ち")
    print(f"{computer_name} {computer_score}  -  {player_score} {player_name}")

    if 2 <= abs(player_score - computer_score) and 25 <= max(player_score, computer_score):
        if computer_score < player_score:
            player_set += 1
            print("このセットで勝利")
        else:
            computer_set += 1
            print("このセットで敗北")
        computer_score, player_score = 0, 0

    if 2 <= max(player_set, computer_set):
        if computer_set < player_set:
            print("このゲームで勝利")
        else:
            print("このゲームで敗北")
        break