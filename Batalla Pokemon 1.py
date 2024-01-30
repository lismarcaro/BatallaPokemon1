#Batalla pokemon

import random #para RandRage (elegir ataque oponente)

PS_Jugador = 100 #Puntos de Salud
PS_Oponente = 100
Defensa_Oponente = 100
Defensa_Jugador = 100
ataque_oponente = random.randrange (1,5)

Ataques = ["latigo", "placaje", "Pistola de agua", "ascuas", "malicioso"]
#Lista de ataques

while PS_Jugador > 0 and PS_Oponente > 0:
    print("Escoje tu nuevo ataque")
    print("Los ataques son: latigo, placaje, pistola de agua, ascuas y malicioso")
    ataque_jugador = input("ataque: ")

    if ataque_jugador == "malicioso":
        Defensa_Oponente = Defensa_Oponente - 10
        print("Tu ataque es: ")
        print(Ataques[4])

    if ataque_jugador == "latigo": #latigo
        print("Tu ataque es: ")
        print(Ataques[0])

        if Defensa_Oponente <= 0:
            Defensa_Oponente = 1
    elif ataque_jugador == "placaje":
        print("Tu ataque es: ")
        print(Ataques[1])
        PS_Oponente -= 35 * (100/Defensa_Oponente)

    elif ataque_jugador == "pistola de agua": #Pistola de agua
        print("Tu ataque es: ")
        print(Ataques[2])

    elif ataque_jugador == "ascuas":
        print("Tu ataque es: ")
        print(Ataques[3])
        pass


        #Turno del Oponente, se define con un Random

    
    if ataque_oponente == 1: #latigo
        print("El ataque de tu oponente es: ")
        print(Ataques[0])
        

        Defensa_Oponente -= 10
        if Defensa_Oponente <= 0:
            Defensa_Oponente = 1

    elif ataque_oponente == 2: #placaje
        print("El ataque de tu oponente es: ")
        print(Ataques[1])
        PS_Oponente -= 35 * (100/Defensa_Oponente)

        
    elif ataque_oponente == 3: #Pistola de agua
        print("El ataque de tu oponente es: ")
        print(Ataques[2])

    elif ataque_oponente == 4: #ascuas
        print("El ataque de tu oponente es: ")
        print(Ataques[3])
        pass

    elif ataque_oponente == 5: #malicioso
        Defensa_Oponente = Defensa_Oponente - 10
        print("El ataque de tu oponente es: ")
        print(Ataques[4])
      
    
    else:
        print("¿¡QUE HACES!? Tus ataques son malicioso, placaje y ascuas")
        continue
        PS_Jugador -=40
   


#Si términa el ciclo, alguien ganó
if PS_Oponente <= 0 and PS_Jugador <= 0:
    print("EMPATE")
elif PS_Oponente <= 0: #el jugador es >0
    print("PERDISTE")
