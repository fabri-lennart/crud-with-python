# models/DetalleCompra.py
# Una fila por cada producto distinto en la compra.
# Si compra 3 Coca-Colas → cantidad=3, no tres filas.
# precio_unitario se guarda al momento de comprar por si el precio cambia después.
from peewee import AutoField, IntegerField, DecimalField, ForeignKeyField
from models.base import BaseModel
from models.Compra import Compra
from models.Producto import Producto


class DetalleCompra(BaseModel):
    id              = AutoField()
    compra          = ForeignKeyField(Compra,   backref='detalles', column_name='compra_id')
    producto        = ForeignKeyField(Producto, backref='detalles', column_name='producto_id')
    cantidad        = IntegerField()
    precio_unitario = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table_name = "detalles_compra"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __repr__(self):
        return f"<DetalleCompra id={self.id} | compra={self.compra_id} | {self.producto_id} x{self.cantidad} | subtotal=${self.subtotal}>"
