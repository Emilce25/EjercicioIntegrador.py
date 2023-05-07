from claseMateriaAprobada import MateriaAprobada
import csv
import numpy as np
from claseManejadorAlumno import ManejadorAlumnos

class ManejadorMaterias:
    __materias_aprobadas=""

    def __init__(self):
        self.materias_aprobadas = []

    def cargar_datos(self, archivo):
        datos = np.genfromtxt(archivo, delimiter=',', dtype=str)
        for d in datos:
            dni, nombre_materia, fecha, nota, aprobacion = d
            materia_aprobada = MateriaAprobada(dni, nombre_materia, fecha, nota, aprobacion)
            self.materias_aprobadas.append(materia_aprobada)
    def buscar_materia_promocionada(self, nombre_materia):
        for alumno in manejador_alumnos.alumnos:
            for materia in alumno.materias_aprobadas:
                if materia.nombre == nombre_materia and materia.aprobacion == 'P' and materia.nota >= 7:
                    print(f'{alumno.dni:<10}{alumno.apellido}, {alumno.nombre:<25}{materia.fecha:<20}{materia.nota:<10}{alumno.año:<10}')