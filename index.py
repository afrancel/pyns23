#if 5 > 3:
#    print("5 es mayor a 3") #print if condition is true

#if 3 > 5:
#    print('Esto no se imprimirá') #la condicion no se cumple, por lo tanto no se imprimirá

#a = 3*20
#b = 2*5
#c = (a/b)**2
#print(c) #Operación explicada: ((3*20)/(2*5))2

#nombre, apellido, edad = 'francel', 'acevedo', 37
#print(nombre, apellido, edad)

#color1 = color2 = color3 = 'color verde'
#print(color1)
#print(color1,color2)

#metalesPreciosos = ('oro','diamante','petroleo')
#print("Su busqueda se encuentra en la posición " + str(metalesPreciosos.index('diamante')))

#for i in range(2,4):
#    print(i)

bicicleta = {
    "ruedas": 2,
    "color":	"rojo",
    "modelo": "cannondale"
}

bicicleta['frenos'] = 'Si'
bicicleta['suspension'] = 'delanterada'
bicicleta.pop('frenos')


#print('\n' + 'bicicleta es igual a:' + '\n' + str(bicicleta))

#del bicicleta['suspension']
#print('\n' + 'bicicleta es igual a:' + '\n' + str(bicicleta))

#bicicleta['frenos'] = 'vbrake'
#print('\n' + 'bicicleta es igual a:' + '\n' + str(bicicleta))

#bicicletados = bicicleta.copy()
#bicicletados.pop('color')

#print('\n' + 'bicicleta es igual a:' + '\n' + str(bicicleta))
#print('\n' + 'bicicleta dos es igual a:' + '\n' + str(bicicletados))

#bicicleta.clear()

#print('\n' + 'bicicleta es igual a:' + '\n' + str(bicicleta))
#print('\n' + 'bicicleta dos es igual a:' + '\n' + str(bicicletados))

#bicicletaTres = dict(bicicleta)

#print('\n' + 'bicicleta es igual a:' + '\n' + str(bicicleta))
#print('\n' + 'bicicleta dos es igual a:' + '\n' + str(bicicletados))
#print('\n' + 'bicicleta Tres es igual a:' + '\n' + str(bicicletaTres))


#Felix = {
#    'Nombre': 'Felix',
#    'Edad': 4
#}
#
#Bruno = {
#    'Nombre':'Bruno',
#    'Edad': 8
#}

#gatitos = {

#    'Felix': Felix,
#    'Bruno': Bruno
#}

#print(gatitos)

#usuario = dict(nombre="Francel Acevedo", edad=38, empleo="Desarrollador")
#print(usuario)

#print(usuario['nombre'])

#usuario.pop('edad')
#print(usuario)

#usuario['nombre'] = 'Luis Acevedo'
#print(usuario)

#usuario['Auto'] = 'Renault Kwid'