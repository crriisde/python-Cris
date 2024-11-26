print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Pedir al usuario que ingrese un año
anio = int(input("Ingresa un año para determinar si es bisiesto: "))

# Verificar si el año es bisiesto
if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
