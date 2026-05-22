def calcular_macros():
    objetivo_usuario = input("Cual es tu objetivo nutricional ? Volumen o Mantenimiento: ")
    peso_corporal = int(input("Ingrese su peso corporal en kg: "))
    
    if objetivo_usuario.lower() == "volumen":
        cantidad_proteinas = peso_corporal * 2.2
        cantidad_carbohidratos = peso_corporal * 4
        print(f"Para tu objetivo de volumen, debes consumir aproximadamente {cantidad_proteinas:.2f} gramos de proteínas y {cantidad_carbohidratos:.2f} gramos de carbohidratos al día.")
    elif objetivo_usuario.lower() == "mantenimiento":
        cantidad_proteinas = peso_corporal * 2
        cantidad_carbohidratos = peso_corporal * 2.5
        print(f"Para tu objetivo de mantenimiento, debes consumir aproximadamente {cantidad_proteinas:.2f} gramos de proteínas y {cantidad_carbohidratos:.2f} gramos de carbohidratos al día.")
    else:
        print("Objetivo no reconocido, por favor ingrese Volumen o Mantenimiento.")

calcular_macros()