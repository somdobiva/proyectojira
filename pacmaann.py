import pygame
import sys
import random

pygame.init()

# Configuración
ANCHO = 400
ALTO = 400
TAM_CELDA = 40
FPS = 8

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Vidas
vidas = 3

# Pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man mejorado")
clock = pygame.time.Clock()

# Mapa MÁS DIFÍCIL
mapa = [
    "##########",
    "#P..#....#",
    "#.#.#.##.#",
    "#.#...#..#",
    "#.###.#..#",
    "#.....#..#",
    "###.###..#",
    "#........#",
    "##########"
]

# Jugador
jugador = [1, 1]

# VARIOS fantasmas
fantasmas = [
    [4, 7],
    [2, 5],
    [6, 3]
]

# Puntos
puntos = {(i, j) for i, fila in enumerate(mapa) for j, col in enumerate(fila) if col == "."}


# ---------------- FUNCIONES ---------------- #

def es_valido(x, y):
    return 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] != "#"


def mover_jugador(dx, dy):
    nx, ny = jugador[0] + dx, jugador[1] + dy
    if es_valido(nx, ny):
        jugador[0], jugador[1] = nx, ny
        puntos.discard((nx, ny))


def mover_fantasmas():
    for fantasma in fantasmas:
        opciones = [(-1,0),(1,0),(0,-1),(0,1)]

        mejor_mov = None
        mejor_dist = float("inf")

        for dx, dy in opciones:
            nx, ny = fantasma[0] + dx, fantasma[1] + dy

            if es_valido(nx, ny):
                dist = abs(nx - jugador[0]) + abs(ny - jugador[1])
                if dist < mejor_dist:
                    mejor_dist = dist
                    mejor_mov = (nx, ny)

        # Movimiento aleatorio a veces
        if random.random() < 0.3:
            random.shuffle(opciones)
            for dx, dy in opciones:
                nx, ny = fantasma[0] + dx, fantasma[1] + dy
                if es_valido(nx, ny):
                    fantasma[0], fantasma[1] = nx, ny
                    break
        elif mejor_mov:
            fantasma[0], fantasma[1] = mejor_mov


def dibujar():
    pantalla.fill(NEGRO)

    # Mapa
    for i, fila in enumerate(mapa):
        for j, col in enumerate(fila):
            if col == "#":
                pygame.draw.rect(pantalla, AZUL,
                                 (j*TAM_CELDA, i*TAM_CELDA, TAM_CELDA, TAM_CELDA))

    # Puntos
    for (i, j) in puntos:
        pygame.draw.circle(
            pantalla, BLANCO,
            (j*TAM_CELDA + TAM_CELDA//2, i*TAM_CELDA + TAM_CELDA//2),
            5
        )

    # Jugador
    pygame.draw.circle(
        pantalla, AMARILLO,
        (jugador[1]*TAM_CELDA + TAM_CELDA//2,
         jugador[0]*TAM_CELDA + TAM_CELDA//2),
        15
    )

    # Fantasmas
    for fantasma in fantasmas:
        pygame.draw.circle(
            pantalla, ROJO,
            (fantasma[1]*TAM_CELDA + TAM_CELDA//2,
             fantasma[0]*TAM_CELDA + TAM_CELDA//2),
            15
        )

    pygame.display.flip()


# ---------------- BUCLE PRINCIPAL ---------------- #

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                mover_jugador(-1, 0)
            elif evento.key == pygame.K_s:
                mover_jugador(1, 0)
            elif evento.key == pygame.K_a:
                mover_jugador(0, -1)
            elif evento.key == pygame.K_d:
                mover_jugador(0, 1)

    mover_fantasmas()

    # Colisión con cualquier fantasma
    for fantasma in fantasmas:
        if jugador == fantasma:
            print("¡Game Over!")
            pygame.quit()
            sys.exit()

    dibujar()
    clock.tick(FPS)