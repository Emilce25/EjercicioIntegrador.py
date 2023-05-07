import numpy as np
from claseAlumno import Alumno
class ManejadorAlumnos:
    __alumnos=""
    def __init__(self):
        self.alumnos = np.array([], dtype=Alumno)

    def cargar_datos(self, archivo):
        datos = np.genfromtxt(archivo, delimiter=',', dtype=str)
        for d in datos:
            dni, apellido, nombre, carrera, anio_carrera = d
            alumno = Alumno(dni, apellido, nombre, carrera, int(anio_carrera))
            self.alumnos = np.append(self.alumnos, alumno)
    def buscar_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None
    
    def listado_alumnos(self):
        alumnos_ordenados = sorted(self.alumnos)
        for alumno in alumnos_ordenados:
            print(f'{alumno.apellido}, {alumno.nombre} ({alumno.año}° año)')