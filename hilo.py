import threading
import time
from database import consulta
from main import iniciarprograma

def ejecutar():
    i=0
    while i< 5:

        iniciarprograma()
        time.sleep(4)
        #i=i+1

if __name__ == '__main__':
    thread = threading.Thread(target=ejecutar)
    thread.start()