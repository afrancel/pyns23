#CONSULTAR DATA > Resumen ******************************************************* 
import mysql.connector

dbpy = mysql.connector.connect(host='localhost', user='root', password='Site2022Lock', database='python23')
cursor = dbpy.cursor()
cursor.execute('select * from usuario')
resultado = cursor.fetchall()
print(resultado)

#INGRESAR DATA > Resumen ********************************************************
sql = 'insert into usuario (email,telefono,edad) values (%s,%s,%s)'
values = ('correo@gmail.com',96385241,38)

#ACTUALIZAR DATA > Resumen *****************************************************
sql = 'update usuario set email = %s where id = %s'
values = ('correouno@gmail.com','10')

#ELIMINAR DATA > Resumen *****************************************************
sql = 'delete usuario set email = %s where id = %s'
values = ('correouno@gmail.com','10')

#INSTRUCCIONES COMUNES A TODAS
cursor.execute(sql, values)
dbpy.commit() #comento los cambios
cursor.execute('select * from usuario')
resultado = cursor.fetchall()
print(resultado)