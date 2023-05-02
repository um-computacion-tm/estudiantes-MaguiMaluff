class Persona:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class Materia:
    def __init__(self, param_nombre, param_aula, param_horario):
        self.nombre = param_nombre
        self.aula = param_aula
        self.horario = param_horario

class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)

    def cursando(self, Materia):
        self.materias_cursando.append(Materia.nombre)

class Materia:
    def __init__(self, param_nombre, param_aula, param_horario):
        self.nombre = param_nombre
        self.aula = param_aula
        self.horario = param_horario



mate = Materia("Matematica", "7", "3 pm")

alumna_maria = Alumno("Maria", "m.perez@gmail.com", 665544)
print(id(alumna_maria))
print("El nombre es: ", alumna_maria.nombre)
print("El email es: ", alumna_maria.email)
print("El legajo es: ", alumna_maria.numero_alumno)
alumna_maria.asistencia_clase()
alumna_maria.cursando(mate)
print("La alumna fue a clase, su asistencia es: ", alumna_maria.asistencia)
print("La alumna cursa: ", alumna_maria.materias_cursando)
print(id(mate))

profesor_pepe = Profesor("Pepe", "pepe@gmail.com", 225588)
print(id(profesor_pepe))
print("El nombre es: ", profesor_pepe.nombre)
print("El email es: ", profesor_pepe.email)
print("El legajo es: ", profesor_pepe.legajo_empleado)
print("Su asistencia es: ", profesor_pepe.asistencia)
profesor_pepe.asistencia_clase()
print("El profesor fue a clase, su asistencia es: ", profesor_pepe.asistencia)
