#PRIMER NUMERO INGRESADO POR EL USUARIO
primero = input('Ingrese primer numero')

#PRIMER NUMERO VALIDACIÓN
try: primero = int(primero)
except: primero = 'error'

if primero == 'error':
    print('El dato ingresado no es un numero')
    quit()

#PRIMER NUMERO INGRESADO POR EL USUARIO
segundo = input('Ingrese segundo numero')

#SEGUNDO NUMERO VALIDACIÓN
try: segundo = int(segundo)
except: segundo = 'error'

if segundo == 'error':
    print('El dato ingresado no es un numero')
    quit()

#OPERACIÓN A REALIZAR
operacion = input('Seleccione operación a realizar')
if operacion == '+':
    print('suma =', primero + segundo)
elif operacion == '-':
    print('Resta =', primero - segundo)
elif operacion == '*':
    print('Multiplicación =', primero * segundo)
elif operacion == '/':
    print('Division =', primero / segundo)
else:
    print('El simbolo ingresado es erróneo')

#--------------------------------------------
#EVALUACIONS PREVIAS

#if primero == 'error' or segundo == 'error':
#    print('Alguno de los datos ingresados no son números')
#else:
#    print(primero + segundo)