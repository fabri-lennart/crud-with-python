# repositories/producto_repository.py
from models.Producto import Producto

class ProductoRepository:
    def obtener_por_id(self, id: int):
        return Producto.get_or_none(Producto.id == id)  # ← retorna objeto Peewee o None
