#Debemos usar una librería del sistema, importar un modulo
import os

#método remove
#os.remove("py11_archivos_borrar.txt")

#antes de borrar, podemos verificar si existe el archivo
#debo usar el método os.path.exists()

if os.path.exists("py11_archivos_borrar.txt"):
    pregunta = input("¿Desea borrar el archivo? (S/N)")
    if pregunta.lower() == "s":
        os.remove("py11_archivos_borrar.txt")
        print("Archivo eliminado")
    else:
        print("Operación cancelada")
else:
    print("El archivo no existe o ya ha sido eliminado")