import re
import time

#Matriz Transpuesta
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

def seleccion_de_opcion(mensaje):
    '''
    Función con un bucle While que recibe como parámetro el mensaje que se mostrará en el input
    '''

    while True:
        opcion = input(mensaje)
        if opcion.isdigit():
            if 1 <= int(opcion) <= 4:
                break

    return opcion

def e():
    '''
    Funcion para dar espacios y no poner muchos print()
    '''
    print()

def monto_de_inversion():
    '''
    Funcion para el monto inversion donde el monto debe ser mayor a 0
    '''

    while True:
        monto_inversion = input("Igrese el monto en soles a invertir: ")
        if monto_inversion.isdigit():
            if int(monto_inversion) >= 1:
                break

    return monto_inversion


def volver_menu():
    '''
    Funcion para volver al menú
    '''

    while True:
        opcion_volver_menu = input("Ingrese 0 para regresar al menu principal: ")
        if opcion_volver_menu.isdigit():
            if int(opcion_volver_menu) == 0:
                e()
                print("Regresando al menú principal, espere por favor...")
                time.sleep(3)
                break

def es_correo_valido(correo):
    """
    Librería re (Regular expresions, RegEx, Expresiones regulares)
    - RegEx es una librería que se utiliza para validar strings mediante la creación de ciertos patrones
    - Se puede usar expresiones regulares para ver si es un correo electrónico válido en Python

    Formato de correo:
    usuario@dominio.extension

    Metacarácteres RegEx:
    r''      --> comprueba que el string que se está ingresando es una expresión regular
    ^        --> indica que la comprobación inicia desde ahí
    [a-z]    --> carácteres alfanuméricos ingleses
    [0-9]    --> carácteres numéricos
    [\-_ \.] --> carácteres "._-" (se utiliza el backslash para que no se interprete como un metacaracter)
    +        --> el patrón colocado anteriormente al + se puede repetir ilimitadas veces
    [@]      --> comprueba la existencia de un @
    [.]      --> comprueba la exixtencia de un .
    {2,3}    --> comprueba que la extención del string tiene 2 a 3 carácteres
    ()       --> encierra cierto patrón entre paréntesis para separarlo
    ?        --> el patrón colocado anteriormente al ? se puede repetir una o ninguna vez
    $        --> indica que la comprobación termina hasta ahí
    """

    expresion_regular = r'^[a-z0-9\-_\.]+[@][a-z]+[.][a-z]{2,3}([.][a-z]{2,3})?$'

    return re.match(expresion_regular, correo) is not None

def imprimir(matriz):
    """
    Imprime la matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print('{:<15}'.format('{:>5}'.format(matriz[i][j])), end=" ")
        print()

def es_fecha_valida(fecha):
    bool = 0
    veredicto = False
    if len(fecha) == 10:
        bool+=1
    lista=fecha.split("/")
    if lista[0].isdigit() and lista[1].isdigit() and lista[2].isdigit():
        bool+=1
        if len(lista[0]) == 2 and len(lista[1]) == 2 and len(lista[2]) == 4:
            bool+=1
        dia = int(lista[0])
        mes = int(lista[1])
        anio = int(lista[2])
        if mes in [1,3,5,7,8,10,12]:
            if 1 <= dia <= 31:
                bool+=1
        if mes in [4,6,9,11]:
            if 1 <= dia <= 30:
                bool+=1
        if mes == 2:
            if anio % 4 == 0 and (anio % 100 !=0 or anio % 400 == 0):
                if 1 <= dia <= 29:
                    bool+=1
            else:
                if 1 <= dia <= 28:
                    bool+=1
        if anio >=1800:
            bool+=1
        if bool==5:
            veredicto = True
        if bool!=5:
            veredicto = False
    return veredicto