print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
nombres = ["Ana", "Pedro", "Andrés", "Maria", "Antonio", "Lucía", "Adriana"]

# Pedir al usuario que ingrese una letra para buscar
letra = input("Ingresa una letra para contar los nombres que comienzan con ella: ").lower()

# Contar cuantos nombres comienzan con la letra ingresada
nombres_con_letra = sum(1 for nombre in nombres if nombre.lower().startswith(letra))

print(f"Cantidad de nombres que comienzan con la letra '{letra}': {nombres_con_letra}")
