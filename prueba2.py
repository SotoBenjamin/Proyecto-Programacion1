from funciones import *
import pandas as pd
import matplotlib.pyplot as plt
import plotly as plot
cryptos_mes={
"Enero":{"Bitcoin":600 , "Etherium":900 , "Dogecoin":300 ,"Binance":400},
"Febrero":{"Bitcoin":230 , "Etherium":500 , "Dogecoin":700 ,"Binance":200},
"Marzo":{"Bitcoin":1000 , "Etherium":340 , "Dogecoin":3450 ,"Binance":2540},
"Abril":{"Bitcoin":900 , "Etherium":600 , "Dogecoin":3450 ,"Binance":3450},
"Mayo":{"Bitcoin":100 , "Etherium":200 , "Dogecoin":300 ,"Binance":400},
"Junio":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Julio":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Agosto":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Septiembre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Octubre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Noviembre":{"Bitcoin":0 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
"Diciembre":{"Bitcoin":100 , "Etherium":0 , "Dogecoin":0 ,"Binance":0},
}
print()
data=pd.DataFrame(cryptos_mes)
print(data)


print(grafico_circular("Noviembre",cryptos_mes))

#bitcoin=data.iloc[[0],:]
#print(bitcoin)
#datos_enero.plot.pie()
#plt.show()
#datos_enero.plot.barh()
#plt.show()

data["Noviembre"].plot(kind="pie")
plt.show()
