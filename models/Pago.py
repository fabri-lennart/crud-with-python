# models/Pago.py
# Ocurre cuando la app cobra la tarjeta vinculada.
# Una Compra tiene UN solo Pago. Si falla → estado='rechazado',
# la Compra sigue 'pendiente' y el usuario puede reintentar.
from peewee import AutoField, CharField, DecimalField, DateTimeField, ForeignKeyField
from datetime import datetime
from models.base import BaseModel
from models.Compra import Compra
from models.Tarjeta import Tarjeta


class Pago(BaseModel):
    id         = AutoField()
    compra     = ForeignKeyField(Compra,  backref='pago',  column_name='compra_id')
    tarjeta    = ForeignKeyField(Tarjeta, backref='pagos', column_name='tarjeta_id')
    monto      = DecimalField(max_digits=10, decimal_places=2)
    estado     = CharField(max_length=20, default='procesando')  # procesando | aprobado | rechazado
    referencia = CharField(max_length=100, null=True)  # código del procesador de pago (Stripe, PayU...)
    fecha_pago = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "pagos"

    def __repr__(self):
        return f"<Pago id={self.id} | compra={self.compra_id} | ${self.monto} | {self.estado}>"
