# models/Producto.py
from peewee import AutoField, CharField, DecimalField, IntegerField, BooleanField, TextField
from models.base import BaseModel


class Producto(BaseModel):
    id              = AutoField()
    nombre          = CharField(max_length=100)
    descripcion     = TextField(null=True)
    precio_unitario = DecimalField(max_digits=10, decimal_places=2)
    categoria       = CharField(max_length=50, null=True)  # bebidas, alimentos, limpieza...
    stock           = IntegerField(default=0)
    activo          = BooleanField(default=True)

    class Meta:
        table_name = "productos"

    def __repr__(self):
        return f"<Producto id={self.id} | {self.nombre} | ${self.precio_unitario} | stock={self.stock}>"
