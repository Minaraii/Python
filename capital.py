# CAPITAL TRACKER  1.0

# 1. Datos
capital = float(input("Capital actual:"))
meta = float(input("¿Cual es tu meta de capital? $"))

# 2. Operaciones
total = capital 
faltante = meta - total
porcentaje = (total / meta) * 100 

# 3. Resultados

print("\n==== CAPITAL TRACKER ====")

print(f"Capital actual: ${capital:,.2f}")
print(f"Capital proyectado: ${total:,.2f}")
print(f"Faltante para la meta: ${faltante:,.2f}")
print(f"Progreso: {porcentaje:.2f}%")

print("==== FIN DEL PROGRAMA ====")