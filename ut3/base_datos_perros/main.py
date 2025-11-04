from database import db, logger
from models import PerroGuia
from repositories.perro_guia_repo import PerroGuiaRepository


def mostrar_perros(limit=10):
    logger.info(f'Listando hasta {limit} perros')
    for p in PerroGuia.select().limit(limit):
        logger.info(f'Perro: chip={p.chip}, raza={p.raza}, institucion={p.institucion}, nivel={p.nivel_entrenamiento}')


def main():
    # Asegurar tabla
    db.create_tables([PerroGuia], safe=True)
    logger.info('Tabla PerroGuia asegurada (create_tables).')

    # Mostrar algunos
    mostrar_perros(5)

    # Actualizar el primer registro si existe
    primero = PerroGuia.select().first() # esto vale None si no hay perros
    if primero:
        logger.info(f'Actualizando nivel_entrenamiento del primer perro (chip={primero.chip}) a 5')
        primero.nivel_entrenamiento = 5
        primero.save()
        logger.info(f'Actualización completa para chip={primero.chip}')

    # Consulta filtrada
    count_once = PerroGuia.select().where(PerroGuia.institucion == 'ONCE').count()
    logger.info(f'Perros con institucion=ONCE: {count_once}')

    # Borrar un registro de prueba (si existe chip=1)
    eliminado = PerroGuia.delete().where(PerroGuia.chip == 1).execute()
    logger.info(f'Registros eliminados con chip=1: {eliminado}')

    # Conteo final
    total = PerroGuia.select().count()
    logger.info(f'Total de registros tras operaciones: {total}')


if __name__ == '__main__':
    main()