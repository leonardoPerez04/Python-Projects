import random
game = ["Rock","Paper","Scissors"]
user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
random_number = random.choice(game)
if (user_number != 0 and user_number !=1 and user_number!=2):
    print("Game Over!")
else:
    print(f"User: {game[user_number]}")
    print(f"Computer: {random_number}")
    if(game[user_number]=="Rock" and random_number=="Paper"):
        print("You Win!")
    elif (game[user_number]=="Rock" and random_number=="Scissors"):
        print("You Win!")
    elif (game[user_number]=="Paper" and random_number=="Rock"):
        print("You Win!")
    elif (game[user_number]=="Scissors" and random_number=="Paper"):
        print("You Win!")
    elif (game[user_number]==random_number):
        print("Draw")
    else:
        print("You Lose!")