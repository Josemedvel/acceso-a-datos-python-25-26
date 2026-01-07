from conexion_pool import r
import time
import json
from pprint import pp

def simular_consulta(user_id):
    print("Preguntando a la base de datos")
    time.sleep(2)
    return {
        "id": user_id,
        "nombre": "Paco",
        "telefono": 683456738,
        "email": "pacogomez@gmail.com",
        "edad" : 20
    }

def cumplir_anno(user_id):
    key = f"user:{user_id}"
    cached = r.get(key)
    if cached is None:
        print("No está en caché!")
        usuario = simular_consulta(user_id)
        usuario["edad"] = usuario.get("edad", 0) + 1
        r.setex(key, 60, json.dumps(usuario))
        return usuario
    else:
        #está en caché
        usuario = json.loads(cached)
        usuario["edad"] = usuario.get("edad", 0) + 1
        ttl = r.ttl(key)
        if ttl and ttl > 0:
            r.setex(key, ttl, json.dumps(usuario))
        else:
            # no tiene expiración o no existe (escribimos sin ttl)
            r.set(key, json.dumps(usuario))
        return usuario



def main():
    user_id = 19
    key = f"user:{user_id}"

    cached = r.get(key)
    if cached is None:
        print("La caché no lo tiene!")
        resultado = simular_consulta(user_id)
        # Guardar como JSON con expiración de 60 segundos
        r.setex(key, 60, json.dumps(resultado))
    else:
        print("Obtenido de caché")
        resultado = json.loads(cached)
    pp(cumplir_anno(user_id))
    pp(resultado)

if __name__ == "__main__":
    main()