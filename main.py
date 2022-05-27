from funciones import transponer as trans
opcion_volver_menu=0
montos_de_criptomoneda=[0,0,0,0]
monto_inversion=0
t=1
lista_socios=[["Nombre"],["Codigo"],["Moneda"],["Monto"]]
while True:
    print("Menu de opciones\n")
    print("1. Registro de nuevo socio")
    print("2. Lista de activos digitales")
    print("3. Lista de socios")
    print("4. Salir\n")
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion.isdigit():
          if 1 <= int(opcion) <= 4:
               break

    if int(opcion) == 1:
        print("Datos personales\n")
        nombre = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")
        correo = input("Ingrese su correo electronico: ")
        print()
        print("Inversion")
        print()
        fecha_inversion = input("Ingrese la fecha: ")
        print()
        print("Criptomoneda a comprar:")
        print("1. Bitcoin")
        print("2. Etherium")
        print("3. Dogcoin")
        print("4. Binance")
        while True:
            opcion_cripto = input("Selecciona una opcion: ")
            if opcion_cripto.isdigit():
              if 1 <= int(opcion_cripto) <= 4:
                break

        if int(opcion_cripto)==1:
           print()
           monto_inversion = int(input("Igrese el monto en soles a invertir: "))
           montos_de_criptomoneda[0]+=monto_inversion
           lista_socios[0].append(nombre)
           lista_socios[1].append("User"+str(t))
           lista_socios[2].append("Bitcoin")
           lista_socios[3].append(str(monto_inversion))
           t+=1
        if int(opcion_cripto)==2:
           print()
           monto_inversion = int(input("Igrese el monto en soles a invertir: "))
           montos_de_criptomoneda[1]+=monto_inversion
           lista_socios[0].append(nombre)
           lista_socios[1].append("User" + str(t))
           lista_socios[2].append("Etherium")
           lista_socios[3].append(str(monto_inversion))
           t+=1
        if int(opcion_cripto) == 3:
            print()
            monto_inversion = int(input("Igrese el monto en soles a invertir: "))
            montos_de_criptomoneda[2]+=monto_inversion
            lista_socios[0].append(nombre)
            lista_socios[1].append("User" + str(t))
            lista_socios[2].append("Dogcoin")
            lista_socios[3].append(str(monto_inversion))
            t+=1
        if int(opcion_cripto) == 4:
            print()
            monto_inversion = int(input("Igrese el monto en soles a invertir: "))
            montos_de_criptomoneda[3]+=monto_inversion
            lista_socios[0].append(nombre)
            lista_socios[1].append("User" + str(t))
            lista_socios[2].append("Binance")
            lista_socios[3].append(str(monto_inversion))
            t+=1
        print(100 * "-")
        print('{:^100}'.format("Fin de registro"))
        print(100 * "-")
        while True:
            opcion_volver_menu = input("Ingrese 0 para regresar al menu principal: ")
            if int(opcion_volver_menu) == 0:
                print()
                break
    if int(opcion)==2:
        print(100*"-")
        print('{:^100}'.format("Lista de activos digitales"))
        print(100 * "-")
        print("El fundo mutuo en Bitcoin es:",montos_de_criptomoneda[0])
        print("El fundo mutuo en Etherium es:",montos_de_criptomoneda[1])
        print("El fundo mutuo en Dogcoin es:",montos_de_criptomoneda[2])
        print("El fundo mutuo en Binance es:",montos_de_criptomoneda[3])
        print(100*"-")
        while True:
            opcion_volver_menu = input("Ingrese 0 para regresar al menu principal: ")
            if opcion_volver_menu.isdigit():
                if int(opcion_volver_menu) == 0:
                    print()
                    break
    if int(opcion)==3:
        print(100 * "-")
        print('{:^100}'.format("Lista de socios"))
        print(100 * "-")
        lista_transpuesta_socios=trans(lista_socios)[:]
        for i in range(len(lista_transpuesta_socios)):
            for j in range(len(lista_transpuesta_socios[0])):
                print('{:<15}'.format('{:>5}'.format(lista_transpuesta_socios[i][j])), end=" ")
            print()
        print(100 * "-")
        while True:
            opcion_volver_menu = input("Ingrese 0 para regresar al menu principal: ")
            if opcion_volver_menu.isdigit():
               if int(opcion_volver_menu) == 0:
                  print()
                  break
        print()
    if int(opcion)==4:
        print(100 * "-")
        print('{:^100}'.format("GRACIAS POR INVERTIR, VUELVA PRONTO"))
        print(100 * "-")
        break








