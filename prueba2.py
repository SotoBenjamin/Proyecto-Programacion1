def es_fecha_valida(fecha):
    '''
    Esta función valida si la fecha es correcta.
    Para ello corrobora que la fecha tenga el formato dd/mm/yyyy.
    Además, corrobora que tanto el día, mes y año sean valores coherentes considerando años bisiestos
    '''

    bool = 0
    veredicto = False
    if "/" in fecha:
        if len(fecha) == 10:
            bool += 1
        lista = fecha.split("/")
        if lista[0].isdigit() and lista[1].isdigit() and lista[2].isdigit():
            bool += 1
            if len(lista[0]) == 2 and len(lista[1]) == 2 and len(lista[2]) == 4:
                bool += 1
            dia = int(lista[0])
            mes = int(lista[1])
            anio = int(lista[2])
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                if 1 <= dia <= 31:
                    bool += 1
            if mes in [4, 6, 9, 11]:
                if 1 <= dia <= 30:
                    bool += 1
            if mes == 2:
                if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
                    if 1 <= dia <= 29:
                        bool += 1
                else:
                    if 1 <= dia <= 28:
                        bool += 1
            if anio >= 1800:
                bool += 1
            if bool == 5:
                return True
            if bool != 5:
                return False
    else:
        return False

fecha_inversion="29/02/2022"
print(es_fecha_valida(fecha_inversion))