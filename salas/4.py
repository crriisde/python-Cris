print(" ")
print("Crisitan David Salas De La O 3.W")
print(" ")

def contar_mayusculas():
    cadena = input("Ingrese una cadena: ")
    count = sum(1 for char in cadena if char.isupper())
    print(f"La cadena tiene {count} letras mayúsculas.")

# Llamar a la función para ejecutar el programa
contar_mayusculas()
