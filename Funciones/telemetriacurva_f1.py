velocidad = int(input("Ingrese la velocidad del auto (en km/h): "))
dano_aleron = int(input("Ingrese el daño del alerón (en porcentaje): "))

def analizar_curva(velocidad, dano_aleron):
    if velocidad > 220 and dano_aleron > 40:
        print("Subviraje crítico: El auto sigue de largo")
    elif velocidad > 220 and dano_aleron <= 40:
        print("Leve: Pérdida de tiempo en el vértice")
    else:
        print("Curva limpia: Trayectoria óptima")

analizar_curva(velocidad, dano_aleron)

