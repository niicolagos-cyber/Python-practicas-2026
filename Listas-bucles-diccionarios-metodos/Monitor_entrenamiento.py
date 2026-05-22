dias = {"Lunes": "Pecho/Triceps", "Martes": "Espalda/Bíceps", "Miércoles": "Piernas", "Jueves": "Hombros", "Viernes": "Pecho/Triceps", "Sábado": "Cardio", "Domingo": "Descanso"}

#.items() es un método que devuelve una vista de objetos de los pares clave-valor en un diccionario. En este caso, se utiliza para iterar sobre el diccionario "dias" y mostrar cada día de la semana junto con el grupo muscular correspondiente para el entrenamiento.

for dia, musculo in dias.items():
    print(f"El dia {dia} toca entrenar {musculo}.")
    if "Piernas" in musculo:
        contador_piernas +=1

if contador_piernas < 2:
    print("¡Error! No estás cumpliendo con la frecuencia 2 en Piernas.")