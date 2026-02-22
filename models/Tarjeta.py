# models/Tarjeta.py
# El usuario vincula su tarjeta UNA VEZ a la app.
# Nunca guardamos el número completo — solo los últimos 4 dígitos.
# El número real lo tokeniza el procesador de pago (Stripe, PayU, etc.)
from peewee import AutoField, CharField, BooleanField, DateField, ForeignKeyField
from models.base import BaseModel
from models.Usuario import Usuario


class Tarjeta(BaseModel):
    id                = AutoField()
    usuario           = ForeignKeyField(Usuario, backref='tarjetas', column_name='usuario_id')
    tipo              = CharField(max_length=10)   # credito | debito
    ultimos_4_dig     = CharField(max_length=4)
    banco_emisor      = CharField(max_length=60)   # Banesco, BHD, Scotiabank...
    fecha_vencimiento = DateField()
    activa            = BooleanField(default=True) # False = desvinculada por el usuario

    class Meta:
        table_name = "tarjetas"

    def __repr__(self):
        return f"<Tarjeta id={self.id} | {self.tipo} | **** {self.ultimos_4_dig} | {self.banco_emisor}>"
