import os
os.system("cls")
personas = {}
def add_persona():
    """Esta funcion añade una persona a la subasta"""  ## Esta linea es una Docstring que sirve para indicar o descibir lo que hace una funcion
    action = False
    while not action:
        resp=input(("Deseas agregar a una persona?: Y, N: ")).lower()
        if resp == "y":
            nombre = input("Como te llamas?: ")
            dinero = float(input("Cuanto quieres ofrecer?: $"))
            personas[nombre]=dinero
            os.system("cls")
        elif resp == "n":
            print("Analizando Resultados.....")
            break;
        else:
            print("Opcion no valida, intenta de nuevo")
    return personas

def ganador(diccionario):
    participante_ganador = 0
    nombre_ganador = ""
    for i in diccionario:
        if diccionario[i]>participante_ganador:
            participante_ganador=diccionario[i]
            nombre_ganador = i
    return nombre_ganador,participante_ganador

diccionario_participantes=add_persona()
nombre,puntuacion = ganador(diccionario_participantes)
print(f"El ganador es: {nombre} con una aportacion de: ${puntuacion}")
