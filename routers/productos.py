from fastapi import APIRouter, HTTPException
from services.producto_service import ProductoService
from schemas.producto import ProductoOut

router = APIRouter(prefix="/productos", tags=["Productos"])
service = ProductoService()

@router.get("/{producto_id}", response_model=ProductoOut)
def obtener_producto(producto_id: int):
    producto = service.buscar(producto_id)       # ← objeto Peewee
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto     
