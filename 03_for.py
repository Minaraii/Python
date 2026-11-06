# MISSION 02.3 - El blucle FOR
# Tarea 1 - Tabla de multiplicar del 5

numero = 5

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Tabla de multiplicar del 7

numero = 7

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Bucle Anidado - Tabla de multiplicar del 3 y del 8 

for numero in [3, 8]:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

    print("------------------------------")