#Lists 
#list_name.append("###")  sirve para agregar cosas al final de una lista
#list_name.extend("###","###","###"..."###")  sirve para agregar muchas cosas al final de la lista
import random
friends = ["Alice","Bob","Charlie","David","Emanuel"]
length = len(friends)
random_number = random.randint(0,length-1)
print(f"Le tocó a: {friends[random_number]}")

#otra forma es utilzando la funcion random.choices, que decuelve un dato aleatorio de la lista
print(f"\nLe toca a: {random.choices(friends)}")
print("\n##############")
fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits,vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])