#Conditional Statments, Logical Operators, Code Blocks and Scope


#  if/else
#  if condition:
#     do this
#  else:
#    do this

height = float(input("What is your height: "))
bill = 0;
if (height>1.20):
    print("You can ride!")
    age = int(input("How old are you?: "))
    if (age<=12):
        bill = 5
        print("Child tickets are $5")
    elif (age<=18):
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want to have a photo take? Tyoe y for Yes and n for No")
    if (wants_photo=="y"):
        bill+=3

    print(f"Your final bill is {bill}")
else:
    print("You can't ride")

print("Welcome to Python Pizza Deliveries!\n")

size = input("What size do you want your pizza? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizaa? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size=="S":
    bill += 15    
elif size=="M":
    bill += 20
else: 
    bill += 25   

if pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if extra_cheese == "Y":
    bill+=1
print(f"Your final bill ares {bill}")
