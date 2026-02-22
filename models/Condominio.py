# libraries
from peewee import Model, AutoField, CharField, IntegerField, BooleanField, DateField
from datetime import date
from models.base import BaseModel


class Condominio(BaseModel):
    id             = AutoField()
    nombre         = CharField(max_length=50)
    direccion      = CharField(max_length=50)
    ciudad         = CharField(max_length=50)
    provincia      = CharField(max_length=100, unique=True)
    codigo_postal  = IntegerField()
    torre          = CharField(max_length=50)
    apartamento    = CharField(max_length=50)

    class Meta:
        table_name = "condominios"

    def nombre_condominio_completo(self):
        return f"{self.nombre} {self.direccion}"

    def __repr__(self):
        return f"<Condominio id={self.id} | {self.nombre_condominio_completo()} | {self.codigo_postal}>"
