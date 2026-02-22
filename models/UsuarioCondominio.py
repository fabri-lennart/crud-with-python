# models/UsuarioCondominio.py
# Tabla pivot: un usuario puede vivir en varios condominios.
# Ej: tiene apartamento en dos residenciales distintos.
from peewee import DateField, BooleanField, ForeignKeyField, CompositeKey
from datetime import date
from models.base import BaseModel
from models.Usuario import Usuario
from models.Condominio import Condominio


class UsuarioCondominio(BaseModel):
    usuario       = ForeignKeyField(Usuario,    backref='condominios', column_name='usuario_id')
    condominio    = ForeignKeyField(Condominio, backref='residentes',  column_name='condominio_id')
    fecha_ingreso = DateField(default=date.today)
    activo        = BooleanField(default=True)

    class Meta:
        table_name  = "usuario_condominio"
        primary_key = CompositeKey('usuario', 'condominio')

    def __repr__(self):
        return f"<UsuarioCondominio usuario={self.usuario_id} | condominio={self.condominio_id} | activo={self.activo}>"
