#mayor detalle en
#https://colab.research.google.com/drive/1mC8HOns-RCQcUO_CGR8lDa9xOekeytIo#scrollTo=hSxAwtOEbO9s

import mysql.connector

#Paso1: asigno a una variable, la conexion de la BD
dbpy = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Site2022Lock',
    database='python23'
)

#Paso2: creo un cursor para relacionar base de datos y logica del sistema a crear
cursor = dbpy.cursor()

#Paso3: Hago la consulta a la BD / método execute
cursor.execute('select * from usuario')

#Paso4: Hago la consulta a la BD / método fetchall
resultado = cursor.fetchall()

#Paso5: Imprimimos los resultados
print(resultado)

#Paso6: Suponiendo que no me acuerdo los datos de la BD, la estructura
#cursor.execute('show create table usuario')

#Paso7: Agregar datos a la BD
sql = 'insert into usuario (email,telefono,edad) values (%s,%s,%s)'
values = ('correocuatro@gmail.com',96385241,38)

#Paso8: Ejecutar sql + values
#Si ejecuto la siguiente línea sin ejecutar el paso 10, los datos no se guardarán
cursor.execute(sql, values) #probado y efectivamente está en blanco

#Paso9: comento el ingreso de datos para que quede registrado
dbpy.commit() #comento los cambios
print(cursor.rowcount," fila creada") #Imprime las filas afectadas, la cantidad

#Paso10: Imprimimos los resultados
cursor.execute('select * from usuario')
resultado = cursor.fetchall()
print(resultado)