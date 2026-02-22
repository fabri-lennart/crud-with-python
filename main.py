# main.py
from database_connection.database    import DatabaseConnection
from database_connection.initializer import DatabaseInitializer

from models.Usuario           import Usuario
from models.Condominio        import Condominio
from models.Producto          import Producto
from models.UsuarioCondominio import UsuarioCondominio
from models.Tarjeta           import Tarjeta
from models.Compra            import Compra
from models.DetalleCompra     import DetalleCompra
from models.Pago              import Pago

from services.usuario_service import UsuarioService

ALL_MODELS = [
    Usuario, Condominio, Producto,
    UsuarioCondominio, Tarjeta,
    Compra, DetalleCompra, Pago,
]

# ── Conexión y tablas ─────────────────────────────────────────────
conn = DatabaseConnection.get_instance()
conn.connect()
initializer = DatabaseInitializer(conn.get_db())
initializer.create_tables(ALL_MODELS)

# ── Probar CRUD de Usuario ────────────────────────────────────────
service = UsuarioService()

# CREATE
print("\n── CREATE ──────────────────────────")
juan = service.registrar(
    nombre="Juan", apellido="Pérez",
    email="juan@email.com", cedula="001-0000001-1",
    edad=30, telefono="809-555-0101"
)
print(juan)

# READ
print("\n── READ ────────────────────────────")
encontrado = service.buscar_por_id(juan.id)
print(encontrado)

todos = service.listar()
print(f"Total usuarios activos: {len(todos)}")

# UPDATE
print("\n── UPDATE ──────────────────────────")
actualizado = service.actualizar(juan.id, telefono="809-999-0000")
print(f"Teléfono nuevo: {actualizado.telefono}")

# DELETE (soft)
print("\n── DELETE ──────────────────────────")
service.eliminar(juan.id)
print(f"Usuarios activos tras delete: {len(service.listar())}")

if __name__ == "__main__":
    print(conn)
