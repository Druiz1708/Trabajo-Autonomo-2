#Importé la libreria random para que la computadora pueda elegir al azar entre piedra, papel o tijera
import random
#Coloque un mensaje de bienvenida al usuario
mensaje= ("Bienvenido")
print(mensaje)
#Opciones válidas para el juego
opciones = ("piedra", "papel", "tijera")
#Bucle principal del juego para que este se va a repita las veces que el jugador quiera seguir jugando 
while True:
    #Variable para que la computadora elija una opción al azar
    computadora= (random.choice(opciones))
    #Variable para almacenar la elección del usuario
    usuario= None
    #Bucle para garantizar que el usuario elija una opción valida
    while usuario not in opciones:
        usuario = input ("Escoge: piedra, papel, tijera:").lower()
        #Condiciones para comparar elecciones del usuario y el computador; y en base a esto se determina el resultado
        if usuario==computadora:
            print("Usuario: ", usuario)
            print("Computadora: ", computadora)
            print("¡Empate!")
        elif usuario == "piedra":
            if computadora == "tijera":
                print("Usuario:", usuario)
                print("Computadora:", computadora)
                print("¡Felicidades! ¡Ganaste!")
            elif computadora == "papel": 
                print("Usuario:", usuario)
                print("Computadora:", computadora)
                print("Perdiste, ¡Intentalo de nuevo!")   
        elif usuario == "papel":
            if computadora == "piedra": 
               print("Usuario:", usuario)
               print("Computadora:", computadora)
               print("Perdiste, ¡Intentalo de nuevo!")
            elif computadora == "tijera": 
               print("Usuario:", usuario)
               print("Computadora:", computadora)
               print("¡Felicidades! ¡Ganaste!")  
        elif usuario == "tijera":
            if computadora == "piedra": 
               print("Usuario:", usuario)
               print("Computadora:", computadora)
               print("¡Felicidades! ¡Ganaste!")
            elif computadora == "papel": 
               print("Usuario:", usuario)
               print("Computadora:", computadora)
               print("Perdiste, ¡Intentalo de nuevo!")
        while True:
         #Preguntar al usuario si quiere volver a jugar
          usuario_reinicio= input("¿Quieres volver a jugar? si, no:").lower()
         #Si el usuario elige que no, se termina el juego
          if  usuario_reinicio == "si":
           print("Jugar de nuevo")
           break
        #Si el usuario elige que si, se reincinia el bucle 
          elif usuario_reinicio == "no":
            print("Gracias por jugar")
            exit ()
          else: 
             print("Opción no valida") 
             continue
