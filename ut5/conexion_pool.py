import redis
from redis.connection import ConnectionPool
import envyte

HOST = envyte.get("HOST")
PORT = envyte.get("PORT")
PASSWORD = envyte.get("PASSWORD")
DECODE_RESPONSES = True

pool = ConnectionPool(
    host = HOST,
    port = PORT,
    password = PASSWORD,
    db = 0,
    decode_responses = DECODE_RESPONSES
    )
r = redis.Redis(connection_pool=pool)