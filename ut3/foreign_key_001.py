from datetime import date
from peewee import *
from base_datos_perros.database import db, logger


class Owner(Model):
	id = AutoField()
	nombre = CharField()

	class Meta:
		database = db
		table_name = 'owner'


class Pet(Model):
	id = AutoField()
	nombre = CharField()
	especie = CharField()
	owner = ForeignKeyField(Owner, backref='pets', on_delete='CASCADE')

	class Meta:
		database = db
		table_name = 'pet'


def run():
	# Habilitar foreign_keys para SQLite por sesión
	db.connect()
	db.execute_sql('PRAGMA foreign_keys = ON;')

	# Crear tablas
	db.drop_tables([Pet, Owner], safe=True)
	db.create_tables([Owner, Pet], safe=True)
	logger.info('Tablas Owner y Pet creadas (FK habilitadas)')

	# Inserción válida: crear owner y mascota
	o = Owner.create(nombre='Carlos')
	p = Pet.create(nombre='Firulais', especie='Perro', owner=o)
	logger.info(f'Insertado Owner id={o.id}, Pet id={p.id} con owner={p.owner.id}')

	# Consulta: acceder a las mascotas de un owner y al owner desde la mascota
	familias = list(Owner.select())
	for fam in familias:
		logger.info(f'Owner {fam.id} {fam.nombre} tiene mascotas: {[pet.nombre for pet in fam.pets]}')

	# Incumplimiento de FK: intentar crear una mascota con owner_id que no existe
	try:
		Pet.create(nombre='SinDueño', especie='Gato', owner=9999)
	except Exception as e:
		logger.exception(f'Incumplimiento de FK (esperado) al crear Pet con owner inexistente: {e}')

	# Borrar owner y comprobar cascade
	owner_id = o.id
	o.delete_instance() # para borrar el registro directamente, sin delete
	remaining = Pet.select().where(Pet.owner == owner_id).count()
	logger.info(f'Mascotas restantes del owner {owner_id} tras borrado (debería ser 0): {remaining}')
	db.close()


if __name__ == '__main__':
	run()

