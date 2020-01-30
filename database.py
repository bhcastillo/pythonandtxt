import sqlite3
from escribirtxt import validoTxt, noClienteTxt, sinSaldoTxt, vaciarTxt
   
def consulta(Num_identifica): 
   sqlselect=(Num_identifica,)
   Conexion = sqlite3.connect("db.db")
   Cursor = Conexion.cursor()
   Cursor.execute("SELECT * FROM usuario where Num_identifica=?",sqlselect)
   
   sql = Cursor.fetchall()
   if sql:
      restarsaldo=10000
      for productos in sql:
         saldo=productos[8]
         print ("su saldo es:",saldo)
         if saldo <= restarsaldo:
            sinSaldoTxt()
            vaciarTxt()
            print('saldo insuficiente para realizar transacción')
            Conexion.commit()
            Conexion.close()
            return (saldo)

         else:
            saldo = saldo - restarsaldo
            valuesupdate=(saldo,Num_identifica,)
            Cursor.execute("Update usuario set saldo=? where Num_identifica=?",valuesupdate)
            print("transacción exitosa. su nuevo saldo es:",saldo)
            print("\n")
            validoTxt(saldo)
            vaciarTxt()
            Conexion.commit()
            Conexion.close()
            return (saldo)
   else:
      vaciarTxt()
      noClienteTxt()
      return(0)
      
                
   #Cursor.execute("INSERT INTO usuario VALUES ('c.c.',1051241032,'juan','calle 5 # 4-3',1,2,3212343221,1002,500000)")
   

