import pygame
from personaje import Personaje

class Mario(Personaje):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._vidas = 1
        self._tiene_power_up = False
        self._color_rojo = (255, 0, 0)
        
    @property
    def vidas(self):
        return self._vidas
        
    def recoger_power_up(self):
        self._tiene_power_up = True
        self._vidas = 2

    def mover_izquierda(self, corriendo=False):
        velocidad_base = -5
        if corriendo:
            velocidad_base *= 1.5
        self._velocidad_x = velocidad_base

    def mover_derecha(self, corriendo=False):
        velocidad_base = 5
        if corriendo:
            velocidad_base *= 1.5
        self._velocidad_x = velocidad_base
        
    def actualizar(self):

        self._x += self._velocidad_x
        self._y += self._velocidad_y

        if self._en_aire:
            self._velocidad_y += 1
            
        if self._y > 400: 
            self._y = 400
            self._velocidad_y = 0
            self._en_aire = False
            
    def dibujar(self, pantalla):
        if self._tiene_power_up:
            color = (200, 0, 0)
        else:
            color = self._color_rojo
        pygame.draw.rect(pantalla, color, (self._x, self._y, 30, 30))
        pygame.draw.circle(pantalla, (255, 255, 255), 
                         (self._x + 15, self._y + 10), 10)
