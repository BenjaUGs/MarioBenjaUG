import pygame
from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._velocidad_x = 0
        self._velocidad_y = 0
        self._en_aire = False
        
    @property
    def posicion(self):
        return (self._x, self._y)
    
    @posicion.setter
    def posicion(self, nueva_posicion):
        self._x, self._y = nueva_posicion
    
    def mover_izquierda(self):
        self._velocidad_x = -5
        
    def mover_derecha(self):
        self._velocidad_x = 5
        
    def detener(self):
        self._velocidad_x = 0
        
    def saltar(self):
        if not self._en_aire:
            self._velocidad_y = -15
            self._en_aire = True
            
    @abstractmethod
    def actualizar(self):
        pass
        
    @abstractmethod
    def dibujar(self, pantalla):
        pass
