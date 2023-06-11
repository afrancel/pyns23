#open función --> asignada a una variable
contenido = open('py11_archivos.txt')

#open función --> asignada a una variable y permisos
contenido = open('py11_archivos.txt','r') # permiso de solo lectura
contenido = open('py11_archivos.txt','a') # permiso de agregar contenido al final con el método 'append'
contenido = open('py11_archivos.txt','w') # permiso de escritura 'write'

#leer el contenido con el método read(), todo el archivo
print(contenido.read())

#leer el contenido con el método read(), pero linea por linea
print(contenido.readline())
print(contenido.readline())
print(contenido.readline())

#iterar sobre las líneas de contenido
for lineas in contenido:
    print(lineas)

contenido.close()