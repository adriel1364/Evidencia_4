class Cafetera:
    def __init__(self, capacidad, nivel_agua, temperatura):
        self.capacidad = capacidad  # Capacidad máxima de la cafetera en litros
        self.nivel_agua = nivel_agua  # Nivel actual de agua en litros
        self.temperatura = temperatura  # Temperatura actual del agua en grados Celsius

    def preparar_cafe(self, cantidad):
        if self.nivel_agua >= cantidad and self.temperatura >= 90:
            self.nivel_agua -= cantidad
            return f"Preparando {cantidad} litros de café."
        elif self.nivel_agua < cantidad:
            return "No hay suficiente agua para preparar esa cantidad de café."
        else:
            return "La temperatura del agua no es suficiente para preparar café."

    def calentar_agua(self, incremento):
        self.temperatura += incremento
        if self.temperatura > 100:
            self.temperatura = 100  # La temperatura no puede exceder los 100 grados Celsius
        return f"Temperatura actual del agua: {self.temperatura}°C."

    def llenar_agua(self, cantidad): 
        if self.nivel_agua + cantidad <= self.capacidad:
            self.nivel_agua += cantidad
            return f"Nivel de agua actual: {self.nivel_agua} litros."
        else:
            return "No se puede agregar esa cantidad de agua, excede la capacidad de la cafetera."

    def __str__(self): 
        return f"Cafetera(capacidad={self.capacidad}, nivel_agua={self.nivel_agua}, temperatura={self.temperatura})"

# Ejemplo de uso
cafetera = Cafetera(2, 1, 91) # capacidad, nivel_agua, temperatura
print(cafetera.calentar_agua(10)) # incremento       # Incrementa la temperatura a 95°C
print(cafetera.preparar_cafe(4)) # cantidad        # Ahora sí se puede preparar café
print(cafetera.llenar_agua(1)) # cantidad            # Llena la cafetera con 1 litro de agua
print(cafetera)  # Muestra el estado actual de la cafetera