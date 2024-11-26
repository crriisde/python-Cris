print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
def contar_vocales(palabra):
    contador = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Contar las vocales en la palabra
    for letra in palabra.lower():
        if letra in contador:
            contador[letra] += 1
    
    return contador

# Pedir al usuario que ingrese una palabra
palabra = input("Ingresa una palabra para contar las vocales: ")

# Contar las vocales
resultado = contar_vocales(palabra)

print(f"Cantidad de vocales en la palabra '{palabra}':")
for vocal, cantidad in resultado.items():
    print(f"{vocal.upper()}: {cantidad}")
