
from leertxt import LecturaTxt, existeTxt
from database import consulta
from escribirtxt import vaciarSalidaTxt
#import escribirtxt
#import dbmysql
def iniciarprograma():
    estado = existeTxt()
    if estado == True:
        linea1=LecturaTxt()
        lista_string = linea1.split(sep=',')
        lista_enteros= [int(x) for x in lista_string]
        Num_identifica= lista_enteros[3]
        print("consulta usuario ")
        print(Num_identifica)
        resultado = consulta(Num_identifica)
        if resultado == 0:
            print("usuario no existe")

    else:
        #vaciarSalidaTxt()
        print('archivo Entrada vacio')
        

iniciarprograma()
#consulta(Num_identifica)


