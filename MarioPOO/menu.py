import pygame
from mario import Mario
from madeline import Madeline

# --- Menú de selección ---
def menu_seleccion(pantalla):
    fuente = pygame.font.SysFont("Arial", 40)
    opciones = ["Mario", "Madeline"]
    seleccionado = 0

    corriendo = True
    while corriendo:
        pantalla.fill((30, 30, 30))  # Fondo gris oscuro

        # Título
        titulo = fuente.render("Selecciona tu personaje", True, (255, 255, 0))
        pantalla.blit(titulo, (200, 100))

        # Opciones
        for i, opcion in enumerate(opciones):
            color = (255, 0, 0) if i == seleccionado else (255, 255, 255)
            texto = fuente.render(opcion, True, color)
            pantalla.blit(texto, (300, 200 + i * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccionado = (seleccionado - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    seleccionado = (seleccionado + 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    # Retorna la clase seleccionada
                    if seleccionado == 0:
                        return Mario(100, 400)
                    elif seleccionado == 1:
                        return Madeline(100, 400)

# --- Loop principal del juego ---
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego con Menu de Personajes")

    # Menú para elegir personaje
    personaje = menu_seleccion(pantalla)

    clock = pygame.time.Clock()
    corriendo = True

    # --- LOOP PRINCIPAL ---
    while corriendo:
        corriendo_flag = False  # asumimos que no corre

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personaje.saltar()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    personaje.detener()

        # Teclas presionadas en este frame
        keys = pygame.key.get_pressed()
        corriendo_flag = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        if keys[pygame.K_LEFT]:
            personaje.mover_izquierda(corriendo_flag)
        elif keys[pygame.K_RIGHT]:
            personaje.mover_derecha(corriendo_flag)
        else:
            personaje.detener()

        # Actualizar y dibujar
        personaje.actualizar()
        pantalla.fill((0, 0, 0))
        personaje.dibujar(pantalla)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
from mario import Mario
from madeline import Madeline

# --- Menú de selección ---
def menu_seleccion(pantalla):
    fuente = pygame.font.SysFont("Arial", 40)
    opciones = ["Mario", "Madeline"]
    seleccionado = 0

    corriendo = True
    while corriendo:
        pantalla.fill((30, 30, 30))  # Fondo gris oscuro

        # Título
        titulo = fuente.render("Selecciona tu personaje", True, (255, 255, 0))
        pantalla.blit(titulo, (200, 100))

        # Opciones
        for i, opcion in enumerate(opciones):
            color = (255, 0, 0) if i == seleccionado else (255, 255, 255)
            texto = fuente.render(opcion, True, color)
            pantalla.blit(texto, (300, 200 + i * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccionado = (seleccionado - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    seleccionado = (seleccionado + 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if seleccionado == 0:
                        return Mario(100, 400)
                    elif seleccionado == 1:
                        return Madeline(100, 400)

# --- Loop principal del juego ---
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego con Menu de Personajes")

    personaje = menu_seleccion(pantalla)

    clock = pygame.time.Clock()
    corriendo = True

    while corriendo:
        corriendo_flag = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personaje.saltar()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    personaje.detener()

        # Teclas presionadas
        keys = pygame.key.get_pressed()
        corriendo_flag = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        if keys[pygame.K_LEFT]:
            try:
                personaje.mover_izquierda(corriendo_flag)  # Mario
            except TypeError:
                personaje.mover_izquierda()  # Madeline
        elif keys[pygame.K_RIGHT]:
            try:
                personaje.mover_derecha(corriendo_flag)  # Mario
            except TypeError:
                personaje.mover_derecha()  # Madeline
        else:
            personaje.detener()

        # Actualizar y dibujar
        personaje.actualizar()
        pantalla.fill((0, 0, 0))
        personaje.dibujar(pantalla)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
