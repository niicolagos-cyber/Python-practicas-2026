componentes_pc = ["GTX 1650", "RTX 4060 TI", "RTX 3060", "RTX 4090"]

componentes_pc.append("RTX 4070")

componentes_pc.sort()

# Enumerate envuelve a la lista, y podemos desempaquetar el índice y el elemento directamente
for i, componente in enumerate(componentes_pc):
    print(f"Puesto {i + 1}: {componente}")