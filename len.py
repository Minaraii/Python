# MISSION 02.5
# ¿Como podrias calcular el promedio? 

capitales = [10, 100, 1000]
total = 0 
for capital in capitales: 
    total += capital
promedio = total / len(capitales)

print(f"Promedio Capital: {promedio}")