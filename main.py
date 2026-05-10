from clientes import Cliente
from logger import Logger

print("=== SISTEMA SOFTWARE FJ ===\n")

# Crear logger
logger = Logger()

# Lista para guardar clientes
clientes = []

# PRUEBA 1: cliente válido
try:
    c1 = Cliente("Daniela", "123", "daniela@gmail.com")
    clientes.append(c1)
    logger.info("Cliente creado correctamente")
except Exception as e:
    logger.error("Error creando cliente: " + str(e))

# PRUEBA 2: cliente inválido
try:
    c2 = Cliente("Juan", "456", "correo_malo")
    clientes.append(c2)
except Exception as e:
    logger.error("Error controlado: " + str(e))

# MOSTRAR CLIENTES
print("\n=== LISTA DE CLIENTES ===")
for c in clientes:
    c.mostrar_datos()

# PRUEBAS DE ERRORES
print("\n=== PRUEBAS DE ERRORES ===")

try:
    numero = int("abc")
except Exception as e:
    logger.error("Error capturado: " + str(e))

try:
    lista = []
    print(lista[1])
except Exception as e:
    logger.error("Error capturado: " + str(e))

print("\nEl sistema sigue funcionando correctamente 😎")

# MÁS PRUEBAS
print("\n=== MÁS PRUEBAS ===")

try:
    x = int("abc")
except Exception as e:
    logger.error(str(e))

try:
    y = 10 / 0
except Exception as e:
    logger.error(str(e))

try:
    lista = []
    print(lista[10])
except Exception as e:
    logger.error(str(e))