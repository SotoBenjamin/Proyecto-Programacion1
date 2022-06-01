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

# def seleccion_de_opcion(mensaje):
#     '''
#     Función con un bucle While que recibe como parámetro el mensaje que se mostrará en el input
#     '''
#
#     while True:
#         opcion = input(mensaje)
#         if opcion.isdigit():
#             if 1 <= int(opcion) <= 4:
#                 break
#
#     return opcion