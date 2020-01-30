from  io import open
#modo lectura################
def validoTxt(saldodb):
    frase = "1"+str(saldodb)+"&&&&&&&&&&&"
    archivo_texto = open('archivosalida.txt','w')
    archivo_texto.write(frase)
    archivo_texto.close()

def sinSaldoTxt():
    frase = "0SinSaldo,"
    archivo_texto = open('archivosalida.txt','w')
    archivo_texto.write(frase)
    archivo_texto.close()

def noClienteTxt():
    frase = "0ClientenoExiste,"
    archivo_texto = open('archivosalida.txt','w')
    archivo_texto.write(frase)
    archivo_texto.close()

def vaciarTxt():
    frase = ""
    archivo_texto = open('entrada.txt','w')
    archivo_texto.write(frase)
    archivo_texto.close()

def vaciarSalidaTxt():
    frase = ""
    archivo_texto = open('archivosalida.txt','w')
    archivo_texto.write(frase)
    archivo_texto.close()