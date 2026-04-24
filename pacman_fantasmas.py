import pygame
import sys
import random

pygame.init()

ANCHO = 400
ALTO = 400
TAM_CELDA = 40

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man con Fantasmas")

NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

mapa = [
    "##########",
    "#P.......#",
    "#.####...#",
    "#....X...#",
    "##########"
]

jugador_x = 1
jugador_y = 1

fantasma_x = 3
fantasma_y = 5

puntos = []
for i, fila in enumerate(mapa):
    for j, col in enumerate(fila):
        if col == ".":
            puntos.append((i, j))

clock = pygame.time.Clock()

def mover_fantasma():
    global fantasma_x, fantasma_y

    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx = fantasma_x + dx
        ny = fantasma_y + dy

        if mapa[nx][ny] != "#":
            fantasma_x = nx
            fantasma_y = ny
            break

while True:
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            nx, ny = jugador_x, jugador_y

            if evento.key == pygame.K_w:
                nx -= 1
            elif evento.key == pygame.K_s:
                nx += 1
            elif evento.key == pygame.K_a:
                ny -= 1
            elif evento.key == pygame.K_d:
                ny += 1

            if mapa[nx][ny] != "#":
                jugador_x, jugador_y = nx, ny

                if (jugador_x, jugador_y) in puntos:
                    puntos.remove((jugador_x, jugador_y))

    # Mover fantasma cada frame
    mover_fantasma()

    # Colisión jugador-fantasma
    if jugador_x == fantasma_x and jugador_y == fantasma_y:
        print("¡Game Over!")
        pygame.quit()
        sys.exit()

    # Dibujar mapa
    for i, fila in enumerate(mapa):
        for j, col in enumerate(fila):
            x = j * TAM_CELDA
            y = i * TAM_CELDA

            if col == "#":
                pygame.draw.rect(pantalla, AZUL, (x, y, TAM_CELDA, TAM_CELDA))

    # Dibujar puntos
    for punto in puntos:
        px = punto[1] * TAM_CELDA + TAM_CELDA // 2
        py = punto[0] * TAM_CELDA + TAM_CELDA // 2
        pygame.draw.circle(pantalla, BLANCO, (px, py), 5)

    # Dibujar jugador
    px = jugador_y * TAM_CELDA + TAM_CELDA // 2
    py = jugador_x * TAM_CELDA + TAM_CELDA // 2
    pygame.draw.circle(pantalla, AMARILLO, (px, py), 15)

    # Dibujar fantasma
    fx = fantasma_y * TAM_CELDA + TAM_CELDA // 2
    fy = fantasma_x * TAM_CELDA + TAM_CELDA // 2
    pygame.draw.circle(pantalla, ROJO, (fx, fy), 15)

    pygame.display.flip()
    clock.tick(5)