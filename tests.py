from jeff_funciones.main_funciones import *

montos_de_criptomoneda = [0, 0, 0, 0]
t = 1
lista_socios = [["Nombre"], ["Codigo"], ["Moneda"], ["Monto"]]
nombre = "Jeffrey"



########################

if int(opcion_cripto) == 1:
    monto_inversion = monto_de_inversion()

    montos_de_criptomoneda[0] += int(monto_inversion)
    lista_socios[0].append(nombre)
    lista_socios[1].append("User" + str(t))
    lista_socios[2].append("Bitcoin")
    lista_socios[3].append(str(monto_inversion))
    t += 1

if int(opcion_cripto) == 2:
    monto_inversion = monto_de_inversion()

    montos_de_criptomoneda[1] += int(monto_inversion)
    lista_socios[0].append(nombre)
    lista_socios[1].append("User" + str(t))
    lista_socios[2].append("Etherium")
    lista_socios[3].append(str(monto_inversion))
    t += 1

if int(opcion_cripto) == 3:
    monto_inversion = monto_de_inversion()

    montos_de_criptomoneda[2] += int(monto_inversion)
    lista_socios[0].append(nombre)
    lista_socios[1].append("User" + str(t))
    lista_socios[2].append("Dogcoin")
    lista_socios[3].append(str(monto_inversion))
    t += 1

if int(opcion_cripto) == 4:
    monto_inversion = monto_de_inversion()

    montos_de_criptomoneda[3] += int(monto_inversion)
    lista_socios[0].append(nombre)
    lista_socios[1].append("User" + str(t))
    lista_socios[2].append("Binance")
    lista_socios[3].append(str(monto_inversion))
    t += 1