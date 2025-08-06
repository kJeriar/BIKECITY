from datetime import datetime
from exceptions import *

class Reservation():
    def __init__(self, bike, cliente, inicio, fin):
        self.bike = bike
        if self.bike.estado != "disponible":
            raise BikeUnavailableError("Esa bicicleta no esta disponible.\nPor favor solicita otra.")
        else:
            self.bike.cambiar_estado("ocupado")
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        if self.inicio > self.fin:
            raise InvalidReservationError("La fecha de inicio no puede ser posterior a la de fin.\nor favor ingrese fechas validas")
        else: 
            self.duracion = (self.fin - self.inicio).total_seconds()/3600
        self.precio = self.duracion*6840
        self.estado = "activa"



    def finalizar():
        self.estado = "completada"
        self.bike.estado = "disponible"
        print(f"El monto cobrado a {self.cliente} es {self.precio} CLP")