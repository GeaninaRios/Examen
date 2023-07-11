import numpy as np
import os
import fun as fn

edificio = np.empty((10,4), dtype=object)
fn.llenaMatriz(edificio)
compradores = []

while True:
    os.system("cls")
    print("**********Casa Feliz**********")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    op = fn.validaMenú()

    if op == 1:
        fn.comprarDepartamento(edificio, compradores)
    elif op == 2:
        fn.mostrarApartamentos(edificio)
    elif op== 3:
        fn.comprarDepartamento
    elif op == 4:
        fn.comprarDepartamento(matriz, compradores)
    else:
        fn.salir()
        break

    os.system("pause")