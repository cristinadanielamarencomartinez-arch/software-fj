class Cliente:

    def __init__(self, nombre, cedula, correo):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo


    def mostrar_datos(self):

        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)
        print("Correo:", self.correo)