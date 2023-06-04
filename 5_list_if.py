#Calculadora
#validación después de pedir los datos
#validación en cada ingreso y si no cumple exit()

#errores
error = "Uno de los números ingresados no es un número"
errordos = "El dato ingresado no es un número. Sesión cerrada"
errortres = "El símbolo ingresado no es correcto"

primer = input("Ingrese 1er número: ")
try: primer = int(primer)
except: primer = error
if primer == error:
    print (errordos)
    exit()

segund = input("Ingrese 2do número: ")
try: segund = int(segund)
except: segund = error
if segund == error:
    print (errordos)
    exit()

operacion = input("Ingrese operacion: ")
if operacion == ("+"):
    resultado = primer + segund
elif  operacion == ("-"):
    resultado = primer - segund
elif  operacion == ("*"):
    resultado = primer * segund
elif  operacion == ("/"):
    resultado = primer / segund
else:
    print(errortres)

print("El resultado es igual a: ", resultado)