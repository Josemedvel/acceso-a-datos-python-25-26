import libsql
import envyte



url = envyte.get("DB_HOST")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("aadut1", sync_url = url, auth_token = auth_token)
conn.sync()


cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
print(cursor.execute("select * from users").fetchall())

conn.close()