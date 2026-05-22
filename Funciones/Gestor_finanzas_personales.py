total_ingresos = float(input("Ingrese el total de ingresos mensuales: "))
categorias_gastos = {
    "Comida": 0,
    "Transporte": 0,
    "Entretenimiento": 0,
}

# La función solo hace matemática (sin prints ni loops)
def calcular_ahorro(ingresos, gastos):
    return ingresos - gastos

# El ciclo principal va fuera de cualquier función
while True:
    print("\n--- Menú de opciones ---")
    print("1: Agregar un gasto a una categoría")
    print("2: Ver resumen de gastos y ahorro")
    print("3: Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        cat = input("Categoría (Comida, Transporte, Entretenimiento): ")
        # .capitalize() ayuda a que si escriben 'comida' igual funcione
        if cat.capitalize() in categorias_gastos:
            monto = float(input("Ingrese el monto del gasto: "))
            # Validación de fondos
            if (sum(categorias_gastos.values()) + monto) > total_ingresos:
                print("¡Cuidado! Ese gasto supera tu ingreso total.")
            else:
                categorias_gastos[cat.capitalize()] += monto
        else:
            print("Categoría no válida.")
            
    elif opcion == "2":
        total_gastos = sum(categorias_gastos.values())
        ahorro = calcular_ahorro(total_ingresos, total_gastos)
        print(f"\nResumen: {categorias_gastos}")
        print(f"Total Gastado: {total_gastos}")
        print(f"Ahorro disponible: {ahorro}")
        
    elif opcion == "3":
        print("Saliendo. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")