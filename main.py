# Lugar para poner los import
from funciones import *

iniciador('Iniciando programa del servidor')

# Variables generales
opcion_volver_menu = 0
montos_de_criptomoneda = [0, 0, 0, 0]
t = 1
lista_socios = [["Nombre"], ["Codigo"], ["Moneda"], ["Monto"]]

# Inicio del código while


while True:

    Separadores("FONDOS MUTUOS CRYPTO")

    # Menú
    print("Menu de opciones\n")
    print("1. Registro de nuevo socio")
    print("2. Lista de activos digitales")
    print("3. Lista de socios")
    print("4. Salir\n")

    # Función para seleccionar una opcion
    opcion = seleccion_de_opcion("Ingrese una opcion: ")
    time.sleep(0.5)
    e()

    # Opción 1
    if int(opcion) == 1:

        Separadores("Registro de nuevo socio")

        print("Datos personales\n")

        nombre = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")

        while True:
            correo = input("Ingrese su correo electronico: ")

            if correo[-3:] == 'com' or es_correo_valido(correo):
                break

        time.sleep(0.5)

        e()
        print("Inversion")
        e()
        while True:
           fecha_inversion = input("Ingrese la fecha: ")
           if es_fecha_valida(fecha_inversion):
               break
        time.sleep(0.5)
        e()
        print("Criptomoneda a comprar:")
        print("1. Bitcoin")
        print("2. Etherium")
        print("3. Dogecoin")
        print("4. Binance")

        # Función para seleccionar una opcion
        opcion_cripto = seleccion_de_opcion("Seleccione una opcion: ")
        e()

        # Datos a almacenar en las matrices
        monto_inversion = monto_de_inversion()
        lista_socios[0].append(nombre)
        lista_socios[1].append("User" + str(t))
        lista_socios[3].append(str(monto_inversion))
        t += 1

        if int(opcion_cripto) == 1:
            montos_de_criptomoneda[0] += int(monto_inversion)
            lista_socios[2].append("Bitcoin")

        if int(opcion_cripto) == 2:
            montos_de_criptomoneda[1] += int(monto_inversion)
            lista_socios[2].append("Etherium")

        if int(opcion_cripto) == 3:
            montos_de_criptomoneda[2] += int(monto_inversion)
            lista_socios[2].append("Dogecoin")

        if int(opcion_cripto) == 4:
            montos_de_criptomoneda[3] += int(monto_inversion)
            lista_socios[2].append("Binance")

        e()
        Separadores("Fin de registro")
        print(' ')

        # Funcion para volver al menú
        volver_menu()
        e()

    #Opcion 2
    if int(opcion) == 2:

        Separadores("Lista de activos digitales")

        print("El fondo mutuo en Bitcoin es:", montos_de_criptomoneda[0])
        print("El fondo mutuo en Etherium es:", montos_de_criptomoneda[1])
        print("El fondo mutuo en Dogecoin es:", montos_de_criptomoneda[2])
        print("El fondo mutuo en Binance es:", montos_de_criptomoneda[3])

        print(100*"-")

        volver_menu()
        e()

    #Opción 3
    if int(opcion) == 3:

        Separadores("Lista de socios")

        # transpuesta
        lista_transpuesta_socios = transponer(lista_socios)[:]

        # IMPRESION DE MATRIZ
        imprimir(lista_transpuesta_socios)
        # IMPRESION DE MATRIZ ---CAMBIAR A FUNCION
        print(100 * "-")

        volver_menu()
        e()

    #Opción 4
    if int(opcion) == 4:

        Separadores_de_cierre("Cerrando el programa","GRACIAS POR INVERTIR EN CRYPTO, VUELVA PRONTO")

        break

