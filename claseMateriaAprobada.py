from datetime import datetime
class MateriaAprobada:
    __dni=""
    __nombre_materia=""
    __fecha=""
    __nota=""
    __aprobacion=""

    def __init__(self, dni, nombre_materia, fecha, nota, aprobacion):
        self.dni = dni
        self.nombre_materia = nombre_materia
        self.fecha = datetime.strptime(fecha, '%d/%m/%Y')
        self.nota = float(nota)
        self.aprobacion = aprobacion