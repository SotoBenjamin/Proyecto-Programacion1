def transponer(matrix):
    """
    Calcula la transpuesta de una matriz
    """
    transpuesta=[]
    for i in range(len(matrix[0])):
        transpuesta.append([])
        for j in range(len(matrix)):
            transpuesta[i].append(matrix[j][i])
    return transpuesta

def imprimir(lista):
    """
    Imprime la matriz
    """
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            print('{:<15}'.format('{:>5}'.format(lista[i][j])), end=" ")
        print()