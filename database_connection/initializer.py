# database_connection/initializer.py
from loguru import logger
from peewee import MySQLDatabase


class DatabaseInitializer:
    """
    Responsabilidad única: crear y verificar tablas.
    No sabe cómo se creó la conexión, solo recibe la db.
    """

    def __init__(self, db: MySQLDatabase):
        self.db = db

    def create_tables(self, models: list, safe: bool = True):
        self.db.create_tables(models, safe=safe)
        for model in models:
            logger.info(f"Tabla asegurada: '{model._meta.table_name}'")

    def verify_tables(self, models: list) -> dict:
        existing = set(self.db.get_tables())
        results = {}
        for model in models:
            table = model._meta.table_name
            exists = table in existing
            status = "✅ existe" if exists else "❌ no existe"
            logger.info(f"  {table}: {status}")
            results[table] = exists
        return results
