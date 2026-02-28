# services/producto_service.py
from repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self):
        self.repo = ProductoRepository()

    def buscar(self, id: int):
        return self.repo.obtener_por_id(id)  # ← retorna lo mismo que el repository
