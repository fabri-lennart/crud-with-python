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

# 1. Conexión
conn = DatabaseConnection.get_instance()
conn.connect()

# 2. Crear tablas — el orden importa por las FK
initializer = DatabaseInitializer(conn.get_db())
initializer.create_tables([
    Usuario,            # sin dependencias
    Condominio,         # sin dependencias
    Producto,           # sin dependencias
    UsuarioCondominio,  # depende de: Usuario, Condominio
    Tarjeta,            # depende de: Usuario
    Compra,             # depende de: Usuario, Condominio
    DetalleCompra,      # depende de: Compra, Producto
    Pago,               # depende de: Compra, Tarjeta
])

# 3. Verificar que existen
initializer.verify_tables([
    Usuario,
    Condominio,
    Producto,
    UsuarioCondominio,
    Tarjeta,
    Compra,
    DetalleCompra,
    Pago,
])

if __name__ == "__main__":
    print(conn)
