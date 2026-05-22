def calcular_tasa_prenez(total_vientres, vacas_vacias):
    porcentaje_prenez = ((total_vientres -vacas_vacias) / total_vientres) * 100
    return round(float(porcentaje_prenez), 2) #poner dos decimales al return

porcenta_de_prenez = calcular_tasa_prenez(200,40)
print(f"La tasa de preñez es: {porcenta_de_prenez}%")