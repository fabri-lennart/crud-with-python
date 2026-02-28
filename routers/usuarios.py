# routers/usuarios.py
from fastapi import APIRouter, HTTPException, status
from schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut
from services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
service = UsuarioService()


@router.post("/", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
def crear_usuario(data: UsuarioCreate):
    try:
        usuario = service.registrar(**data.model_dump())
        return usuario
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[UsuarioOut])
def listar_usuarios():
    return service.listar()


@router.get("/{usuario_id}", response_model=UsuarioOut)
def obtener_usuario(usuario_id: int):
    usuario = service.buscar_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioOut)
def actualizar_usuario(usuario_id: int, data: UsuarioUpdate):
    try:
        # solo pasa los campos que fueron enviados (no None)
        campos = {k: v for k, v in data.model_dump().items() if v is not None}
        return service.actualizar(usuario_id, **campos)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: int):
    try:
        service.eliminar(usuario_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
