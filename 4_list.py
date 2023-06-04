#ejercicios, solicitar datos al usuario
#01. Un arreglo que tiene una lista de opciones
#02. Intentar adivinar cuales datos hay

dato = input("Introduzca un Dato: ")
lista = ["bike","rueda","montana"]

if lista.count(dato):
    print(dato, " si está en esta lista")
else:
    print(dato, " no está en esta lista")