ingredientes = ["carne", "pechuga", "papas", "huevos", "brocoli"]

for ing in ingredientes:
    print(f"Preparando {ing} en la freidora de aire a 180°C...")
    if ing == "papas":
        print("Las papas tardarán 20 minutos en cocinarse.")
    else:
        print("Tardará unos 10 minutos en cocinarse.")
    print("-" * 20) # Para separar cada plato