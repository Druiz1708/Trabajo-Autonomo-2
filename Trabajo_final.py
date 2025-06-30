# Importa la librería random para que la computadora pueda elegir entre piedra, papel o tijera
import random
# Importa os para poder limpiar la pantalla según el sistema operativo
import os
 # Permite ocultar lo que escribe el segundo jugador (modo multijugador)
from getpass import getpass

# Función para limpiar la pantalla dependiendo del sistema operativo
def limpiar():
    # cls para Windows, clear para Unix/Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


# Bucle principal del menú del juego
while True:
    print("¡Bienvenido al juego Piedra 🪨, Papel 📄 o Tijera ✂️!")
    print("Elige el modo de juego:")
    print("1) Jugar contra la computadora")
    print("2) Jugar multijugador")
    print("3) Salir")

    # Se solicita al usuario que elija una opción
    opcion = input("Ingresa la opción que decidiste (1, 2 o 3): ")
    # Limpia la pantalla
    limpiar()

    # Modo 1: Jugador contra la computadora
    if opcion == "1":
        # Se pide el nombre del jugador
        nombre = input("Ingresa tu nombre para comenzar a jugar: ")
        # Inicializa los puntos del jugador
        puntos_jugador = 0
        # Inicializa los puntos de la computadora
        puntos_pc = 0
        # Inicializa el contador de empates
        empates = 0

        # Bucle para repetir rondas
        while True:
            print("Opciones: piedra 🪨, papel 📄, tijera ✂️ (o escribe 'salir' para terminar)")
            # El jugador ingresa su jugada
            jugador = input("Tu jugada: ").lower()
            limpiar()

            # Si escribe salir, se termina este modo de juego
            if jugador == "salir":
                print("Saliendo del modo contra computadora")
                break

            # Jugadas válidas
            opciones = ["piedra", "papel", "tijera"]
            if jugador not in opciones:
                print("Opción no válida. Intenta de nuevo.")
                # Vuelve a pedir la jugada
                continue
 
            # La computadora elige una jugada al azar
            computadora = random.choice(opciones)

            # Se comparan las jugadas usando una estructura clara y humana
            if jugador == computadora:
                print("Usuario:", jugador)
                print("Computadora:", computadora)
                print("¡Empate!")
                empates += 1
            elif jugador == "piedra":
                if computadora == "tijera":
                    print("Usuario:", jugador)
                    print("Computadora:", computadora)
                    print("¡Felicidades! ¡Ganaste!")
                    puntos_jugador += 1
                elif computadora == "papel":
                    print("Usuario:", jugador)
                    print("Computadora:", computadora)
                    print("Perdiste, ¡Inténtalo de nuevo!")
                    puntos_pc += 1
            elif jugador == "papel":
                if computadora == "piedra":
                    print("Usuario:", jugador)
                    print("Computadora:", computadora)
                    print("¡Felicidades! ¡Ganaste!")
                    puntos_jugador += 1
                elif computadora == "tijera":
                    print("Usuario:", jugador)
                    print("Computadora:", computadora)
                    print("Perdiste, ¡Inténtalo de nuevo!")
                    puntos_pc += 1
            elif jugador == "tijera":
                if computadora == "papel":
                    print("Usuario:", jugador)
                    print("Computadora:", computadora)
                    print("¡Felicidades! ¡Ganaste!")
                    puntos_jugador += 1
                elif computadora == "piedra":
                    print("Usuario:", jugador)
                    print("Computadora:", computadora)
                    print("Perdiste, ¡Inténtalo de nuevo!")
                    puntos_pc += 1

            # Mostrar puntajes actuales
            print(f"{nombre}: {puntos_jugador} | Computadora: {puntos_pc} | Empates: {empates}")

            # Preguntar si desea continuar o volver al menú
            while True:
                continuar = input("¿Quieres volver a jugar? (si/no/menu): ").lower()
                if continuar == "no":
                    print("¡Gracias por jugar! ¡Hasta la próxima!")
                    exit()
                elif continuar == "menu":
                    print("Volviendo al menú principal...")
                    break
                elif continuar == "si":
                    limpiar()
                    break
                else:
                    print("Opción no válida. Escribe solo: si, no o menu.")

            if continuar == "menu":
                # Sale al menú principal
                break

    # Modo 2: Jugador vs Jugador (multijugador local)
    elif opcion == "2":
        print("Modo multijugador activado.")
        jugador1 = input("Nombre del Jugador 1: ")
        jugador2 = input("Nombre del Jugador 2: ")
        puntos1 = 0
        puntos2 = 0
        empates = 0

        while True:
            print("Opciones disponibles: piedra 🪨, papel 📄 o tijera ✂️")
            # Entrada oculta
            jugada1 = getpass(f"{jugador1}, escribe tu jugada: ").lower()
            jugada2 = getpass(f"{jugador2}, escribe tu jugada: ").lower()
            limpiar()

            opciones = ["piedra", "papel", "tijera"]
            if jugada1 not in opciones or jugada2 not in opciones:
                print("Una o ambas jugadas no son válidas. Inténtelo de nuevo.")
                continue

            # Evaluación de las jugadas
            if jugada1 == jugada2:
                print("Usuario:", jugada1)
                print("Usuario:", jugada2)
                print("¡Empate!")
                empates += 1
            elif jugada1 == "piedra":
                if jugada2 == "tijera":
                    print("Usuario:", jugada1)
                    print("Usuario:", jugada2)
                    print(f"¡{jugador1} gana esta ronda!")
                    puntos1 += 1
                elif jugada2 == "papel":
                    print("Usuario:", jugada1)
                    print("Usuario:", jugada2)
                    print(f"¡{jugador2} gana esta ronda!")
                    puntos2 += 1
            elif jugada1 == "papel":
                if jugada2 == "piedra":
                    print("Usuario:", jugada1)
                    print("Usuario:", jugada2)
                    print(f"¡{jugador1} gana esta ronda!")
                    puntos1 += 1
                elif jugada2 == "tijera":
                    print("Usuario:", jugada1)
                    print("Usuario:", jugada2)
                    print(f"¡{jugador2} gana esta ronda!")
                    puntos2 += 1
            elif jugada1 == "tijera":
                if jugada2 == "papel":
                    print("Usuario:", jugada1)
                    print("Usuario:", jugada2)
                    print(f"¡{jugador1} gana esta ronda!")
                    puntos1 += 1
                elif jugada2 == "piedra":
                    print("Usuario:", jugada1)
                    print("Usuario:", jugada2)
                    print(f"¡{jugador2} gana esta ronda!")
                    puntos2 += 1

            # Mostrar puntuaciones actuales
            print(f"{jugador1}: {puntos1} | {jugador2}: {puntos2} | Empates: {empates}")

            # Preguntar si desean continuar o volver al menú
            while True:
                seguir = input("¿Quieren volver a jugar? (si/no/menu): ").lower()
                if seguir == "no":
                    print("¡Gracias por jugar! ¡Hasta la próxima!")
                    exit()
                elif seguir == "menu":
                    print("Volviendo al menú principal...")
                    break
                elif seguir == "si":
                    limpiar()
                    break
                else:
                    print("Opción no válida. Escribe solo: si, no o menu.")

            if seguir == "menu":
                # Regresa al menú principal
                break

    # Modo 3: Salir del juego completamente
    elif opcion == "3":
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        break
    # Si se introduce una opción inválida desde el menú
    else:
        print("Opción no válida. Por favor, escoge entre 1, 2 o 3.")