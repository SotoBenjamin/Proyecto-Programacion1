import numpy as np
import pandas as pd
import pandas_datareader.data as web

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
data = data.iloc[:,3]

# Precio de compra
precio_compra = data["2022-06-10"]
print("Precio de compra:", precio_compra)

# Precio de venta (siempre es el día anterior al actual)
precio_venta = data["2022-06-28"]
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

