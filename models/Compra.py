# models/Compra.py
# Se crea cuando el usuario confirma su carrito.
# El estado empieza en 'pendiente' hasta que el Pago sea aprobado.
from peewee import AutoField, CharField, DateTimeField, DecimalField, TextField, ForeignKeyField
from datetime import datetime
from models.base import BaseModel
from models.Usuario import Usuario
from models.Condominio import Condominio


class Compra(BaseModel):
    id           = AutoField()
    usuario      = ForeignKeyField(Usuario,    backref='compras', column_name='usuario_id')
    condominio   = ForeignKeyField(Condominio, backref='compras', column_name='condominio_id')
    fecha_compra = DateTimeField(default=datetime.now)
    total        = DecimalField(max_digits=10, decimal_places=2)
    estado       = CharField(max_length=20, default='pendiente')  # pendiente | pagada | cancelada
    notas        = TextField(null=True)

    class Meta:
        table_name = "compras"

    def __repr__(self):
        return f"<Compra id={self.id} | usuario={self.usuario_id} | total=${self.total} | {self.estado}>"
