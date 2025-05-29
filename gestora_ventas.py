import pandas as pd
from datetime import datetime
from producto import Producto, Cliente, Venta
import ast

# Clase que gestiona las operaciones de ventas, productos y clientes
class GestoraVentas:
    def __init__(self, productos_file="productos.xlsx", clientes_file="clientes.xlsx", ventas_file="ventas.xlsx"):
        # Inicializa los archivos y listas para almacenar datos
        self.productos_file = productos_file
        self.clientes_file = clientes_file
        self.ventas_file = ventas_file
        self.productos = []
        self.clientes = []
        self.ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        # Carga los datos de los archivos Excel

        # Cargar productos
        try:
            productos_df = pd.read_excel(self.productos_file)
            for _, row in productos_df.iterrows():
                self.productos.append(Producto(row['ID'], row['Nombre'], row['Categoría'], row['Precio'], row['Stock']))
        except FileNotFoundError:
            # Si el archivo no existe, crea uno vacío
            print(f"No se encontró el archivo {self.productos_file}. Creando archivo vacío.")
            productos_df = pd.DataFrame(columns=['ID', 'Nombre', 'Categoría', 'Precio', 'Stock'])
            productos_df.to_excel(self.productos_file, index=False)

        # Cargar clientes
        try:
            clientes_df = pd.read_excel(self.clientes_file)
            for _, row in clientes_df.iterrows():
                self.clientes.append(Cliente(row['ID'], row['Nombre'], row['Email']))
        except FileNotFoundError:
            # Si el archivo no existe, crea uno vacío
            print(f"No se encontró el archivo {self.clientes_file}. Creando archivo vacío.")
            clientes_df = pd.DataFrame(columns=['ID', 'Nombre', 'Email'])
            clientes_df.to_excel(self.clientes_file, index=False)

        # Cargar ventas
        try:
            ventas_df = pd.read_excel(self.ventas_file)
            for _, row in ventas_df.iterrows():
                cliente = next((c for c in self.clientes if c.id == row['ClienteID']), None)
                try:
                    # Convierte la lista de productos desde texto
                    productos = ast.literal_eval(row['Productos'])
                except (ValueError, SyntaxError):
                    print(f"Error al procesar la columna 'Productos' en la fila: {row}")
                    productos = []  # Manejar el error según sea necesario
                fecha = datetime.strptime(row['Fecha'], "%Y-%m-%d %H:%M:%S")
                self.ventas.append(Venta(row['ID'], cliente, productos, fecha))
        except FileNotFoundError:
            # Si el archivo no existe, crea uno vacío
            print(f"No se encontró el archivo {self.ventas_file}. Creando archivo vacío.")
            ventas_df = pd.DataFrame(columns=['ID', 'ClienteID', 'Productos', 'Fecha'])
            ventas_df.to_excel(self.ventas_file, index=False)

    def guardar_datos(self):
        # Guarda los datos en los archivos Excel

        # Guardar productos
        productos_data = [{'ID': p.id, 'Nombre': p.nombre, 'Categoría': p.categoria, 'Precio': p.precio, 'Stock': p.stock} for p in self.productos]
        productos_df = pd.DataFrame(productos_data)
        productos_df.to_excel(self.productos_file, index=False)

        # Guardar clientes
        clientes_data = [{'ID': c.id, 'Nombre': c.nombre, 'Email': c.email} for c in self.clientes]
        clientes_df = pd.DataFrame(clientes_data)
        clientes_df.to_excel(self.clientes_file, index=False)

        # Guardar ventas
        ventas_data = [{'ID': v.id, 'ClienteID': v.cliente.id, 'Productos': str(v.productos), 'Fecha': v.fecha.strftime("%Y-%m-%d %H:%M:%S")} for v in self.ventas]
        ventas_df = pd.DataFrame(ventas_data)
        ventas_df.to_excel(self.ventas_file, index=False)

    def agregar_producto(self, producto):
        # Agrega un nuevo producto a la lista y guarda los datos
        self.productos.append(producto)
        self.guardar_datos()

    def agregar_cliente(self, cliente):
        # Agrega un nuevo cliente a la lista y guarda los datos
        self.clientes.append(cliente)
        self.guardar_datos()

    def realizar_venta(self, cliente_id, productos_vendidos):
        # Realiza una nueva venta
        cliente = next((c for c in self.clientes if c.id == cliente_id), None)
        if not cliente:
            raise ValueError("Cliente no encontrado")

        productos = []
        for producto_id, cantidad in productos_vendidos:
            producto = next((p for p in self.productos if p.id == producto_id), None)
            if not producto:
                raise ValueError(f"Producto con ID {producto_id} no encontrado")
            if producto.stock < cantidad:
                raise ValueError(f"Stock insuficiente para el producto {producto.nombre}")
            producto.actualizar_stock(-cantidad)
            productos.append((producto, cantidad))

        venta = Venta(len(self.ventas) + 1, cliente, productos)
        self.ventas.append(venta)
        self.guardar_datos()
        return venta

    @staticmethod
    def crear_producto(id, nombre, categoria, precio, stock):
        # Crea una instancia de Producto
        return Producto(id, nombre, categoria, precio, stock)

    @staticmethod
    def crear_cliente(id, nombre, email):
        # Crea una instancia de Cliente
        return Cliente(id, nombre, email)

    @staticmethod
    def crear_venta(id, cliente, productos, fecha=None):
        # Crea una instancia de Venta
        return Venta(id, cliente, productos, fecha)