aleron_delantero = int(input("Ingrese el nivel de carga aerodinamica del aleron delantero (del 1 al 10): "))
aleron_trasero = int(input("Ingrese el nivel de carga aerodinamica del aleron trasero (del 1 al 10): "))

if (aleron_delantero) - (aleron_trasero) > 2:
    print("Alerta: Exceso de carga frontal. El auto tiene tendencia al sobreviraje (Oversteer).")
elif (aleron_trasero) - (aleron_delantero) > 2:
    print("Alerta: Exceso de carga trasera. El auto va a sufrir subviraje (Understeer) en cuervas lentas.")
else:
    print("Balance aerodinamico optimo.")


