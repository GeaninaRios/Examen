def validaMenú():
    while True:
        try:
            op = int(input("\tElija opcion: "))
            if op < 1 or op > 5:
                print("Debe ingresar un numero del 1 al 5")
            else:
                break
        except:
            print("Debe ingresar un numero")
    return op

def llenaMatriz(matriz):
    for i in range(10):
        for j in range(4):
            matriz[i,j] = " "

def validaPiso():
    while True:
        try:
            piso = int(input("¿En que piso desea comprar el departamento?: "))
            if piso < 1 or piso > 10:
                print("Debe ingresar un numero de piso del 1 al 10")
            else:
                break
        except:
            print("Debe ingresar un numero")
    return piso

def validaTipo():
    while True:
        tipo = input("\n¿Que tipo de departamento quiere? (A/B/C/D): ").lower()
        if tipo != "a" and tipo != "b" and tipo != "c" and tipo != "d":
            print("Debe ingresar a, b, c o d")
        else:
            break
    return tipo

def mostrarApartamentos(matriz):
    print("\n\tPiso               Tipo")
    print("\t\t A\t B\t C\t D\n")
    for i in range(9, -1, -1):
        print("\t", i+1, end =" ")
        for j in range(4):
            print("\t", matriz[i, j], end=" ")
        print()
    print()

def validaRun():
    while True:
        try:
            run = int(input("\nIngrese su rut para registrarlo, sin el digito verificador: "))
            if run < 1000000 or run > 99999999:
                print("Debe ingresar un rut valido, sin el digito verificador")
            else:
                break
        except:
            print("Debe ingresar un numero")
    return run

def comprarDepartamento(matriz, compradores):
    mostrarApartamentos(matriz)

    piso = validaPiso()
    tipo = validaTipo()

    while True:
        if (tipo == "a" and matriz[piso-1, 0] == "X") or (tipo == "b" and matriz[piso-1, 1] == "X") or (tipo == "c" and matriz[piso-1, 2] == "X") or (tipo == "d" and matriz[piso-1, 3] == "X"):
            print("No esta disponible, elija otro")

            piso = validaPiso()
            tipo = validaTipo()
        else:
            if tipo == "a":
                print("\nCosto de 3800 UF")
                matriz[piso-1,0] = "X"
            elif tipo == "b":
                print("\nCosto de 3000 UF")
                matriz[piso-1,1] = "X"
            elif tipo == "c":
                print("\nCosto de 2800 UF")
                matriz[piso-1,2] = "X"
            else:
                print("\nCosto de 3500 UF")
                matriz[piso-1,3] = "X"

            run = validaRun()
            compradores.append(run)

            print("\nLa operación se ha realizado correctamente.\n")
            break

def salir():
    print("Salida del sistema, Geanina Ríos 11/07/2023")