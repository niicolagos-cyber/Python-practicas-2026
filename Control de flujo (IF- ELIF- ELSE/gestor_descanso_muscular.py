def gestor_descanso(dias):
    dias = int(input("Cuantos dias pasaron desde la ultima vez que entrenó piernas? "))
    if dias <= 2:
        print("Músculo en recuperación, entrená el tren superior.")
    elif dias >= 3 and dias <= 4:
        print("Ventana ideal para mantener la frecuencia 2, metele a las piernas.")
    else:
        print("Estás perdiendo estimulo, toca dia de piernas urgente.")

gestor_descanso(0)