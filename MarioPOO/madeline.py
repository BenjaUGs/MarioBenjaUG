import pygame
from personaje import Personaje

class Madeline(Personaje):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._vidas = 1
        self._tiene_power_up = False
        self._color_azul = (0, 0, 255)
        self._salto_doble_disponible = True
        self._salto_doble_activo = False
        
    def saltar(self):
        if not self._en_aire:
            self._velocidad_y = -15
            self._en_aire = True
            self._salto_doble_disponible = True
        elif self._salto_doble_disponible and not self._salto_doble_activo:
            self._velocidad_y = -12
            self._salto_doble_activo = True
            self._salto_doble_disponible = False
            
    def actualizar(self):
        self._x += self._velocidad_x
        self._y += self._velocidad_y
        
        if self._en_aire:
            self._velocidad_y += 1
            

        if self._y > 400:
            self._y = 400
            self._velocidad_y = 0
            self._en_aire = False
            self._salto_doble_disponible = True
            self._salto_doble_activo = False

    def dibujar(self, pantalla):
        color = self._color_azul
        pygame.draw.rect(pantalla, color, (self._x, self._y, 30, 30))
        pygame.draw.circle(pantalla, (255, 255, 255), 
                         (self._x + 15, self._y + 10), 10)
