#Tenemos permiso de escritura (append), no se sobreescribirá nada
contenido = open('py11_archivos.txt', 'a')

#agrego cotenido a través de un input y lo agrego con el método .write()
nuevoTexto = input ("Agregue un nuevo texto: ")
contenido.write("\n"+ nuevoTexto)

#cierro el archivo
contenido.close()

#imprimo el archivo, aqui no hay permisos, solo imprimo el contenido
#use otra variable para imprimir el contenido
leerArchivo = open('py11_archivos.txt')
print(leerArchivo.read())