print(" ")
print("Crisitan David Salas De La O 3.W")
print(" ")

def mas_larga(palabras):
    return max(palabras, key=len)

palabras = ["manzana", "kiwi", "cereza", "plátano"]
print("La palabra más larga es:", mas_larga(palabras))
