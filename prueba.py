#import re

#def es_correo_valido(correo):
#    """
#    Usar expresiones regulares para ver si es un correo electrónico válido en Python
#    Recuerda importar el módulo re
#
#    Una expresión regular más precisa es:
#    r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
#    """

#    expresion_regular = r'[a-z0-9\-_.]+[@][a-z\-_.]+[.][a-z]{2,3}'

#    return re.match(expresion_regular, correo) is not None




#cadena=input("correo:")
#print(es_correo_valido(cadena))

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
        if mes == (1 or 3 or 5 or 7 or 8 or 10 or 12):
            if 1 <= dia <= 31:
                bool+=1
        if mes == (4 or 6 or 9 or 11):
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

while True:
    fecha = input("fecha:")
    print(es_fecha_valida(fecha))
    if es_fecha_valida(fecha):
        break
