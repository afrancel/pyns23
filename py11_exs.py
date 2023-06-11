

#######################################
import os

file = "registroprueba4.txt"

if os.path.exists(file):
    print("archivo existe")
else:
    print ("Archivo no existe, pero ha sido creado. Ahora procedemos a agregar el contenido", end="\n")
    print ("El contenido se muestra a continuación", end="\n")

def nuevoUsuario(nombre,apellido):
    archivo = open(file,'a')
    archivo.write(nombre+' '+apellido)
    archivo.close()

nuevoUsuario('Francel','Acevedo')

leerArchivo = open(file)
print(leerArchivo.read())