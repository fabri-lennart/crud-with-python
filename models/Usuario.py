# models/Usuario.py
from peewee import AutoField, CharField, IntegerField, BooleanField, DateField
from datetime import date
from models.base import BaseModel


class Usuario(BaseModel):
    id             = AutoField()
    nombre         = CharField(max_length=50)
    apellido       = CharField(max_length=50)
    email          = CharField(max_length=100, unique=True)
    telefono       = CharField(max_length=20,  null=True)
    cedula         = CharField(max_length=20,  unique=True)
    edad           = IntegerField()
    fecha_registro = DateField(default=date.today)
    activo         = BooleanField(default=True)

    class Meta:
        table_name = "usuarios"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __repr__(self):
        return f"<Usuario id={self.id} | {self.nombre_completo()} | {self.email}>"
