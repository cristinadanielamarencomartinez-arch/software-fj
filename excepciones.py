# =========================
# reservas.py
# =========================

from excepciones import ReservaError


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar_reserva(self):
        try:
            if self.duracion <= 0:
                raise ReservaError("La duración debe ser mayor a cero.")

            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"

            return f"Reserva confirmada para {self.cliente.nombre}. Costo total: ${costo}"

        except Exception as e:
            self.estado = "Fallida"
            raise ReservaError(f"Error al confirmar reserva: {str(e)}")

    def cancelar_reserva(self):
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
            return f"La reserva de {self.cliente.nombre} ha sido cancelada."
        else:
            raise ReservaError("No se puede cancelar una reserva no confirmada.")

    def mostrar_estado(self):
        return f"Estado actual de la reserva: {self.estado}"
