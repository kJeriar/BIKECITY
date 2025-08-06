'''
Recibir una bicicleta, cliente, fecha de inicio y fin.

Validar que:

La fecha de inicio sea menor que la de fin → InvalidReservationError

La bicicleta esté disponible → BikeUnavailableError

Calcular duración y precio.

Cambiar el estado de la bicicleta.

Marcar la reserva como "activa".

Permitir finalizar la reserva, cambiando estados.
'''


from datetime import datetime
import math
from exceptions import BikeUnavailableError, InvalidReservationError

class Reservation:
    # Tarifa fija por hora
    tarifa_por_hora = 10

    def __init__(self, bike, cliente, inicio, fin):
        # Validación de fechas
        if inicio >= fin:
            raise InvalidReservationError("La fecha de inicio debe ser menor que la de fin.")

        # Validación de disponibilidad
        if bike.estado != "disponible":
            raise BikeUnavailableError("La bicicleta no está disponible para reservar.")

        self.bike = bike
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin

        self.duracion = self.calcular_duracion()
        self.precio = self.calcular_precio()
        self.estado = "activa"

        # Cambia el estado de la bicicleta a ocupado
        self.bike.cambiar_estado("ocupado")

    def calcular_duracion(self):
        #Devuelve la duración en horas, redondeada hacia arriba.
        segundos = (self.fin - self.inicio).total_seconds()
        horas = segundos / 3600
        return math.ceil(horas)

    def calcular_precio(self):
        #Calcula el precio total según la duración.
        return self.duracion * self.tarifa_por_hora

    def finalizar(self):
       #Finaliza la reserva: cambia estados y muestra el total cobrado.
        self.estado = "completada"
        self.bike.cambiar_estado("disponible")
        print(f"\nReserva finalizada. Total cobrado a {self.cliente}: {self.precio} unidades.")

    def __str__(self):
        return (f"Reserva de {self.cliente} | {self.bike.modelo} | "
                f"{self.duracion}h | {self.precio} unidades | Estado: {self.estado}")