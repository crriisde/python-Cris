print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
# Definir una tupla con 10 edades
edades = (18, 25, 30, 15, 40, 22, 19, 35, 17, 45)

# Contar cuántas edades son superiores a 20
mayores_20 = sum(1 for edad in edades if edad > 20)


print(f"Cantidad de personas con edades superiores a 20: {mayores_20}")
