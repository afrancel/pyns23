preguntaUsuario = input("Ingrese un ingrediente")

listaIngredientes = ['harina', 'mantequilla', 'leche', 'canela']

if listaIngredientes.count(preguntaUsuario) > 0:
    print('El dato ingresado' + str(preguntaUsuario) + 'si existe')
else:
    print('El dato ingresado' + str(preguntaUsuario) + 'no existe')