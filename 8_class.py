class Dr:
    def __init__(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
    def saludo(self):
        print('El nombre del doctor es', self.nombre)

doctor = Dr('Juan','Pablo','Ginecologo')