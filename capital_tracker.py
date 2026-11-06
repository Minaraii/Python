# CAPITAL TRACKER  1.1

#1. Datos
capital = float(input("Capital actual: $"))
meta = float(input("¿Cual es tu meta de capital? $"))

# 2. Validaciones
if meta <= 0: 
    print("La meta debe ser mayor que cero.")

else: 
    if capital < 0:
        print("El capital no puede ser negativo .")

    else:
        # 3. Operaciones 
        total = capital
        faltante = meta - total
        porcentaje = (total / meta) * 100

        # 4. Resultados 
        print("\n=== CAPITAL TRACKER ===")
        print(f"Capital actual: ${capital:,.2f}")
        print(f"Capital proyectado: ${total:,.2f}")
        print(f"Faltante para la meta: ${faltante:,.2f}")
        print(f"Progreso: {porcentaje:.2f}%")

        # 5. Clasificacion 
        if porcentaje >= 100:
            print("CUMBRE ALCANZADA")
        elif porcentaje >= 75:
            print("CASI EN LA CUMBRE")
        elif porcentaje >= 50: 
            print("MITAD DEL CAMINO")
        elif porcentaje >= 25:
            print("EMPEZANDO EL ASCENSO")
        else:
            print("SIGUE ADELANTE, NO TE RINDAS")

        print("=== FIN DEL PROGRAMA ===")