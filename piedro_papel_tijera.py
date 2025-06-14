import random
mensaje= ("Bienvenido")
print(mensaje)
opciones = ("piedra", "papel", "tijera")
while True:
    computadora= (random.choice(opciones))
    usuario= None
    while usuario not in opciones:
        usuario = input ("Escoge: piedra, papel, tijera:").lower()
        if usuario==computadora:
            print("Usuario: ", usuario)
            print("Computadora: ", computadora)
            print("¡Empate!")
        elif usuario == "piedra":
            if computadora == "tijera":
                print("Usuario", usuario)
                print("Computadora", computadora)
                print("¡Felicidades! ¡Ganaste!")
            elif computadora == "papel": 
                print("Usuario", usuario)
                print("Computadora", computadora)
                print("Perdiste, ¡Intentalo de nuevo!")   
        elif usuario == "papel":
            if computadora == "piedra": 
               print("Usuario", usuario)
               print("Computadora", computadora)
               print("Perdiste, ¡Intentalo de nuevo!")
            elif computadora == "tijera": 
               print("Usuario", usuario)
               print("Computadora", computadora)
               print("¡Felicidades! ¡Ganaste!")  
        elif usuario == "tijera":
            if computadora == "piedra": 
               print("Usuario", usuario)
               print("Computadora", computadora)
               print("¡Felicidades! ¡Ganaste!")
            elif computadora == "papel": 
               print("Usuario", usuario)
               print("Computadora", computadora)
               print("Perdiste, ¡Intentalo de nuevo!") 
    usuario_reinicio= input("¿Quieres volver a jugar? si, no:").lower()
    if  usuario_reinicio == "no":
         print("Gracias por jugar")
         break
    elif usuario_reinicio == "si":
         print("Jugar de nuevo")
         continue