import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","v","u","w","x","y","z","A","B","C","D","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","*","+","{","}","_","-","$","%","&","/","#","(",")","=","?","¿"]
password = []
print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

counter1 = 0
for letras in letters:
    counter1+=1
    if nr_letters>=counter1:
        password.extend(random.choices(letters))
    
counter2 = 0
for simbolos in symbols:
    counter2+=1
    if nr_symbols>=counter2:
        password.extend((random.choices(symbols)))

counter3 = 0
for numeros in numbers:
    counter3+=1
    if nr_numbers>=counter3:
        password.extend((random.choices(numbers)))

random.shuffle(password) #modifica la lista original de manera aleatoria
# contrasena_aleatoria = random.sample(password, leng(password)) --> genera un nuevo orden aleatorio sin modificar el orden original de la lista
psw = ""
for char in password:
    psw += char

print(f"Your password is: {psw}")