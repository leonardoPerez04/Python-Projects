print("Hello "+ input("What is your name?")+"!") #primero ejecuta "input" para completar la cadena, posteriormente ejecuta el "print" con la cadena completa
name = input("What is your name?")
print(name)
print(len(name))
#print(len(input("What is your name")))
username = input("What is your name")
length = len(username)
print("The name is "+username+" and its length is "+str(length))
glass1 = "milk"
glass2 = "juice"
glass3 = glass1
glass1 = glass2
glass2 = glass3

print(glass1+" "+glass2)  
name_of_the_city = input("What's the name of the city you grew up in?\n")
petname = input("What's your pet's name?\n")
print("Your band name could be "+name_of_the_city+" "+petname)