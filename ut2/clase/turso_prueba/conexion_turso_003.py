import envyte
import libsql

db_url = envyte.get("DB_URL")
api_token = envyte.get("API_TOKEN")

conn = libsql.connect("pruebaaad", sync_url=db_url, auth_token=api_token)
conn.sync()