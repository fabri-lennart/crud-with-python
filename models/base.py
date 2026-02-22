# models/base.py
from peewee import Model
from database_connection.database import DatabaseConnection

db = DatabaseConnection.get_instance().db

class BaseModel(Model):
    class Meta:
        database = db
