print(" ")
print("Crisitan David Salas De La O 3.W")
print(" ")

def filtrar_palabras(palabras, n):
    return [palabra for palabra in palabras if len(palabra) > n]


palabras = ["manzana", "kiwi", "cereza", "plátano"]
n = 5
print("Palabras con más de", n, "caracteres:", filtrar_palabras(palabras, n))
