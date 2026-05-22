proteinas = int(input("Ingrese los gramos de proteinas: "))
carbohidratos = int(input("Ingrese los gramos de carbohidratos: "))
grasas = int(input("Ingrese los gramos de grasas: "))

def calcular_calorias_totales(proteinas, carbohidratos, grasas):
    return (proteinas * 4) + (carbohidratos * 4) + (grasas * 9)

calorias_totales = calcular_calorias_totales(proteinas, carbohidratos, grasas)
print(f"El total de calorias que tiene el plato es de {calorias_totales}")