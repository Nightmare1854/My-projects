import random

def roll_dice() :

    start = 1
    stop = 6
    roll = random.randint(start,stop)

    return roll

while True:
    players_count = input("Enter number of Players(2-4) : ")
    if players_count.isdigit():
        players_count = int(players_count)
        if 2 <= players_count <= 4:
            break
        else:
            print("Must be betwee 2 to 4")
    else:
        print("Invalid, try again!")

max_score = 20
player_score = [0 for i in range(players_count)]

while max(player_score) < max_score:

    for player_index in range(players_count):

        print("\nPlayer ",player_index+1," turn has started!!!")
        print("Your total score is : ",player_score[player_index], "\n")
        current_score = 0

        while True:

            roll_qn = input("Would like to roll (yes) or (no) ? : ")
            if (roll_qn.lower() != "y"):
                break
            
            value = roll_dice()
            if value == 1:
                print("Oops!!! It's a One, your score is reset to Zero.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a : ",value)
                
            print("Your current score is : ",current_score)
        player_score[player_index] += current_score
        print("Your total score is : ",player_score[player_index])

max_score = max(player_score)
winner_idx = player_score.index(max_score)
print("Player ", winner_idx+1 , " is the winner with score of ",max_score)