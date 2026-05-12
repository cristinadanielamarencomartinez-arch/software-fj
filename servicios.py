from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, nombre, costo_base, capacidad):
        super().__init__(nombre, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioNoDisponibleError("Las horas deben ser mayores a cero.")
        return self.costo_base * horas

    def descripcion(self):
        return f"Reserva de sala para {self.capacidad} personas."


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, costo_base, tipo_equipo):
        super().__init__(nombre, costo_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ServicioNoDisponibleError("Los días deben ser mayores a cero.")
        return self.costo_base * dias

    def descripcion(self):
        return f"Alquiler de equipo tipo {self.tipo_equipo}."


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, costo_base, area):
        super().__init__(nombre, costo_base)
        self.area = area

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioNoDisponibleError("Las horas deben ser mayores a cero.")
        return self.costo_base * horas

    def descripcion(self):
        return f"Asesoría especializada en {self.area}."
