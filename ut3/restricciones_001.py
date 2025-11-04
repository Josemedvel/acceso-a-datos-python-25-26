from datetime import date
from peewee import *

# Importar la base de datos y logger desde el paquete base_datos_perros
from base_datos_perros.database import db, logger

class Persona(Model):
    id = AutoField()
    nombre = CharField(null=False)
    edad = IntegerField(constraints=[Check('edad >= 0')])
    email = CharField(unique=True)
    fecha_nac = DateField()
    salario = DecimalField(max_digits=10, decimal_places=2, constraints=[Check('salario >= 0')])
    activo = BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.fecha_nac >= date.today():
            raise ValueError("fecha_nac debe ser anterior a hoy")
        else:
            return super().save(*args, **kwargs)
    
    class Meta:
        database = db
        table_name = 'persona'


def run():
    # borrar tabla
    db.drop_tables([Persona], safe=True)
    # Asegurar tabla
    db.create_tables([Persona], safe=True)
    logger.info('Tabla Persona asegurada para pruebas de restricciones')

    # Inserción válida con save()
    try:
        p1 = Persona(nombre='Ana', edad=30, email='ana@example.com', fecha_nac=date(1995, 1, 1), salario=2500.50)
        p1.save()
        logger.info(f'Inserción con save() correcta: id={p1.id}')
    except Exception as e:
        logger.exception(f'Error al insertar p1 con save(): {e}')

    # Inserción válida con create()
    try:
        p2 = Persona.create(nombre='Luis', edad=40, email='luis@example.com', fecha_nac=date(1985, 6, 6), salario=3000)
        logger.info(f'Inserción con create() correcta: id={p2.id}')
    except Exception as e:
        logger.exception(f'Error al insertar p2 con create(): {e}')

    # Inserción inválida con save: edad negativa
    try:
        p3 = Persona(nombre='ErrorEdad', edad=-5, email='err_edad@example.com', fecha_nac=date(2030, 1, 1), salario=100)
        p3.save()
    except Exception as e:
        logger.exception(f'Incumplimiento de restricción edad negativa (esperado): {e}')

    # Inserción inválida con create: salario negativo
    try:
        p4 = Persona.create(nombre='ErrorSalario', edad=25, email='err_sal@example.com', fecha_nac=date(2000, 1, 1), salario=-10)
    except Exception as e:
        logger.exception(f'Incumplimiento de restricción salario negativo (esperado): {e}')

    # Inserción inválida: email duplicado (debería lanzar IntegrityError)
    try:
        p5 = Persona.create(nombre='DupEmail', edad=22, email='ana@example.com', fecha_nac=date(2001, 2, 2), salario=1000)
    except Exception as e:
        logger.exception(f'Incumplimiento de restricción email único (esperado): {e}')

    # Inserción inválida con save: nombre NULL/None
    try:
        p6 = Persona(nombre=None, edad=20, email='sin_nombre@example.com', fecha_nac=date(2003, 3, 3), salario=500)
        p6.save()
    except Exception as e:
        logger.exception(f'Incumplimiento de restricción nombre NOT NULL (esperado): {e}')

    # Inserción inválida con create: fecha posterior a hoy
    try:
        p7 = Persona.create(nombre="Eugenia", edad=89, email="abuela_genia@gmail.com", fecha_nac=date(2026,7,10), salario=10)
    except Exception as e:
        logger.exception(f'Incumplimiento de restricción fecha_nac posterior al día actual')
    
    # Mostrar estado final
    total = Persona.select().count()
    logger.info(f'Total de personas tras pruebas: {total}')


if __name__ == '__main__':
    run()