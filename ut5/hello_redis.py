import redis
import envyte

HOST = envyte.get("HOST")
PORT = envyte.get("PORT")
PASSWORD = envyte.get("PASSWORD")
DECODE_RESPONSES = True


r = redis.Redis(
    host = HOST,
    port = PORT,
    password = PASSWORD,
    decode_responses = DECODE_RESPONSES
    )

print(r.ping()) # nos tiene que salir True