import logging
from peewee import SqliteDatabase
from pathlib import Path



logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "perros.db"

if not DB_PATH.exists():
    logger.error(f"La base de datos {DB_PATH} no existe, se creará al conectar")
else:
    logger.info(f"Conectando con la base de datos {DB_PATH}")

db = SqliteDatabase(DB_PATH)