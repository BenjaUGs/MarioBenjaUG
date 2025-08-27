from desafio import Submarino

def iniciar_menu():
    sub = Submarino()
    print("Bienvenido al panel de control del submarino The Perle.")
    print("Escriba un comando. Use 'ayuda' para ver opciones.")

    comandos = {
        "estado": lambda: print(sub),
        "asignar": lambda: asignar(sub),
        "sumergir": lambda: sumergir(sub),
        "daño": lambda: recibir(sub),
        "reparar": lambda: sub.reparar(),
        "tripulantes": lambda: print(f"Tripulantes: {len(sub)}"),
        "ayuda": mostrar_ayuda,
        "salir": lambda: exit()
    }

    while True:
        cmd = input(">> ").strip().lower()
        if cmd in comandos:
            comandos[cmd]()
        else:
            print("Comando no válido. Escriba 'ayuda'.")

def asignar(sub):
    try:
        m = int(input("Energía a motores: "))
        a = int(input("Energía a armas: "))
        e = int(input("Energía a escudos: "))
        sub.asignar_energia(m, a, e)
    except:
        print("Entrada inválida.")

def sumergir(sub):
    try:
        metros = int(input("Metros a sumergir: "))
        sub.sumergirse(metros)
    except:
        print("Entrada inválida.")

def recibir(sub):
    try:
        daño = int(input("Cantidad de daño: "))
        sub.recibir_danio(daño)
    except:
        print("Entrada inválida.")

def mostrar_ayuda():
    print("""
Comandos disponibles:
- estado: Muestra el estado actual
- asignar: Asigna energía a sistemas
- sumergir: Baja el submarino
- daño: Simula daño
- reparar: Repara el submarino
- tripulantes: Muestra cantidad
- salir: Cierra el programa
""")

if __name__ == "__main__":
    iniciar_menu()
