# #Randomisation and Python Lists
import random
# #random.randit(a,b) Return a random integer N such that a<=N<=b
# numero_aleatorio=(random.randint(1,5))
# print(numero_aleatorio)

# random_number = random.random() # 0<=N<=1.0
# print(random_number)

# random_float = random.uniform(1,10)
# print(random_float)

heads_tails = int(random.randint(0,1))

if heads_tails == 0:
    print("Heads")
else:
    print("Tails")