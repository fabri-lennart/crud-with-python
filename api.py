from fastapi import FastAPI
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

from routers import usuarios

ALL_MODELS = [
    Usuario, Condominio, Producto,
    UsuarioCondominio, Tarjeta,
    Compra, DetalleCompra, Pago,
]

# ── Inicializar BD ────────────────────────────────────────────────
conn = DatabaseConnection.get_instance()
conn.connect()
DatabaseInitializer(conn.get_db()).create_tables(ALL_MODELS)

# ── App FastAPI ───────────────────────────────────────────────────
app = FastAPI(title="Condominio API", version="1.0.0")

# ── Registrar routers ─────────────────────────────────────────────
app.include_router(usuarios.router)


@app.get("/")
def root():
    return {"message": "API funcionando ✅"}
