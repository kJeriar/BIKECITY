# bike
class Bike:
    def __init__(self, modelo):
        self.modelo = modelo
        self.estado = "disponible"
        
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in ["disponible","ocupado"]:
            raise ValueError ("Estado invalido, las opciones correctas son disponible u ocupado.")
        self.estado = nuevo_estado
        
    def __str__(self):
        return f"Bike :{self.modelo} - Estado: {self.estado} "