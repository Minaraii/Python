# MISSION 02.4 -  Analizador de capitales 

capitales = [33, 100, 250, 500, 1000]
total = 0 

for capital in capitales:
    total += capital
    print(f"Capital: {capital}")

print(f"Total de capitales: {total}")

# Analizador de capitales 2.0

capitales = [33, 100, 250, 500, 1000]
total = 0

for capital in capitales:
    total += capital
    print(f"Capital: {capital}")
    print(f"Total acumulado: {total}")

print("------------------------------")
print(f"Capital total: {total}")
print(f"Capital maximo: {max(capitales)}")
print(f"Capital minimo: {min(capitales)}")