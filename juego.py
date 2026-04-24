import os
import time

# Mapa del juego
mapa = [
    list("##########"),
    list("#P.......#"),
    list("#.####...#"),
    list("#........#"),
    list("##########")
]

# Posición inicial del jugador
jugador_x = 1
jugador_y = 1
puntos = 0

def mostrar_mapa():
    os.system("cls" if os.name == "nt" else "clear")
    for fila in mapa:
        print("".join(fila))
    print(f"Puntos: {puntos}")

def mover(direccion):
    global jugador_x, jugador_y, puntos

    nuevo_x = jugador_x
    nuevo_y = jugador_y

    if direccion == "w":
        nuevo_x -= 1
    elif direccion == "s":
        nuevo_x += 1
    elif direccion == "a":
        nuevo_y -= 1
    elif direccion == "d":
        nuevo_y += 1

    # Comprobar colisión con pared
    if mapa[nuevo_x][nuevo_y] != "#":
        # Sumar punto si hay '.'
        if mapa[nuevo_x][nuevo_y] == ".":
            puntos += 1

        # Mover jugador
        mapa[jugador_x][jugador_y] = " "
        jugador_x = nuevo_x
        jugador_y = nuevo_y
        mapa[jugador_x][jugador_y] = "P"

def quedan_puntos():
    for fila in mapa:
        if "." in fila:
            return True
    return False

# Bucle principal
while True:
    mostrar_mapa()

    if not quedan_puntos():
        print("¡Has ganado!")
        break

    movimiento = input("Mover (WASD): ").lower()
    mover(movimiento)