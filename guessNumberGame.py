import random
generate_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
ans = input(("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
opns = 0
print(f"Numero generado: {generate_number}")
if ans == 'hard':
    print("You have 5 attempts reamining to guess the number")
    while opns<=4:
        opns +=1
        user_number = int(input("Make a guees: "))
        if user_number == generate_number:
            print(f"Congratulations! You guessed the number {generate_number} correctly!")
            break
        else:
            difference = abs(user_number-generate_number)
            if user_number > generate_number:
                if difference > 10:
                    print("Too high!")
                else:
                    print("A little high")
            elif user_number < generate_number:
                if difference >10:
                    print("Too low!")
                else:
                    print("A little low")
        if opns > 4:
            print("You Lose!")
elif ans == 'easy':
    print("You have 10 attempts reamining to guess the number")
    while opns <=9:
        opns+=1
        user_number = int(input("Make a guees: "))
        if user_number == generate_number:
            print(f"Congratulations! You guessed the number {generate_number} correctly!")
            break
        else:
            difference = abs(user_number-generate_number)
            if user_number > generate_number:
                if difference > 10:
                    print("Too high!")
                else:
                    print("A little high")
            elif user_number < generate_number:
                if difference >10:
                    print("Too low!")
                else:
                    print("A little low")
        if opns > 9:
            print("You Lose!")
else: 
    print("Try again!")