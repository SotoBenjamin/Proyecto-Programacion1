import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta

# fecha = "01/06/2022"
# lista = fecha.split("/")
# tupla = (lista[2], lista[1], lista[0])
# fecha_compra = "-".join(tupla)
#
# print(fecha_compra)

# # Instalar pandas_datareader
# import pip
# pip.main(['install', 'pandas_datareader'])

# Buscar la información de la moneda
"""
BITCOIN = BTC-USD
ETHERIUM = ETH-USD
DOGECOIN = DOGE-USD
BINANCE = BNB-USD
"""

data = web.DataReader("BTC-USD", data_source="yahoo", start="2021-06-01")


# Utilizar solo el precio de cierre de la moneda
data = data.iloc[:, 3]

# Precio de compra
precio_compra = data["2022-06-10"]
print("Precio de compra:", precio_compra)

# Precio de venta (siempre es el día anterior al actual)
precio_venta = data["2022-07-01"]
print("Precio de venta:", precio_venta)

# Inversión
invirtio = 10000
print("Inversión:", invirtio)

# Dinero_actual con la fórmula
"""
            Dinero      Valor de la crypto en determinado dia
Compra:    Inversion             precio_de_compra
Venta:        x                   precio_de_venta

Fórmula:
        x = Inversion*precio_de_venta/precio de compra
"""

dinero_actual = invirtio*precio_venta/precio_compra

print("Dinero actual:", dinero_actual)

# Ganancias o pérdidas
if dinero_actual > invirtio:
    print("Hubo ganancias")
    ganancia = dinero_actual - invirtio
    print("Se ganó", ganancia)
else:
    print("Hubo pérdidas")
    perdida = invirtio - dinero_actual
    print("Se perdió", perdida)



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


# print(estado_de_inversion("Bitcoin","03/06/2022",10000))


