# services/usuario_service.py
from loguru import logger
from models.Usuario import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    """
    Aplica las reglas de negocio.
    No sabe nada de SQL — usa el repository para eso.
    """

    def __init__(self):
        self.repo = UsuarioRepository()

    # ── CREATE ────────────────────────────────────────────────────
    def registrar(self, nombre: str, apellido: str, email: str,
                  cedula: str, edad: int, telefono: str = None) -> Usuario:

        # Regla 1: email único
        if self.repo.obtener_por_email(email):
            raise ValueError(f"El email '{email}' ya está registrado.")

        # Regla 2: cédula única
        if self.repo.obtener_por_cedula(cedula):
            raise ValueError(f"La cédula '{cedula}' ya está registrada.")

        # Regla 3: edad mínima
        if edad < 18:
            raise ValueError("El usuario debe ser mayor de 18 años.")

        return self.repo.crear(nombre, apellido, email, cedula, edad, telefono)

    # ── READ ──────────────────────────────────────────────────────
    def buscar_por_id(self, usuario_id: int) -> Usuario:
        usuario = self.repo.obtener_por_id(usuario_id)
        if not usuario:
            raise ValueError(f"No existe un usuario con id={usuario_id}.")
        return usuario

    def listar(self) -> list[Usuario]:
        usuarios = self.repo.listar_todos()
        logger.info(f"{len(usuarios)} usuarios activos encontrados.")
        return usuarios

    # ── UPDATE ────────────────────────────────────────────────────
    def actualizar(self, usuario_id: int, **campos) -> Usuario:
        # Si quieren cambiar el email, verificar que no lo use otro
        if "email" in campos:
            existente = self.repo.obtener_por_email(campos["email"])
            if existente and existente.id != usuario_id:
                raise ValueError(f"El email '{campos['email']}' ya está en uso.")

        usuario = self.repo.actualizar(usuario_id, **campos)
        if not usuario:
            raise ValueError(f"No existe un usuario con id={usuario_id}.")
        return usuario

    # ── DELETE ────────────────────────────────────────────────────
    def eliminar(self, usuario_id: int) -> bool:
        if not self.repo.eliminar(usuario_id):
            raise ValueError(f"No existe un usuario con id={usuario_id}.")
        logger.info(f"Usuario id={usuario_id} eliminado correctamente.")
        return True
