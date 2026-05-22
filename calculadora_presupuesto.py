procesador = float(input("Ingrese el valor del procesador: "))
tarjeta_grafica = float(input("Ingrese el valor de la tarjeta: "))
memoria_ram = float(input("Ingrese el valor de la memoria RAM: "))

costo_total = procesador + tarjeta_grafica + memoria_ram

print(f"El costo total de la computadora es: {costo_total * 1.21} pesos.") # se multiplica por el 21% para incluir el iva.
