#def saludo():
#    print("Buen día")

#def saludoUsuario(nombreUsuario):
#    print('Hola Usuario:',nombreUsuario)

#saludoUsuario('Francel')
#saludo()


#def nombreCompleto(*nombre):
#    print('Hola:',nombre)
#
#nombreCompleto('francel','acevedo')

#def nombreCompleto(apellido,nombre):
#    print('Hola:',nombre,apellido)
#
#nombreCompleto(nombre='francel',apellido='acevedo')

#def hola(**kwargs):
#    print('Hola',kwargs['nombre'],kwargs['apellido'],kwargs['apellidos'])
#
#hola(nombre='francel',apellido='emilio',apellidos='acevedo')

#def parametroDefault(argumento = 'default'):
#    print(argumento)

#parametroDefault('le agregue algo')
#parametroDefault()

def funcionLista(listaNombres):
    for el in listaNombres:
        print(el)

#funcionLista(['Luis','Pedro'])

#LOS VALORES CUANDO LOS RETORNAMOS, DEBEMOS MOSTRARLOS A TRAVÉS DE UNA VARIABLE

def concatenaNombres(listaNombres):
    i = ''
    for el in listaNombres:
        i = i + 'Paciente: ' + el + '\n'
    return i

nombres = concatenaNombres(['Pedro','Luis','Carlos'])
print(nombres)

