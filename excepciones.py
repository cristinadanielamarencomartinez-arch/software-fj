# =========================
# excepciones.py
# =========================

class ErrorSistema(Exception):
    """Excepción base del sistema."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Se genera cuando los datos del cliente son inválidos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaError(ErrorSistema):
    """Se genera cuando ocurre un error en una reserva."""
    pass
