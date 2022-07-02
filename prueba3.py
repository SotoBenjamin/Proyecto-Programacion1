import numpy as np


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


def busqueda_lineal(lista, e):
    position = 0
    for i in lista:
        if i == e:
            return True, position
        position += 1
    return False, position

lista_socios = [["Nombre", "Jeffrey", "Juan", "Pablo"], ["Codigo", "User1", "User2", "User3"],
                ["Moneda", "Bitcoin", "Etherium", "Dogecoin"], ["Monto", 10000, 20000, 15000], ["Fecha", "a", "b", "c"]]

lista_transpuesta_socios = transponer(lista_socios)

lista_nueva = np.array(lista_transpuesta_socios)

imprimir(lista_nueva[:, :4])

while True:
    usuario = input("Ingrese el codigo de usuario: ")

    result = busqueda_lineal(lista_socios[1], usuario)
    if result[0]:
        print(f"Bienvenido, {lista_socios[0][result[1]]}")
        user_moneda = lista_socios[2][result[1]]
        user_inversion = lista_socios[3][result[1]]
        user_fecha = lista_socios[4][result[1]]
        break


