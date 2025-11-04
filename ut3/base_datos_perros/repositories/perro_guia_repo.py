from models import PerroGuia
from database import db

class PerroGuiaRepository:
    """Maneja todas las operaciones con perros guía"""
    @staticmethod
    def create_perro_guia(fecha_nac, sexo, raza, nivel_entrenamiento, institucion):
        return PerroGuia.create(
            fecha_nac = fecha_nac,
            sexo = sexo,
            raza = raza,
            nivel_entrenamiento = nivel_entrenamiento,
            institucion = institucion
        )
    
    @staticmethod
    def ingesta_multiple(lista_tuplas):
        with db.atomic():
            PerroGuia.insert_many(lista_tuplas, fields=[
                PerroGuia.fecha_nac,
                PerroGuia.sexo,
                PerroGuia.raza,
                PerroGuia.nivel_entrenamiento,
                PerroGuia.institucion
            ]).execute()

    @staticmethod
    def consulta_todos():
        return PerroGuia.select()