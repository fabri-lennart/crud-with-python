# schemas/usuario.py
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre:   str
    apellido: str
    email:    EmailStr
    cedula:   str
    edad:     int
    telefono: Optional[str] = None


class UsuarioUpdate(BaseModel):
    nombre:   Optional[str]   = None
    apellido: Optional[str]   = None
    email:    Optional[EmailStr] = None
    telefono: Optional[str]   = None
    edad:     Optional[int]   = None


class UsuarioOut(BaseModel):
    id:              int
    nombre:          str
    apellido:        str
    email:           str
    cedula:          str
    edad:            int
    telefono:        Optional[str]
    fecha_registro:  date
    activo:          bool

    model_config = {"from_attributes": True}  # permite leer desde objetos Peewee
