# Lugar para poner los import
from funciones import *
import pandas as pd
import matplotlib.pyplot as plt
iniciador('Iniciando programa del servidor','Carga con exito.')
e()

# Variables generales
opcion_volver_menu = 0
montos_de_criptomoneda = [0, 0, 0, 0]
t = 1
lista_socios = [["Nombre"], ["Codigo"], ["Moneda"], ["Monto"]]
cryptos_mes={
"Enero":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Febrero":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Marzo":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Abril":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Mayo":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Junio":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Julio":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Agosto":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Septiembre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Octubre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Noviembre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Diciembre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
} #diccionario de inversiones por moneda y mes
mes=""
moneda=""
# Inicio del código while
while True:
    Separadores("FONDOS MUTUOS CRYPTO")

    # Menú
    print("Menu de opciones\n")
    print("1. Registro de nuevo socio")
    print("2. Lista de activos digitales")
    print("3. Lista de socios")
    print("4. Leer base de datos")
    print("5. Guardar base de datos")
    print("6. Salir\n")

    # Función para seleccionar una opcion
    opcion = seleccion_de_opcion("Ingrese una opcion: ")
    time.sleep(0.5)
    e()

    # Opción 1
    if int(opcion) == 1:
        Separadores("Registro de nuevo socio")
        e()

        print("Datos personales\n")

        ## Ingreso de datos
        nombre = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")

        ## Validación del correo
        while True:
            correo = input("Ingrese su correo electronico: ")
            if es_correo_valido(correo):
                break

        e()
        iniciador('Cargando nueva informacion','Informacion actualizada.')
        e()

        print("Inversion")
        e()

        ## Validación de la fecha
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
        if int(opcion_cripto)==1:
            moneda="Bitcoin"
        if int(opcion_cripto)==2:
            moneda="Etherium"
        if int(opcion_cripto)==3:
            moneda="Dogecoin"
        if int(opcion_cripto)==4:
            moneda="Binance"
        # Datos a almacenar en las matrices
        monto_inversion = monto_de_inversion()

        #Llenando el diccionario  cryptos_mes
        mes_num=int(fecha_inversion.split("/")[1])
        if mes_num==1:
            mes="Enero"
        if mes_num==2:
            mes="Febrero"
        if mes_num==3:
            mes="Marzo"
        if mes_num==4:
            mes="Abril"
        if mes_num==5:
            mes="Mayo"
        if mes_num==6:
            mes="Junio"
        if mes_num==7:
            mes="Julio"
        if mes_num==8:
            mes="Agosto"
        if mes_num==9:
            mes="Septiembre"
        if mes_num==10:
            mes="Octubre"
        if mes_num==11:
            mes="Noviembre"
        if mes_num==12:
            mes="Diciembre"

        cryptos_mes[mes][moneda]+=int(monto_inversion)
        data1=pd.DataFrame(cryptos_mes)



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
        iniciador('Guardando informacion','Informacion guardada.')
        e()

        Separadores("Fin de registro")

        # Funcion para volver al menú
        volver_menu()
        e()

    #Opcion 2
    if int(opcion) == 2:

        Separadores("Lista de activos digitales")

        print("1. Tabla de inversiones")
        print("2. Estadisticas mensuales")
        print("3. Regresar al menú principal")
        e()
        while True:
            opcion_lista_activos = input("Ingrese una opcion:")
            if opcion_lista_activos.isdigit():
                if 1<= int(opcion_lista_activos) <=3:
                    break
        if int(opcion_lista_activos) == 1:
                print("El fondo mutuo en Bitcoin es:", montos_de_criptomoneda[0])
                print("El fondo mutuo en Etherium es:", montos_de_criptomoneda[1])
                print("El fondo mutuo en Dogecoin es:", montos_de_criptomoneda[2])
                print("El fondo mutuo en Binance es:", montos_de_criptomoneda[3])
        if int(opcion_lista_activos) == 2:
                print(data1.head())
        if int(opcion_lista_activos) == 3:
            volver_menu_version2("3")

        print(63*"-")

        e()

    #Opción 3
    if int(opcion) == 3:

        Separadores("Lista de socios")

        # transpuesta
        lista_transpuesta_socios = transponer(lista_socios)[:]

        # IMPRESION DE MATRIZ
        imprimir(lista_transpuesta_socios)
        # IMPRESION DE MATRIZ ---CAMBIAR A FUNCION
        print(63*"-")

        volver_menu()
        e()

    #Opción 4
    if int(opcion) == 4:
        print("Leer base de datos")
        volver_menu()

    #Opción 5
    if int(opcion) == 5:
        print("Guardar base de datos")
        volver_menu()

    #Opción 6
    if int(opcion) == 6:
        iniciador('Cerrando el programa','')
        Separadores("GRACIAS POR INVERTIR EN CRYPTO CORPORATION, VUELVA PRONTO :D")

        break
