# repositories/usuario_repository.py
from loguru import logger
from models.Usuario import Usuario


class UsuarioRepository:
    """
    Solo habla con la DB. Sin reglas de negocio.
    Pregunta, guarda, actualiza, elimina — nada más.
    """

    def crear(self, nombre: str, apellido: str, email: str,
              cedula: str, edad: int, telefono: str = None) -> Usuario:
        usuario = Usuario.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            cedula=cedula,
            edad=edad,
            telefono=telefono,
        )
        logger.info(f"Usuario creado en DB: id={usuario.id}")
        return usuario

    def obtener_por_id(self, usuario_id: int) -> Usuario | None:
        try:
            return Usuario.get_by_id(usuario_id)
        except Usuario.DoesNotExist:
            logger.warning(f"Usuario id={usuario_id} no existe.")
            return None

    def obtener_por_email(self, email: str) -> Usuario | None:
        try:
            return Usuario.get(Usuario.email == email)
        except Usuario.DoesNotExist:
            return None

    def obtener_por_cedula(self, cedula: str) -> Usuario | None:
        try:
            return Usuario.get(Usuario.cedula == cedula)
        except Usuario.DoesNotExist:
            return None

    def listar_todos(self) -> list[Usuario]:
        return list(Usuario.select().where(Usuario.activo == True))

    def actualizar(self, usuario_id: int, **campos) -> Usuario | None:
        usuario = self.obtener_por_id(usuario_id)
        if not usuario:
            return None
        for campo, valor in campos.items():
            setattr(usuario, campo, valor)
        usuario.save()
        logger.info(f"Usuario id={usuario_id} actualizado: {campos}")
        return usuario

    def eliminar(self, usuario_id: int) -> bool:
        """Soft delete — no borra de la DB, solo marca activo=False."""
        usuario = self.obtener_por_id(usuario_id)
        if not usuario:
            return False
        usuario.activo = False
        usuario.save()
        logger.info(f"Usuario id={usuario_id} desactivado (soft delete).")
        return True
