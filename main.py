from datetime import datetime
from bike import Bike
from reservation import Reservation
from exceptions import BikeUnavailableError, InvalidReservationError

if __name__ == "__main__":
    # Crear bicicleta
    bici1 = Bike("Urbana Pro")
    print("Bicicleta creada:", bici1)

    reservas = []

    # Reserva válida
    try:
        #datatime (año, mes, día, hora, minuto)
        #5 de agosto de 2025, a las 09:00 horas
        inicio = datetime(2025, 8, 5, 9, 0)
        fin = datetime(2025, 8, 5, 12, 30)
        reserva1 = Reservation(bici1, "Marcy", inicio, fin)
        reservas.append(reserva1)
        print("\nReserva realizada:")
        print(reserva1)
    except (BikeUnavailableError, InvalidReservationError, ValueError) as e:
        print("Error al reservar:", e)
    finally:
        print("reserva registrada con exito.")

    # Intento de reserva con bici ya ocupada
    try:
        reserva2 = Reservation(bici1, "Karla", inicio, fin)
        reservas.append(reserva2)
    except BikeUnavailableError as e:
        print("\nError esperado:", e)
    finally:
        print("reserva registrada sin exito, la bici esta ocupada.")

    # Intento de reserva con fechas inválidas
    try:
        reserva3 = Reservation(bici1, "Tripi", fin, inicio)
        reservas.append(reserva3)
    except InvalidReservationError as e:
        print("\nError esperado:", e)
    finally:
        print("reserva registrada sin exito, fechas inválidas.")

    # Finalizar la reserva original
    try:
        reserva1.finalizar()
    except Exception as e:
        print("Error al finalizar:", e)
    finally:
        print("Reserva finalizada registrada.")

    # Nueva reserva válida luego de liberar la bicicleta
    try:
        nuevo_inicio = datetime(2025, 8, 5, 14, 0)
        nuevo_fin = datetime(2025, 8, 5, 16, 0)
        reserva4 = Reservation(bici1, "Valentina", nuevo_inicio, nuevo_fin)
        reservas.append(reserva4)
        print("\nNueva reserva realizada:")
        print(reserva4)
    except Exception as e:
        print("Error inesperado:", e)
    finally:
        print("Intento de nueva reserva registrado.")

    # Estado final
    print("\nEstado final de la bicicleta:", bici1)
    print("Todas las reservas:")
    for r in reservas:
        print("-", r)
