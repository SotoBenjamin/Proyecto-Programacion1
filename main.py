# Lugar para poner los import
from funciones import *
iniciador('Iniciando programa del servidor', 'Carga con exito.')
e()

# Variables generales
opcion_volver_menu = 0
montos_de_criptomoneda = [0, 0, 0, 0]
t = 1
lista_socios = [["Nombre"], ["Codigo"], ["Moneda"], ["Monto"], ["Fecha"]]
cryptos_mes = {
    "Enero": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Febrero": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Marzo": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Abril": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Mayo": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Junio": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Julio": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Agosto": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Septiembre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Octubre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Noviembre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Diciembre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    }
# diccionario de inversiones por moneda y mes
data1 = pd.DataFrame(cryptos_mes)
mes = ""
moneda = ""
socio_cryptos_mes = {
    "enero": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Febrero": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Marzo": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Abril": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Mayo": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Junio": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Julio": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Agosto": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Septiembre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Octubre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Noviembre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    "Diciembre": {"Bitcoin": 0, "Etherium": 0, "Dogecoin": 0, "Binance": 0},
    }
# diccionario de socios por moneda y mes
data2 = pd.DataFrame(cryptos_mes)
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
    print("6. Estado de inversiones")
    print("7. Salir\n")

    # Función para seleccionar una opcion
    opcion = seleccion_de_opcion("Ingrese una opcion: ")
    time.sleep(0.5)
    e()

    # Opción 1 - Agregar nuevo socio
    if int(opcion) == 1:
        Separadores("Registro de nuevo socio")
        e()

        print("Datos personales\n")

        # Ingreso de datos
        nombre = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")

        # Validación del correo
        while True:
            correo = input("Ingrese su correo electronico: ")
            if es_correo_valido(correo):
                break

        e()
        iniciador('Cargando nueva informacion', 'Informacion actualizada.')
        e()

        print("Inversion")
        e()

        # Validación de la fecha
        while True:
            fecha_inversion = input("Ingrese la fecha: ")
            if es_fecha_valida(fecha_inversion):
                lista_socios[4].append(fecha_inversion)
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
        if int(opcion_cripto) == 1:
            moneda = "Bitcoin"
        if int(opcion_cripto) == 2:
            moneda = "Etherium"
        if int(opcion_cripto) == 3:
            moneda = "Dogecoin"
        if int(opcion_cripto) == 4:
            moneda = "Binance"
        # Datos a almacenar en las matrices
        monto_inversion = monto_de_inversion()

        # Llenando el diccionario  cryptos_mes
        mes_num = int(fecha_inversion.split("/")[1])
        if mes_num == 1:
            mes = "Enero"
        if mes_num == 2:
            mes = "Febrero"
        if mes_num == 3:
            mes = "Marzo"
        if mes_num == 4:
            mes = "Abril"
        if mes_num == 5:
            mes = "Mayo"
        if mes_num == 6:
            mes = "Junio"
        if mes_num == 7:
            mes = "Julio"
        if mes_num == 8:
            mes = "Agosto"
        if mes_num == 9:
            mes = "Septiembre"
        if mes_num == 10:
            mes = "Octubre"
        if mes_num == 11:
            mes = "Noviembre"
        if mes_num == 12:
            mes = "Diciembre"

        cryptos_mes[mes][moneda] += int(monto_inversion)
        data1 = pd.DataFrame(cryptos_mes)

        socio_cryptos_mes[mes][moneda] += 1
        data2 = pd.DataFrame(socio_cryptos_mes)

        lista_socios[0].append(nombre)
        user = "User" + str(t)
        lista_socios[1].append(user)
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
        iniciador('Guardando informacion', 'Informacion guardada.')
        e()

        print(f"Su código de usuario es: {user}")
        time.sleep(2)
        e()

        Separadores("Fin de registro")

        # Funcion para volver al menú
        volver_menu()
        e()

    # Opcion 2 - Lista de activos digitales
    if int(opcion) == 2:
        while True:
            Separadores("Lista de activos digitales")
            e()
            print("1. Tabla de inversiones")
            print("2. Estadisticas mensuales")
            print("3. Regresar al menú principal")
            e()
            while True:
                opcion_lista_activos = input("Ingrese una opcion:")
                if opcion_lista_activos.isdigit():
                    if 1 <= int(opcion_lista_activos) <= 3:
                        break
            if int(opcion_lista_activos) == 1:
                print("El fondo mutuo en Bitcoin es:", montos_de_criptomoneda[0])
                print("El fondo mutuo en Etherium es:", montos_de_criptomoneda[1])
                print("El fondo mutuo en Dogecoin es:", montos_de_criptomoneda[2])
                print("El fondo mutuo en Binance es:", montos_de_criptomoneda[3])
                e()
                volver_menu_lista_activos()

            if int(opcion_lista_activos) == 2:
                while True:
                    Separadores("Estadisticas Mensuales")
                    e()
                    e()
                    print("1. Cryptos en Enero")
                    print("2. Cryptos en Febrero")
                    print("3. Cryptos en Marzo")
                    print("4. Cryptos en Abril")
                    print("5. Cryptos en Mayo")
                    print("6. Cryptos en Junio")
                    print("7. Cryptos en Julio")
                    print("8. Cryptos en Agosto")
                    print("9. Cryptos en Septiembre")
                    print("10. Cryptos en Octubre")
                    print("11. Cryptos en Noviembre")
                    print("12. Cryptos en Diciembre")
                    print("13. Cryptos General")
                    print("14.Volver a La lista de activos digitales")
                    e()
                    e()
                    while True:
                        opcion_estadisticas_mensuales = input("Ingrese una opcion:")
                        if opcion_estadisticas_mensuales.isdigit():
                            if 1 <= int(opcion_estadisticas_mensuales) <= 14:
                                break
                    if int(opcion_estadisticas_mensuales) == 1:

                        if grafico_circular("Enero", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Enero")
                            data1["Enero"].plot(kind="barh")
                            plt.show()
                            data1["Enero"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 2:

                        if grafico_circular("Febrero", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Febrero")
                            data1["Febrero"].plot(kind="barh")
                            plt.show()
                            data1["Febrero"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 3:

                        if grafico_circular("Marzo", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Marzo")
                            data1["Marzo"].plot(kind="barh")
                            plt.show()
                            data1["Marzo"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 4:
                        if grafico_circular("Abril", cryptos_mes):
                            Separadores("Se muestra el gráfico de barras para el mes de Abril")
                            data1["Abril"].plot(kind="barh")
                            plt.show()
                            data1["Abril"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")

                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 5:

                        if grafico_circular("Mayo", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Mayo")
                            data1["Mayo"].plot(kind="barh")
                            plt.show()
                            data1["Mayo"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 6:

                        if grafico_circular("Junio", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Junio")
                            data1["Junio"].plot(kind="barh")
                            plt.show()
                            data1["Junio"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 7:

                        if grafico_circular("Julio", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Julio")
                            data1["Julio"].plot(kind="barh")
                            plt.show()
                            data1["Julio"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 8:

                        if grafico_circular("Agosto", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Agosto")
                            data1["Agosto"].plot(kind="barh")
                            plt.show()
                            data1["Mayo"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 9:

                        if grafico_circular("Septiembre", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Septiembre")
                            data1["Septiembre"].plot(kind="barh")
                            plt.show()
                            data1["Septiembre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 10:
                        if grafico_circular("Octubre", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Octubre")
                            data1["Octubre"].plot(kind="barh")
                            plt.show()
                            data1["Octubre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 11:
                        if grafico_circular("Noviembre", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Noviembre")
                            data1["Noviembre"].plot(kind="barh")
                            plt.show()
                            data1["Noviembre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 12:
                        if grafico_circular("Diciembre", cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Diciembre")
                            data1["Diciembre"].plot(kind="barh")
                            plt.show()
                            data1["Diciembre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos para este mes")
                        volver_menu_Estadisticas_mensuales()
                    if int(opcion_estadisticas_mensuales) == 13:
                        if validar_estadistica_anual(cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras del análisis general de Cryptos")
                            data1.sum().plot(kind="barh")
                            plt.show()
                            data1.sum().plot(kind="pie")
                            plt.show()
                        else:
                            print("No se ha ingresado ningun dato")
                        volver_menu_Estadisticas_mensuales()

                    if int(opcion_estadisticas_mensuales) == 14:
                        iniciador("Volviendo a La lista de activos digitales", "Operación realizada con éxito")
                        break
            if int(opcion_lista_activos) == 3:
                iniciador("Volviendo al Menú Principal", "Operación realizada con éxito")
                break

            print(63 * "-")

            e()

    # Opción 3 - Lista de socios
    if int(opcion) == 3:
        while True:
            Separadores("Lista de socios")

            print("1. Tabla de socios")
            print("2. Estadísticas mensuales")
            print("3. Regresar al menú principal")
            e()
            while True:
                opcion_lista_socios = input("Ingrese una opcion:")
                if opcion_lista_socios.isdigit():
                    if 1 <= int(opcion_lista_socios) <= 3:
                        break
            if int(opcion_lista_socios) == 1:
                # transpuesta
                matrix=lista_socios[:]
                lista_transpuesta_socios = transponer(matrix)[:]
                lista_nueva = np.array(lista_transpuesta_socios)

                # IMPRESION DE MATRIZ
                imprimir(lista_nueva[:,:4])

                e()
                volver_menu_socios()
            if int(opcion_lista_socios) == 2:
                while True:
                    Separadores("Estadisticas Mensuales")
                    e()
                    e()
                    print("1. Socios en Enero")
                    print("2. Socios en Febrero")
                    print("3. Socios en Marzo")
                    print("4. Socios en Abril")
                    print("5. Socios en Mayo")
                    print("6. Socios en Junio")
                    print("7. Socios en Julio")
                    print("8. Socios en Agosto")
                    print("9. Socios en Septiembre")
                    print("10. Socios en Octubre")
                    print("11. Socios en Noviembre")
                    print("12. Socios en Diciembre")
                    print("13. Socios General")
                    print("14.Volver a La lista de socios")
                    e()
                    while True:
                        opcion_socios_mensuales = input("Ingrese una opcion:")
                        if opcion_socios_mensuales.isdigit():
                            if 1 <= int(opcion_socios_mensuales) <= 14:
                                break
                    if int(opcion_socios_mensuales) == 1:
                        if grafico_circular("enero", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Enero")
                            data2["enero"].plot(kind="barh")
                            plt.show()
                            data2["enero"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()
                    if int(opcion_socios_mensuales) == 2:
                        if grafico_circular("Febrero", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Febrero")
                            data2["Febrero"].plot(kind="barh")
                            plt.show()
                            data2["Febrero"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 3:
                        if grafico_circular("Marzo", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Marzo")
                            data2["Marzo"].plot(kind="barh")
                            plt.show()
                            data2["Marzo"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 4:
                        if grafico_circular("April", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de April")
                            data2["April"].plot(kind="barh")
                            plt.show()
                            data2["April"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 5:
                        if grafico_circular("Mayo", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Mayo")
                            data2["Mayo"].plot(kind="barh")
                            plt.show()
                            data2["Mayo"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 6:
                        if grafico_circular("Junio", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Junio")
                            data2["Junio"].plot(kind="barh")
                            plt.show()
                            data2["Junio"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 7:
                        if grafico_circular("Julio", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Julio")
                            data2["Julio"].plot(kind="barh")
                            plt.show()
                            data2["Julio"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 8:
                        if grafico_circular("Agosto", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Agosto")
                            data2["Agosto"].plot(kind="barh")
                            plt.show()
                            data2["Agosto"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 9:
                        if grafico_circular("Septiembre", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Septiembre")
                            data2["Septiembre"].plot(kind="barh")
                            plt.show()
                            data2["Septiembre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 10:
                        if grafico_circular("Octubre", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Octubre")
                            data2["Octubre"].plot(kind="barh")
                            plt.show()
                            data2["Octubre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 11:
                        if grafico_circular("Noviembre", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Noviembre")
                            data2["Noviembre"].plot(kind="barh")
                            plt.show()
                            data2["Noviembre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 12:
                        if grafico_circular("Diciembre", socio_cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras para el mes de Diciembre")
                            data2["Diciembre"].plot(kind="barh")
                            plt.show()
                            data2["Diciembre"].plot(kind="pie")
                            plt.show()
                        else:
                            print("No hay datos ingresados para este mes")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 13:
                        if validar_estadistica_anual(cryptos_mes):
                            Separadores("Se muestra el gráfico circular y de barras del análisis general de los Socios")
                            data2.sum().plot(kind="barh")
                            plt.show()
                            data2.sum().plot(kind="pie")
                            plt.show()
                        else:
                            print("No se ha ingresado ningun dato")
                        volver_menu_socios_mensuales()

                    if int(opcion_socios_mensuales) == 14:
                        iniciador("Volviendo a La lista de activos digitales", "Operación realizada con éxito")
                        break

            if int(opcion_lista_socios) == 3:
                iniciador("Volviendo al Menú Principal", "Operación realizada con éxito")
                break
            e()
            print(63*"-")

    # Opción 4 - Leer base de datos
    if int(opcion) == 4:
        Separadores("Leer base de datos")
        e()
        archivo = input("Digite el nombre del archivo:")
        lista_socios = csv_a_matriz(archivo)[:]
        imprimir(lista_socios)
        lista_socios = transponer(lista_socios)[:]

        volver_menu()

    # Opción 5 - Guardar base de datos
    if int(opcion) == 5:
        Separadores("Guardar base de datos")
        e()
        new_matrix = transponer(lista_socios)[:]

        nombre = input("Escribe el nombre del archivo a guardar: ")
        matriz_a_csv(new_matrix, nombre)

        volver_menu()

    # Opción 6 - Estado de inversiones
    if int(opcion) == 6:
        Separadores("Estado de inversiones")
        e()

        ## Crear un While True hasta que encuentre el nombre
        while True:
            usuario = input("Ingrese el codigo de usuario: ")

            result = busqueda_lineal(lista_socios[1], usuario)
            if result[0]:
                iniciador("Buscando usuario", "Usuario encontrado")
                e()
                # Variables del usuario
                user_moneda = lista_socios[2][result[1]]
                user_inversion = int(lista_socios[3][result[1]])
                user_fecha = lista_socios[4][result[1]]

                print(f"Bienvenido, {lista_socios[0][result[1]]}")
                e()
                user_dinero_actual = estado_de_inversion(user_moneda, user_fecha, user_inversion)

                print(f"Su dinero invertido inicialmente fue: {user_inversion} dólares")
                print(f"La moneda invertida es: {user_moneda}")
                time.sleep(1)
                e()

                if user_dinero_actual > user_inversion:
                    print("Estado: Hubo ganancias")
                    ganancia = user_dinero_actual - user_inversion
                    print(f"Se ganó {round(ganancia, 3)} dólares")
                    time.sleep(1)

                    comision = (1 / 100) * ganancia
                    user_ganancia = user_dinero_actual - comision
                    print(f"Su dinero actual es: {round(user_ganancia, 3)} dólares")
                else:
                    print("Estado: Hubo pérdidas")
                    perdida = user_inversion - user_dinero_actual
                    print(f"Se perdió {round(perdida, 3)} dólares")
                    time.sleep(1)

                    print(f"Su dinero actual es: {round(user_dinero_actual, 3)} dólares")
                e()

                iniciador("Calculando la ganancia total del fondo mutuo", "", 0)
                e()

                ganancia_total_fondo_mutuo = 0
                for i in range(1, len(lista_socios[3])):
                    user_moneda = lista_socios[2][i]
                    user_inversion = int(lista_socios[3][i])
                    user_fecha = lista_socios[4][i]

                    user_dinero_actual = estado_de_inversion(user_moneda, user_fecha, user_inversion)

                    if user_dinero_actual > user_inversion:
                        ganancia = user_dinero_actual - user_inversion
                        comision = (1 / 100) * ganancia
                        ganancia_total_fondo_mutuo += comision

                print(f"Ganancia del fondo mutuo: {round(ganancia_total_fondo_mutuo,3)} dólares")
                e()
                break
            elif usuario == "0":
                e()
                iniciador("Cerrando la búsqueda de usuario", '', 2)
                e()
                break
            else:
                iniciador("Buscando usuario", "Usuario no encontrado")
                e()

        volver_menu()

    # Opción 7 - Salir
    if int(opcion) == 7:
        iniciador('Cerrando el programa', '')
        Separadores("GRACIAS POR INVERTIR EN CRYPTO CORPORATION, VUELVA PRONTO :D")


        break