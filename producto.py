from datetime import datetime

# Clase que representa un producto en el sistema
class Producto:
    def __init__(self, id, nombre, categoria, precio, stock):
        # Inicializa los atributos del producto
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        # Actualiza el stock del producto, verificando que no sea negativo
        if self.stock + cantidad < 0:
            raise ValueError("Stock insuficiente")
        self.stock += cantidad

    def __str__(self):
        # Representación en cadena del producto
        return f"ID: {self.id}, Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}"


# Clase que representa un cliente en el sistema
class Cliente:
    def __init__(self, id, nombre, email):
        # Inicializa los atributos del cliente
        self.id = id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        # Representación en cadena del cliente
        return f"ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}"


# Clase que representa una venta en el sistema
class Venta:
    def __init__(self, id, cliente, productos, fecha=None):
        # Inicializa los atributos de la venta
        self.id = id
        self.cliente = cliente
        self.productos = productos  # Lista de tuplas (producto, cantidad)
        self.fecha = fecha if fecha else datetime.now()

    def calcular_total(self):
        # Calcula el total de la venta sumando el precio de los productos por su cantidad
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def __str__(self):
        # Representación en cadena de la venta
        productos_str = "\n".join([f"{producto.nombre} x{cantidad}" for producto, cantidad in self.productos])
        return (f"Venta ID: {self.id}\nCliente: {self.cliente.nombre}\nFecha: {self.fecha}\n"
                f"Productos:\n{productos_str}\nTotal: {self.calcular_total()}")