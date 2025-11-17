import json
from peewee import *
from models import Producto
from database import inicializar_base, db
from pprint import pprint

def main():

    #inicializar_base([Producto])
    '''portatil = Producto.create(
        nombre='Asus Gaming Pro',
        especificaciones = {
            'cpu': 'Intel Core i5 1340U',
            'ram': '16GB',
            'almacenamiento': {
              'tipo': 'NVME',
              'capacidad': '1TB'  
            }
        },
        opiniones = {
            'Jose': 'Un gran ordenador para el día a día',
            'María': 'Después de un mes de uso me ha dejado de funcionar el Enter, no lo recomiendo'
        },
        precio = 1200.99
    )
    '''
    # consulta sobre el valor de una clave
    q1 = Producto.select().where(Producto.especificaciones['rom'] == '16GB')
    for fila in q1.dicts():
        pprint(fila)
    
    # consultas para comprobar que existan claves (operador -> y ?)
    
    # anidado
    try:
        q2 = Producto.select().where(SQL("especificaciones->'almacenamiento' ? %s", ('capacidad',)))
        for fila in q2.dicts():
            pprint(fila)
    except Exception as e:
        print("No podemos usar el operador -> ni ? si el campo es JSON y no JSONB")
    
    # nivel superior
    q3 = Producto.select().where(SQL("opiniones ? %s", ('Jose',)))
    for fila in q3.dicts():
        pprint(fila)

    # consumo de datos JSONB, directo
    q4 = Producto.select(Producto.especificaciones).dicts()
    q4_dicts = list(q4)
    for dic in q4_dicts:
        print(dic["especificaciones"])

    # consumo de datos JSON, parseo a JSON
    q5 = Producto.select(Producto.opiniones)
    q5_lista = list(q5)
    for item in q5_lista:
        print(item, type(item))
        diccionario = json.loads(item)
        if 'Jose' in diccionario:
            print('La queja de Jose es:', diccionario['Jose'])

if __name__ == "__main__":
    main()