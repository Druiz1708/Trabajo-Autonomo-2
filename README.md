Juego en Python: Piedra, Papel o Tijera.

Realice un juego de consola desarrollado en Python, que incluye dos modos de juego:

Modo 1: Jugador Vs Computadora

Modo 2: Jugador Vs Jugador (Multijugador)

Lo diseñe para que sea jugado desde la consola con controles simples

Lenguaje de programación:

El lenguaje que utilice fue python, la versión 3.13, ya que es el lenguaje que usted en clase nos enseño por ser el mas adecuado para aprender programación.

Requisitos:

Debe estar el Python 3.x instalado en tu ordenador

Estructura del codigo:

1.Librerias utilizadas:

Random: Utilice esta libreria para que la computadora elija aleatoriamente entre piedra, papel o tijera

os: Utilice est alibreria para limpiar la pantalla de la consola según el sistema operativo

getpass: Utilice esta libreria para que los jugadores ingresen sus elecciones de forma oculta en modo jugador

2.	Modos de Juego
   
Modo 1: Contra la Computadora

El jugador escoge su jugada

La computadora escoge su jugada aleatoriamente

Se comparan las dos jugadas para determinar el resultado

Se actualizan los puntos y se pregunta si el jugador desea jugar de nuevo, volver al menu o salir del juego

Modo 2: Multijugador

Cada jugador ingresa su jugada en secreto (Oculta con getpass)

Se comparan las elecciones de ambos

Se publican los resultados

Se muestran las estadisticas y se pregunta si quieren seguir jugando, volver al menu o salir del juego

Logica del juego

El juego sigue las reglas clasicas:

-Piedra vence Tijera

-Tijera vence Papel

-Papel vence Piedra

Se usa estructuras de condicionales como if, elif, else para determinar el resultado de cada jugada

¿Como ejecutar el juego?

1.	Abre tu terminal o consola de comandos en Python
   
2.	Abre la carpeta donde esta guardado el archivo del juego
   
3.	Seleccion "Run Python File"
   
4.	El juego se ejecutara en la terminal
   
¿Cómo jugar?

1.	Ejecuta el programa en la terminal con python juego.py
  
2.	Le aparecera el menu principal con 3 opciones:

i.	Jugar contra la computadora

ii.	Modo multijugador

iii.	Salir del juego

4.	Cuando escoja el modo en el que desea jugar

i.	Escribe tu jugada: piedra, papel o tijera

ii.	El contricante hara su jugada

iii.	Se mostrara quien gano o si es empate

5.	Al final de cada ronda, se preguntara:

i.	Si: para volver a jugar

ii.	No: Para salir completamente del juego

iii.	Menu: Para regresar al menu principal

6.	Si ingresa Una palabra distinta a las dichas, el sistema lo inidcara y te volvera a preguntar que opcion escoges

Creditos:

El proyecto presente fue desarrollado como parte del trabajo final para la materia de Logica de Programacion

Notas:

-El programa esta en español

-Incluye validacion de entradas para evitar errores

-Opcion menu permite regresar al menu principal sin salirse completamente del juego
