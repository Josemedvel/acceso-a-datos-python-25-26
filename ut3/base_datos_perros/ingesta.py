from database import db, logger
from peewee import *
from models import PerroGuia
from repositories.perro_guia_repo import PerroGuiaRepository 

perros = [
    ('2021-04-14', 'H', 'Labrador', 5, 'ONCE'),
('2020-09-09', 'M', 'Golden Retriever', 1, 'ONCE'),
('2019-06-28', 'M', 'Pastor Alemán', 1, 'PerrosGuía España'),
('2018-02-15', 'H', 'Labrador', 5, 'ONCE'),
('2021-11-30', 'M', 'Golden Retriever', 1, 'CNV Perros Guía'),
('2020-07-12', 'M', 'Pastor Alemán', 1, 'ONCE'),
('2019-05-21', 'H', 'Labrador', 2, 'PerrosGuía España'),
('2018-10-10', 'M', 'Golden Retriever', 5, 'ONCE'),
('2022-01-27', 'H', 'Labrador', 1, 'CNV Perros Guía'),
('2020-03-03', 'M', 'Pastor Alemán', 5, 'ONCE'),
('2019-12-04', 'H', 'Golden Retriever', 2, 'PerrosGuía España'),
('2017-08-16', 'M', 'Labrador', 5, 'ONCE'),
('2021-06-29', 'H', 'Golden Retriever', 1, 'CNV Perros Guía'),
('2020-12-01', 'M', 'Pastor Alemán', 3, 'ONCE'),
('2018-07-19', 'H', 'Labrador', 5, 'PerrosGuía España'),
('2019-03-11', 'M', 'Golden Retriever', 5, 'ONCE'),
('2022-02-02', 'M', 'Labrador', 1, 'ONCE'),
('2018-09-23', 'H', 'Pastor Alemán', 3, 'CNV Perros Guía'),
('2021-05-14', 'M', 'Golden Retriever', 5, 'ONCE'),
('2019-10-05', 'H', 'Labrador', 4, 'PerrosGuía España'),
('2017-11-17', 'M', 'Golden Retriever', 5, 'ONCE'),
('2020-01-26', 'H', 'Pastor Alemán', 4, 'ONCE'),
('2022-03-15', 'M', 'Labrador', 1, 'CNV Perros Guía'),
('2018-06-09', 'H', 'Golden Retriever', 1, 'ONCE'),
('2019-09-27', 'M', 'Labrador', 5, 'PerrosGuía España'),
('2020-05-07', 'M', 'Pastor Alemán', 4, 'ONCE'),
('2021-07-31', 'H', 'Golden Retriever', 1, 'ONCE'),
('2017-12-20', 'M', 'Labrador', 5, 'CNV Perros Guía'),
('2018-11-08', 'H', 'Pastor Alemán', 4, 'PerrosGuía España'),
('2021-02-13', 'M', 'Labrador', 5, 'ONCE')
]

db.drop_tables([PerroGuia], safe=True)
db.create_tables([PerroGuia], safe=True)
logger.info(f'Tablas tiradas y recreadas. Iniciando inserción múltiple de {len(perros)} filas')
PerroGuiaRepository.ingesta_multiple(perros)
logger.info(f'Inserción múltiple completa, el número de registros es de : {PerroGuia.select().count()}')
