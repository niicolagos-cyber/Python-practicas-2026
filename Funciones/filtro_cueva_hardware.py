def filtrar_por_presupuesto(catalogo, presupuesto_max):
    #recorrer el diccionario y armar una lista nueva que contenga solo los nombres de las placas que el usuario puede pagar con su presupuesto_max y retornar esa lista
    placas_filtradas = []
    for placa, precio in catalogo.items():
        if precio <= presupuesto_max:
            placas_filtradas.append(placa)
    return placas_filtradas