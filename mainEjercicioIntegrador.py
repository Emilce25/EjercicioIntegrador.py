import numpy as np
import csv
from claseManejadorAlumno import ManejadorAlumnos
from claseManejadorMaterias import ManejadorMaterias
 
if __name__ == '__main__':
 manejador_alumnos = ManejadorAlumnos()
 manejador_alumnos.cargar_datos('alumnos.csv')
 manejador_materias = ManejadorMaterias()
 manejador_materias.cargar_datos('materiasAprobadas.csv')