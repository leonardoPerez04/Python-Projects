#Hangman
import random
def random_word():
    lista_palabras = ['Casa','Mesa','Silla','Computadora','Celular','Reloj','Collar','Planta','Arbol','Arbusto','Oso','Leon','Delfin','Tigre',
    'Elefante','Loro','Gato','Conejo']
    palabra = random.choice(lista_palabras)
    return palabra.lower()

def converir_palabra_guiones(palabra):
    return "_" * len(palabra)

list_ascii = [''' +---+

    |   |

    O   |

        |

        |

        |

  =========''','''

 

    +---+

    |   |

    O   |

    |   |

        |

        |

  =========''','''

 

    +---+

    |   |

    O   |

   /|   |

        |

        |

  =========''','''

 

    +---+

    |   |

    O   |

   /|\  |

        |

        |

  =========''','''

 

    +---+

    |   |

    O   |

   /|\  |

   /    |

        |

  =========''','''

 

    +---+

    |   |

    O   |

   /|\  |

   / \  |

        |

  =========''']

palabra_elegida = random_word()
palabra_con_guiones = converir_palabra_guiones(palabra_elegida)
print(palabra_elegida)
print(f"Tu palabra para adivinar es: {palabra_con_guiones}")

lista_palabra_sin_guiones = list(palabra_elegida)
lista_palabra_con_guiones = list(palabra_con_guiones)
longitud_palabra = len(lista_palabra_sin_guiones)
errores = 0
oportunidades = 20
while oportunidades>0:
    
    
    letra_usuario = input("Ingresa una letra: ")
    acierto = False
    for i in range(longitud_palabra):
        if letra_usuario == lista_palabra_sin_guiones[i]:
            lista_palabra_con_guiones[i] = lista_palabra_sin_guiones[i]
            acierto = True
    print("".join(lista_palabra_con_guiones))
    if not acierto:  
        errores += 1
        print(f"Fallaste. Errores: {errores}") 

    if errores == 1:
        print(list_ascii[0])
    if errores == 2:
        print(list_ascii[1])
    if errores == 3:
        print(list_ascii[2])
    if errores == 4:
        print(list_ascii[3])
    if errores == 5:
        print(list_ascii[4])
    if errores == 6:
        print(list_ascii[5])
        print("\n\n\t\t\t\t############### Has perdido!! ############")
        break
    if lista_palabra_con_guiones == lista_palabra_sin_guiones:
        print("\n\n\t\t\t\t############# Has ganado! ############")
        break
    oportunidades -= 1
    if oportunidades == 0:
        print("Te quedaste sin oportunidades. ¡Has perdido!")
