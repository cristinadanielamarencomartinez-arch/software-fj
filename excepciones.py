# =========================
# excepciones.py
# Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Software FJ
# =========================

class ErrorSistema(Exception):
    """
    Clase base para todas las excepciones personalizadas del sistema.
    Permite centralizar el manejo de errores generales.
    """
    def __init__(self, mensaje="Ha ocurrido un error general en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ClienteInvalidoError(ErrorSistema):
    """
    Se genera cuando los datos del cliente son incorrectos,
    incompletos o no cumplen con las validaciones establecidas.
    """
    def __init__(self, mensaje="Los datos del cliente son inválidos."):
        super().__init__(mensaje)


class ServicioNoDisponibleError(ErrorSistema):
    """
    Se genera cuando un servicio solicitado no existe,
    no está disponible o contiene parámetros inválidos.
    """
    def __init__(self, mensaje="El servicio solicitado no está disponible."):
        super().__init__(mensaje)


class ReservaError(ErrorSistema):
    """
    Se genera cuando ocurre un problema durante el proceso
    de creación, confirmación o cancelación de una reserva.
    """
    def __init__(self, mensaje="Ha ocurrido un error en la gestión de la reserva."):
        super().__init__(mensaje)


class DuracionInvalidaError(ReservaError):
    """
    Se genera cuando la duración ingresada para una reserva
    es menor o igual a cero.
    """
    def __init__(self, mensaje="La duración de la reserva debe ser mayor a cero."):
        super().__init__(mensaje)


class CostoInvalidoError(ServicioNoDisponibleError):
    """
    Se genera cuando el costo base de un servicio
    presenta valores inválidos.
    """
    def __init__(self, mensaje="El costo del servicio es inválido."):
        super().__init__(mensaje)


class ArchivoLogError(ErrorSistema):
    """
    Se genera cuando ocurre un error al registrar
    eventos o excepciones dentro del archivo log.
    """
    def __init__(self, mensaje="No se pudo registrar el evento en el archivo log."):
        super().__init__(mensaje)


class OperacionNoPermitidaError(ErrorSistema):
    """
    Se genera cuando el usuario intenta ejecutar
    una acción no permitida dentro del sistema.
    """
    def __init__(self, mensaje="La operación solicitada no está permitida."):
        super().__init__(mensaje)


# =========================
# Función opcional de prueba
# =========================

def validar_edad_cliente(edad):
    """
    Ejemplo de validación para demostrar
    el uso de excepciones personalizadas.
    """
    try:
        if edad < 18:
            raise ClienteInvalidoError("El cliente debe ser mayor de edad.")
        return "Edad válida."

    except ClienteInvalidoError as e:
        raise ClienteInvalidoError(f"Error de validación: {str(e)}")
