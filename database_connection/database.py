# database_connection/database.py
import configparser
from loguru import logger
from peewee import MySQLDatabase


class DatabaseConnection:
    """
    Singleton — responsabilidad única: gestionar la conexión a la DB.
    Cambiamos pymysql por peewee.MySQLDatabase para que sea compatible
    con los modelos Peewee y el DatabaseInitializer.
    """

    _instance = None

    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise RuntimeError("Usa DatabaseConnection.get_instance()")
        self._config = self._load_config()
        db_cfg = self._config["data_base"]

        # peewee.MySQLDatabase en lugar de pymysql.connect()
        self.db = MySQLDatabase(
            db_cfg["database"],
            host=db_cfg["host"],
            port=int(db_cfg["port"]),
            user=db_cfg["user"],
            password=db_cfg["password"],
            charset="utf8mb4",
        )
        DatabaseConnection._instance = self
        logger.info("DatabaseConnection creada.")

    @classmethod
    def get_instance(cls) -> "DatabaseConnection":
        if cls._instance is None:
            logger.debug("Creando instancia de DatabaseConnection")
            cls()
        return cls._instance

    @staticmethod
    def _load_config() -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read("config.ini")
        logger.debug("config.ini cargado correctamente")
        return config

    def connect(self):
        if self.db.is_closed():
            self.db.connect()
            logger.info(f"Conexión abierta → {self.db.database}")

    def disconnect(self):
        if not self.db.is_closed():
            self.db.close()
            logger.info("Conexión cerrada.")

    def get_db(self) -> MySQLDatabase:
        """Retorna el objeto db para que DatabaseInitializer lo use."""
        return self.db

    def __repr__(self):
        state = "abierta" if not self.db.is_closed() else "cerrada"
        return f"<DatabaseConnection db={self.db.database} [{state}]>"
