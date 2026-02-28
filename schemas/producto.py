# schemas/producto.py
from pydantic import BaseModel

class ProductoOut(BaseModel):
    id:     int
    nombre: str
    precio_unitario: float

    model_config = {"from_attributes": True}  # ← permite leer objetos Peewee
