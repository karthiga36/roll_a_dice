import random


def roll():
    minval = 1
    maxval = 6

    roll = random.randint(minval, maxval)
    return roll


while True:
    players = input("enter no of players (2-4):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("must be between 2 to 4 players")
    else:
        print("invalid try again")


maxscore = 50
player_score = [0 for _ in range(players)]

while max(player_score) < maxscore:

    for playerind in range(players):
        print("\n Player number", playerind+1, "turn has just started")

        print("\n your total score is:", player_score[playerind]+1)

        currentscore = 0

        while True:

            rollyn = input("Would you like to roll (Y)?")
            if rollyn.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("your turn finish because u rolled 1")
                currentscore = 0
                break

            else:
                print("you rolled a:", value)
                currentscore += value

            print("your score is:", currentscore)

        player_score[playerind] += currentscore
        print("your total score is ", player_score[playerind])

maxscore = max(player_score)
winner = player_score.index(maxscore)

print("the winner is", winner + 1, "with a score:", maxscore)
