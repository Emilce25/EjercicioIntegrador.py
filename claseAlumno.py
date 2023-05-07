import numpy as np


class Alumno:
    __dni=""
    __apellido=""
    __nombre=""
    __carrera=""
    __anio_carrera=""

    def __init__(self, dni, apellido, nombre, carrera, anio_carrera):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio_carrera = anio_carrera
    
    def agregar_materia_aprobada(self, materia):
        self.materias_aprobadas.append(materia)
    
    def promedio_con_aplazos(self):
        notas = [materia.nota for materia in self.materias_aprobadas]
        promedio = np.mean(notas)
        return promedio
    
    def promedio_sin_aplazos(self):
        notas = [materia.nota for materia in self.materias_aprobadas if materia.nota >= 4]
        if len(notas) == 0:
            return 0
        else:
            promedio = np.mean(notas)
            return promedio
    
    def __lt__(self, other):
        if self.año == other.año:
            return self.apellido.lower() + self.nombre.lower() < other.apellido.lower() + other.nombre.lower()
        else:
            return self.año < other.año
