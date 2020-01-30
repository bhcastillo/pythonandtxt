from io import open
import  os


def LecturaTxt():
    
    archivo_text = open('entrada.txt','r')
    linea = archivo_text.read()
    return (linea)

def existeTxt():
    if os.stat("Entrada.txt").st_size == 0:
        return False
    else:
        return True
    


##############leer por lineas
#archivo_texto = open("archivo.txt","r")
#texto = archivo_texto.readlines()
#archivo_texto.close()
#print(texto)


##########