class Componente:
    def __init__(self, id, name, category, marca, sell_price, buy_price, stock, description, income_date):
        self.id = id
        self.name = name
        self.category = category
        self.marca = marca
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.stock = stock
        self.description = description
        self.income_date = income_date

    def info(self):
        return (f"ID: {self.id}, Name: {self.name}, Category: {self.category}, Marca: {self.marca}, "
                f"Sell Price: {self.sell_price}, Buy Price: {self.buy_price}, Stock: {self.stock}, "
                f"Description: {self.description}, Income Date: {self.income_date}")

# Clases hijas especializadas
class Resistencia(Componente):
    def __init__(self, id, name, marca, sell_price, buy_price, stock, description, income_date, valor, potencia, tipo):
        super().__init__(id, name, "Resistencia", marca, sell_price, buy_price, stock, description, income_date)
        self.valor = valor
        self.potencia = potencia
        self.tipo = tipo
    
    def info(self):
        return super().info() + f", Valor: {self.valor}, Potencia: {self.potencia}, Tipo: {self.tipo}"

class Capacitor(Componente):
    def __init__(self, id, name, marca, sell_price, buy_price, stock, description, income_date, capacitancia, voltaje, tipo):
        super().__init__(id, name, "Capacitor", marca, sell_price, buy_price, stock, description, income_date)
        self.capacitancia = capacitancia
        self.voltaje = voltaje
        self.tipo = tipo
    
    def info(self):
        return super().info() + f", Capacitancia: {self.capacitancia}, Voltaje: {self.voltaje}, Tipo: {self.tipo}"

class Transistor(Componente):
    def __init__(self, id, name, marca, sell_price, buy_price, stock, description, income_date, tipo, hfe, voltaje_max):
        super().__init__(id, name, "Transistor", marca, sell_price, buy_price, stock, description, income_date)
        self.tipo = tipo
        self.hfe = hfe
        self.voltaje_max = voltaje_max
    
    def info(self):
        return super().info() + f", Tipo: {self.tipo}, hFE: {self.hfe}, Voltaje Máximo: {self.voltaje_max}"

class Microcontrolador(Componente):
    def __init__(self, id, name, marca, sell_price, buy_price, stock, description, income_date, arquitectura, memoria, num_pines, voltaje_operacion):
        super().__init__(id, name, "Microcontrolador", marca, sell_price, buy_price, stock, description, income_date)
        self.arquitectura = arquitectura
        self.memoria = memoria
        self.num_pines = num_pines
        self.voltaje_operacion = voltaje_operacion
    
    def info(self):
        return super().info() + f", Arquitectura: {self.arquitectura}, Memoria: {self.memoria}, " \
        f"Pines: {self.num_pines}, Voltaje Operación: {self.voltaje_operacion}"

# Ejemplo de uso
t1 = Transistor(1, "Transistor NPN", "STMicroelectronics", 1.5, 0.8, 100, "Transistor de uso general", "2025-03-27", "NPN", 200, 40)
print(t1.info())
