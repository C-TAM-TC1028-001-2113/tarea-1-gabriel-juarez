def main():
    # escribe tu código abajo de esta línea
    from math import ceil
    palabras = int(input("Dame el número de palabras: "))
    paginas = ceil(palabras/475)
    costo = paginas * 60
    costo_1 = costo * .9
    
    print("El costo de la publicación es :", costo_1)

if __name__ == '__main__':
    main()
