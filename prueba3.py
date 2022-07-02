import numpy as np
from datetime import datetime, timedelta
import pandas_datareader.data as web

def transponer(matrix):
    """
    Calcula la transpuesta de una matriz
    """
    transpuesta = []
    for i in range(len(matrix[0])):
        transpuesta.append([])
        for j in range(len(matrix)):
            transpuesta[i].append(matrix[j][i])
    return transpuesta


def imprimir(matriz):
    """
    Imprime la matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print('{:<15}'.format('{:>5}'.format(matriz[i][j])), end=" ")
        print()


def estado_de_inversion(moneda, fecha, inversion):
    # Para obtener el tipo de moneda

    codigo = ""
    if moneda == "Bitcoin":
        codigo = "BTC-USD"
    elif moneda == "Etherium":
        codigo = "ETH-USD"
    elif moneda == "Dogecoin":
        codigo = "DOGE-USD"
    elif moneda == "Binance":
        codigo = "BNB-USD"

    # Para obetener la fecha del precio de compra
    lista = fecha.split("/")
    tupla = (lista[2], lista[1], lista[0])
    fecha_compra = "-".join(tupla)

    # Para obtener la fecha del precio de venta
    now = datetime.now()
    new_date = now + timedelta(days=-1)
    fecha_venta = str(new_date.date())

    # Extracción de las crypto
    data = web.DataReader(codigo, data_source="yahoo", start="2021-06-01")
    data = data.iloc[:, 3]

    precio_compra = data[fecha_compra]
    precio_venta = data[fecha_venta]

    dinero_actual = inversion*precio_venta/precio_compra

    return dinero_actual


def busqueda_lineal(lista, e):
    position = 0
    for i in lista:
        if i == e:
            return True, position
        position += 1
    return False, position


lista_socios = [["Nombre", "Jeffrey", "Juan", "Pablo"], ["Codigo", "User1", "User2", "User3"], ["Moneda", "Bitcoin", "Etherium", "Dogecoin"], ["Monto", 10000, 10000, 10000], ["Fecha", "18/06/2022", "18/06/2022", "18/06/2022"]]

lista_transpuesta_socios = transponer(lista_socios)

lista_nueva = np.array(lista_transpuesta_socios)

imprimir(lista_nueva[:, :4])

# while True:
#     usuario = input("Ingrese el codigo de usuario: ")
#
#     result = busqueda_lineal(lista_socios[1], usuario)
#     if result[0]:
#         # Variables del usuario
#         user_moneda = lista_socios[2][result[1]]
#         user_inversion = int(lista_socios[3][result[1]])
#         user_fecha = lista_socios[4][result[1]]
#
#         print(f"Bienvenido, {lista_socios[0][result[1]]}")
#         user_dinero_actual = estado_de_inversion(user_moneda, user_fecha, user_inversion)
#
#         print(f"Su dinero invertido inicialmente fue: {user_inversion} dólares")
#         print(f"La moneda invertida es: {user_moneda}")
#         print(f"Su dinero actual es: {round(user_dinero_actual, 3)} dólares")
#
#         if user_dinero_actual > user_inversion:
#             print("Hubo ganancias")
#             ganancia = user_dinero_actual - user_inversion
#             print(f"Se ganó {round(ganancia, 3)} dólares")
#         else:
#             print("Hubo pérdidas")
#             perdida = user_inversion - user_dinero_actual
#             print(f"Se perdió {round(perdida, 3)} dólares")
#         break


ganancia_total_fondo_mutuo = 0

for i in range(1, len(lista_socios[3])):
    user_moneda = lista_socios[2][i]
    user_inversion = int(lista_socios[3][i])
    user_fecha = lista_socios[4][i]

    user_dinero_actual = estado_de_inversion(user_moneda, user_fecha, user_inversion)

    if user_dinero_actual > user_inversion:
        print("Hubo ganancias")
        print(user_dinero_actual)

        ganancia = user_dinero_actual - user_inversion
        comision = (1/100)*ganancia
        print(f"comision: {comision}")
        user_ganancia = user_dinero_actual - comision
        print(f"final {user_ganancia}")

        ganancia_total_fondo_mutuo += comision

    else:
        print("Hubo pérdidas")
        print(user_dinero_actual)

    print()

print(f"Ganancia del fondo mutuo: {ganancia_total_fondo_mutuo}")

