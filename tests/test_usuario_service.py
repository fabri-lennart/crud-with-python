# tests/test_usuario_service.py
import pytest
from unittest.mock import MagicMock, patch
from services.usuario_service import UsuarioService
from models.Usuario import Usuario


# ── Fixture: service con repository mockeado ──────────────────────
# Un mock reemplaza el repository real para no tocar la DB
@pytest.fixture
def service():
    with patch("services.usuario_service.UsuarioRepository") as MockRepo:
        mock_repo = MockRepo.return_value
        svc = UsuarioService()
        svc.repo = mock_repo
        yield svc, mock_repo


# ── CREATE ────────────────────────────────────────────────────────
def test_registrar_usuario_valido(service):
    svc, mock_repo = service

    # Simulamos que email y cédula NO existen en la DB
    mock_repo.obtener_por_email.return_value = None
    mock_repo.obtener_por_cedula.return_value = None

    # Simulamos el objeto que retorna el repository al crear
    usuario_mock = MagicMock()
    usuario_mock.id = 1
    mock_repo.crear.return_value = usuario_mock

    result = svc.registrar(
        nombre="Juan", apellido="Pérez",
        email="juan@email.com", cedula="001-0000001-1",
        edad=30
    )

    assert result.id == 1
    mock_repo.crear.assert_called_once()  # verificamos que SÍ llamó a crear


def test_registrar_rechaza_email_duplicado(service):
    svc, mock_repo = service

    # Simulamos que el email YA existe
    mock_repo.obtener_por_email.return_value = MagicMock()

    with pytest.raises(ValueError, match="email"):
        svc.registrar(
            nombre="Juan", apellido="Pérez",
            email="juan@email.com", cedula="001-0000001-1",
            edad=30
        )

    mock_repo.crear.assert_not_called()  # no debe haber llegado a crear


def test_registrar_rechaza_cedula_duplicada(service):
    svc, mock_repo = service

    mock_repo.obtener_por_email.return_value = None
    mock_repo.obtener_por_cedula.return_value = MagicMock()  # cédula existe

    with pytest.raises(ValueError, match="cédula"):
        svc.registrar(
            nombre="Juan", apellido="Pérez",
            email="nuevo@email.com", cedula="001-0000001-1",
            edad=30
        )

    mock_repo.crear.assert_not_called()


def test_registrar_rechaza_menor_de_edad(service):
    svc, mock_repo = service

    mock_repo.obtener_por_email.return_value = None
    mock_repo.obtener_por_cedula.return_value = None

    with pytest.raises(ValueError, match="18"):
        svc.registrar(
            nombre="Juan", apellido="Pérez",
            email="juan@email.com", cedula="001-0000001-1",
            edad=16  # menor de 18
        )

    mock_repo.crear.assert_not_called()


# ── READ ──────────────────────────────────────────────────────────
def test_buscar_por_id_existente(service):
    svc, mock_repo = service

    usuario_mock = MagicMock()
    usuario_mock.id = 5
    mock_repo.obtener_por_id.return_value = usuario_mock

    result = svc.buscar_por_id(5)
    assert result.id == 5


def test_buscar_por_id_no_existente(service):
    svc, mock_repo = service

    mock_repo.obtener_por_id.return_value = None  # no existe

    with pytest.raises(ValueError, match="id=99"):
        svc.buscar_por_id(99)


# ── UPDATE ────────────────────────────────────────────────────────
def test_actualizar_email_ya_en_uso(service):
    svc, mock_repo = service

    # El email nuevo ya lo usa OTRO usuario (id=2)
    otro_usuario = MagicMock()
    otro_usuario.id = 2
    mock_repo.obtener_por_email.return_value = otro_usuario

    with pytest.raises(ValueError, match="en uso"):
        svc.actualizar(usuario_id=1, email="ocupado@email.com")


def test_actualizar_campos_validos(service):
    svc, mock_repo = service

    mock_repo.obtener_por_email.return_value = None  # email libre

    usuario_mock = MagicMock()
    usuario_mock.telefono = "809-000-0000"
    mock_repo.actualizar.return_value = usuario_mock

    result = svc.actualizar(usuario_id=1, telefono="809-000-0000")
    assert result.telefono == "809-000-0000"


# ── DELETE ────────────────────────────────────────────────────────
def test_eliminar_usuario_existente(service):
    svc, mock_repo = service

    mock_repo.eliminar.return_value = True

    result = svc.eliminar(1)
    assert result is True


def test_eliminar_usuario_no_existente(service):
    svc, mock_repo = service

    mock_repo.eliminar.return_value = False  # no encontró el usuario

    with pytest.raises(ValueError, match="id=99"):
        svc.eliminar(99)
