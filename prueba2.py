from funciones import *
import pandas as pd
import matplotlib.pyplot as plt

cryptos_mes={
"Enero":{"Bitcoin":900 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Febrero":{"Bitcoin":500 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Marzo":{"Bitcoin":1000 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Abril":{"Bitcoin":300 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Mayo":{"Bitcoin":500 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Junio":{"Bitcoin":500 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Julio":{"Bitcoin":500 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Agosto":{"Bitcoin":500 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Septiembre":{"Bitcoin":500 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Octubre":{"Bitcoin":600 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Noviembre":{"Bitcoin":700 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Diciembre":{"Bitcoin":800 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
}

print(validar_estadistica_anual(cryptos_mes))
data=pd.DataFrame(cryptos_mes)
#print(data)
serie=data.sum()
#print(serie)
serie.plot(kind="barh")
plt.show()
#serie.plot(kind="pie")
#plt.show()



#print(grafico_circular("Noviembre",cryptos_mes))

#bitcoin=data.iloc[[0],:]
#print(bitcoin)

#datos_enero.plot.pie()
#plt.show()
#datos_enero.plot.barh()
#plt.show()

#data["Noviembre"].plot(kind="pie")
#plt.show()
