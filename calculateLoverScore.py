def calculate_lover_score(name1,name2):
    nombre = list((name1 + name2).upper())
    word = ['T','R','U','E']
    counter = 0
    for char in nombre:
        if char in word:
            counter += 1
    word_lover = ['L','O','V','E','R']
    counter_2 = 0
    for char in nombre:
        if char in word_lover:
            counter_2+=1
    print(str(counter)+str(counter_2))
calculate_lover_score("Leonardo","Luisa Fernanda")  