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
    Usar expresiones regulares para ver si es un correo electrónico válido en Python
    Recuerda importar el módulo re

    Una expresión regular más precisa es:
    r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    """

    expresion_regular = r'[a-z0-9\-_\.]+[@][a-z]+[.][a-z]{1,3}'

    return re.match(expresion_regular, correo) is not None

def es_fecha_valida(fecha):
    """
    Valida una fecha ; para ser valida la fecha debe tener el siguiente formato
    dd/mm/yyy . Considera años bisiestos
    """
    lista=fecha.split("/")
    bool1=False
    bool2=False
    bool3=False
    if len(lista)==3:
        bool1=True
    if len(lista[0])==2 and len(lista[1])==2 and len(lista[2])==4:
         bool2=True
    dia=int(lista[0])
    mes=int(lista[1])
    anio=int(lista[2])
    if mes==1:
        if 1<=dia<=31:
            bool3=True
    if mes==2:
        if anio%4==0 and (anio%100!=0 or anio%400==0):
            if 1<=dia<=29:
                bool3=True
        else:
            if 1<=dia<=28:
                bool3=True
    if mes==3:
        if 1<=dia<=31:
            bool3=True
    if mes == 4:
        if 1 <= dia <= 30:
            bool3 = True
    if mes == 5:
        if 1 <= dia <= 31:
            bool3 = True
    if mes == 6:
        if 1 <= dia <= 30:
            bool3 = True
    if mes == 7:
        if 1 <= dia <= 31:
            bool3 = True
    if mes == 8:
        if 1 <= dia <= 31:
            bool3 = True
    if mes == 9:
        if 1 <= dia <= 30:
            bool3 = True
    if mes == 10:
        if 1 <= dia <= 31:
            bool3 = True
    if mes == 11:
        if 1 <= dia <= 30:
            bool3 = True
    if mes == 12:
        if 1 <= dia <= 31:
            bool3= True
    return bool1 and bool2 and bool3
print(es_fecha_valida("29/02/2004"))


