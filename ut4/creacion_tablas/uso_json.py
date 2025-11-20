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
    q1 = Producto.select().where(Producto.especificaciones['ram'] == '8GB').dicts()
    
    for fila in q1:
        pprint(fila)
    
    # consultas para comprobar que existan claves (operador -> y ?)
    
    # anidado
    try:
        q2 = Producto.select().where(SQL("especificaciones->'almacenamiento' ? %s", ('capacidad',))).dicts()
        for fila in q2:
            pprint(fila)
    except Exception as e:
        print("No podemos usar el operador -> ni ? si el campo es JSON y no JSONB")
    
    print()

    # parseo manual de JSON
    q2_alternativo = Producto.select().dicts()
    for fila in q2_alternativo:
        if "almacenamiento" in fila["especificaciones"]:
            if "capacidad" in fila["especificaciones"]["almacenamiento"]:
                pprint(fila)

    # nivel superior
    q3 = Producto.select().where(SQL("opiniones ? %s", ('Jose',))).dicts()
    for fila in q3:
        pprint(fila)

    # consumo de datos JSON usando dicts
    q4 = Producto.select(Producto.especificaciones).dicts()
    q4_dicts = list(q4)
    for dic in q4_dicts:
        print(dic["especificaciones"])

    # más consumo directo
    q5 = Producto.select(Producto.opiniones)
    q5_lista = list(q5)
    for item in q5_lista:
        print(item.opiniones, type(item.opiniones))
        if 'Jose' in item.opiniones:
            print('La opinión de Jose es:', item.opiniones['Jose'])

    # operador ?| (Se usa para saber si existe alguna de las claves)
    q_ex_or = Producto.select().where(SQL("opiniones ?| ARRAY[%s, %s]", ('Jose', 'Manuel')))
    for item in q_ex_or:
        print(f"{item.nombre}: {item.opiniones}")
    
    # operador ?& (Se usa para saber si existen todas las claves)
    q_ex_and = list(Producto.select().where(SQL("opiniones ?& ARRAY[%s, %s]", ('Jose', 'Mara'))))
    for item in q_ex_and:
            print(item)
    if len(q_ex_and) == 0:
        print("No hay registros que tengan las dos claves")
    
    
    # operador @> (Se usa para saber si un JSON contiene otro JSON)
    json_buscado = {
        "Jose": "Un gran ordenador para el día a día"
    }
    q_contains = Producto.select().where(
        SQL("opiniones @> %s", (json.dumps(json_buscado),))
    )
    for item in q_contains:
        print(item.opiniones)

    # operador <@ (Se usa para saber si un JSON ES CONTENIDO en otro, no es tan común)

    # en peewee usando el tipo de dato BinaryJSONField,
    # podemos usar el método contains
    q_contains_peewee = Producto.select().where(
        Producto.opiniones.contains(json_buscado)
    )
    for item in q_contains_peewee:
        print(f"{item.nombre}:{item.opiniones}")



if __name__ == "__main__":
    main()