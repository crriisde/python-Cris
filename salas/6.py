print(" ")
print("Crisitan David Salas De La O 3.W")
print(" ")

def calcular_edades():
    anio_actual = int(input("Ingrese el año en curso: "))
    
    for i in range(3):
        nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
        anio_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
        edad = anio_actual - anio_nacimiento
        print(f"{nombre} cumplirá {edad} años en {anio_actual}.")

# Llamar a la función para ejecutar el programa
calcular_edades()
