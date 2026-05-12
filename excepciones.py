# =========================
# excepciones.py
# =========================

class ErrorSistema(Exception):
    """Excepción base del sistema."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Error en datos del cliente."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error cuando el servicio no puede prestarse."""
    pass


class ReservaError(ErrorSistema):
    """Error en procesos de reserva."""
    pass
