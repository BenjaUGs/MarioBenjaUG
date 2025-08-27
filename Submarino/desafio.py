class Submarino:
    def __init__(self):
        self.nombre = "The Perle"
        self.salud = 60
        self.tripulantes = 2
        self.energia_total = 6
        self.energia = {
            "motores": 0,
            "armas": 0,
            "escudos": 0
        }
        self.profundidad = 0

def asignar_energia(self, sistema, puntos):
    if sistema in self.energia and 0 <= puntos <= self.energia_total:
        energia_usada = sum(self.energia.values()) - self.energia[sistema]
        energia_disponible = self.energia_total - energia_usada
        if puntos <= energia_disponible:
            self.energia[sistema] = puntos


    def sumergirse(self, metros):
        if self.energia["motores"] > 0:
            self.profundidad += metros * self.energia["motores"]
    
    def recibir_danio(self, daño):
        defensa = self.energia["escudos"] * 5
        daño_real = max(0, daño - defensa)
        self.salud -= daño_real
        if self.salud < 0:
            self.salud = 0

    def reparar(self):
        if self.tripulantes >= 2:
            self.salud += 10 * self.tripulantes
            if self.salud > 60:
                self.salud = 60

    def __str__(self):
        return f"{self.nombre} - Salud: {self.salud}, Profundidad: {self.profundidad}, Tripulantes: {self.tripulantes}"

    def __len__(self):
        return self.tripulantes