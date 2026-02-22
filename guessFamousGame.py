import random
ig_users = {
    "Justin Biber": [294000000,"He is a famous pop singer"],
    "Jude Bellingam": [38300000,"He is a Real Madrid player, and he is very awesome"],
    "Santiago Giménez":[1600000,"He is a Feyenord player, and he is a mexican fotbal player"],
    "Vini Jr": [52700000,"He is the best fotball player of the world, he is Real Madrid player"],
    "System of a Down": [4400000,"They're the best rock band of all time"]
}
 
#Podemos convertir el diccionario a una lista para asi poder acceder de forma aleatoria a sus datos:
# random_data = random.choice(list(diccionary_name.key()))
#recordando que random.choice devuelve un dato aleatorio de una lista en forma de cadena de texto
def random_user_ob(ig_users):
    for random_user_ig in random.sample(list(ig_users.keys()),2):
        user_data = ig_users[random_user_ig]
        return random_user_ig,user_data
    
def most_followes(list_A,List_B):
    if list_A[1][0]>List_B[1][0]:
        return "A",list_A
    else:
        return "B", List_B

score = 0
while True:
    usuario_1,data_1 = random_user_ob(ig_users)
    print(f"A. {usuario_1}: {str(data_1[1])}")
    A = [usuario_1,data_1]
    usuario_2, data_2 = random_user_ob(ig_users)
    while usuario_1 == usuario_2: 
        usuario_2, data_2 = random_user_ob(ig_users)
    print("Vs")
    print(f"B. {usuario_2}: {str(data_2[1])}")
    B = [usuario_2,data_2]
    user_win,winer_data = most_followes(A,B)
    ans = input("Who has more followers? Type A or B:   ").upper()
    if ans == user_win:
        score += 1
        print(f"Correctly, {winer_data[0]}: {winer_data[1][1]} and he has {winer_data[1][0]} followers")
    else:
        print(f"You Lose!, Your fina score is: {score}")
        break
