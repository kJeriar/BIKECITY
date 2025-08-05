from bike import Bike

# Crear una bicicleta
bici = Bike("Montaña X")

# Ver estado inicial
print("Estado inicial:", bici.estado)  # Esperado: disponible

# Cambiar a ocupado
try:
    bici.cambiar_estado("ocupado")
    print("Estado después de reservar:", bici.estado)  # Esperado: ocupado
except ValueError as e:
    print("Error:", e)

# Cambiar a disponible nuevamente
try:
    bici.cambiar_estado("disponible")
    print("Estado después de liberar:", bici.estado)  # Esperado: disponible
except ValueError as e:
    print("Error:", e)

# Probar estado inválido
try:
    bici.cambiar_estado("en reparación")
except ValueError as e:
    print("Error esperado por estado inválido:", e)