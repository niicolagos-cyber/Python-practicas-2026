def calcular_tiempo_descarga():
    velocidad_internet = float(input("Ingrese la velocidad de internet en Megabits por segundo (Mbps): "))
    tamano_archivo_mb = float(input("Ingrese el tamaño del archivo en GB: "))
    
    megabytes_por_segundo = velocidad_internet / 8
    tamano_archivo_mb = tamano_archivo_mb * 1000
    tiempo_horas = (tamano_archivo_mb / megabytes_por_segundo) / 3600
    
    if tiempo_horas < 3:
        print(f"El tiempo estimado de descarga es de {tiempo_horas:.2f} horas. Es una descarga rápida.")
    elif tiempo_horas >=3 and tiempo_horas <= 8:
        print(f"El tiempo estimado de descarga es de {tiempo_horas:.2f} horas. Paciencia, mirate una peli mientras tanto.")
    else:
        print(f"El tiempo estimado de descarga es de {tiempo_horas:.2f} horas. Mejor que te vayas a dormir, porque va a tardar mucho.")

calcular_tiempo_descarga()