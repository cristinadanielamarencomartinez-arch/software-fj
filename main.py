from clientes import Cliente

print("=== SISTEMA SOFTWARE FJ ===\n")

# Lista para guardar clientes
clientes = []

# PRUEBA 1: cliente válido
try:
    c1 = Cliente("Daniela", "123", "daniela@gmail.com")
    clientes.append(c1)
    print("Cliente creado correctamente\n")
except Exception as e:
    print("Error creando cliente:", e)


# PRUEBA 2: cliente inválido (correo malo)
try:
    c2 = Cliente("Juan", "456", "correo_malo")
    clientes.append(c2)
except Exception as e:
    print("Error controlado:", e, "\n")


# MOSTRAR CLIENTES
print("=== LISTA DE CLIENTES ===")
for c in clientes:
    c.mostrar_datos()
    print("------------------")


# SIMULACIÓN DE ERRORES
print("\n=== PRUEBAS DE ERRORES ===")

try:
    numero = int("abc")  # error intencional
except Exception as e:
    print("Error capturado:", e)


try:
    lista = []
    print(lista[1])  # error intencional
except Exception as e:
    print("Error capturado:", e)


print("\nEl sistema sigue funcionando correctamente 😎")
