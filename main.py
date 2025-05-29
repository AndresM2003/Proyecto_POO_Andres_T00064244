import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gestora_ventas import GestoraVentas
from producto import Producto, Cliente

# Clase que representa la interfaz gráfica para gestionar ventas
class InterfazGestoraVentas:
    def __init__(self, root, gestora):
        # Inicializa la ventana principal y las pestañas
        self.root = root
        self.gestora = gestora
        self.root.title("Gestora de Ventas de Productos Electrónicos")
        self.root.geometry("600x400")

        # Crear pestañas
        self.tab_control = ttk.Notebook(root)
        self.tab_productos = ttk.Frame(self.tab_control)
        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_ventas = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_productos, text="Productos")
        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.add(self.tab_ventas, text="Ventas")
        self.tab_control.pack(expand=1, fill="both")

        # Pestaña Productos
        self.crear_tab_productos()

        # Pestaña Clientes
        self.crear_tab_clientes()

        # Pestaña Ventas
        self.crear_tab_ventas()

    def crear_tab_productos(self):
        # Configura la pestaña de gestión de productos
        ttk.Label(self.tab_productos, text="Gestión de Productos").pack(pady=10)

        # Listar productos
        self.productos_listbox = tk.Listbox(self.tab_productos, width=80)
        self.productos_listbox.pack(pady=10)
        self.actualizar_lista_productos()

        # Formulario para agregar productos
        ttk.Label(self.tab_productos, text="Agregar Producto").pack(pady=5)
        self.producto_id = tk.Entry(self.tab_productos, width=10)
        self.producto_nombre = tk.Entry(self.tab_productos, width=20)
        self.producto_categoria = tk.Entry(self.tab_productos, width=20)
        self.producto_precio = tk.Entry(self.tab_productos, width=10)
        self.producto_stock = tk.Entry(self.tab_productos, width=10)

        # Etiquetas y campos de entrada
        ttk.Label(self.tab_productos, text="ID").pack()
        self.producto_id.pack()
        ttk.Label(self.tab_productos, text="Nombre").pack()
        self.producto_nombre.pack()
        ttk.Label(self.tab_productos, text="Categoría").pack()
        self.producto_categoria.pack()
        ttk.Label(self.tab_productos, text="Precio").pack()
        self.producto_precio.pack()
        ttk.Label(self.tab_productos, text="Stock").pack()
        self.producto_stock.pack()

        # Botón para agregar producto
        ttk.Button(self.tab_productos, text="Agregar Producto", command=self.agregar_producto).pack(pady=10)

    def crear_tab_clientes(self):
        # Configura la pestaña de gestión de clientes
        ttk.Label(self.tab_clientes, text="Gestión de Clientes").pack(pady=10)

        # Listar clientes
        self.clientes_listbox = tk.Listbox(self.tab_clientes, width=80)
        self.clientes_listbox.pack(pady=10)
        self.actualizar_lista_clientes()

        # Formulario para agregar clientes
        ttk.Label(self.tab_clientes, text="Agregar Cliente").pack(pady=5)
        self.cliente_id = tk.Entry(self.tab_clientes, width=10)
        self.cliente_nombre = tk.Entry(self.tab_clientes, width=20)
        self.cliente_email = tk.Entry(self.tab_clientes, width=30)

        # Etiquetas y campos de entrada
        ttk.Label(self.tab_clientes, text="ID").pack()
        self.cliente_id.pack()
        ttk.Label(self.tab_clientes, text="Nombre").pack()
        self.cliente_nombre.pack()
        ttk.Label(self.tab_clientes, text="Email").pack()
        self.cliente_email.pack()

        # Botón para agregar cliente
        ttk.Button(self.tab_clientes, text="Agregar Cliente", command=self.agregar_cliente).pack(pady=10)

    def crear_tab_ventas(self):
        # Configura la pestaña de gestión de ventas
        ttk.Label(self.tab_ventas, text="Gestión de Ventas").pack(pady=10)

        # Listar ventas
        self.ventas_listbox = tk.Listbox(self.tab_ventas, width=80)
        self.ventas_listbox.pack(pady=10)
        self.actualizar_lista_ventas()

        # Formulario para realizar ventas
        ttk.Label(self.tab_ventas, text="Realizar Venta").pack(pady=5)
        self.venta_cliente_id = tk.Entry(self.tab_ventas, width=10)
        self.venta_productos = tk.Entry(self.tab_ventas, width=40)

        # Etiquetas y campos de entrada
        ttk.Label(self.tab_ventas, text="ID Cliente").pack()
        self.venta_cliente_id.pack()
        ttk.Label(self.tab_ventas, text="Productos (ID, Cantidad)").pack()
        self.venta_productos.pack()

        # Botón para realizar venta
        ttk.Button(self.tab_ventas, text="Realizar Venta", command=self.realizar_venta).pack(pady=10)

    def actualizar_lista_productos(self):
        # Actualiza la lista de productos en la interfaz
        self.productos_listbox.delete(0, tk.END)
        for producto in self.gestora.productos:
            self.productos_listbox.insert(tk.END, str(producto))

    def actualizar_lista_clientes(self):
        # Actualiza la lista de clientes en la interfaz
        self.clientes_listbox.delete(0, tk.END)
        for cliente in self.gestora.clientes:
            self.clientes_listbox.insert(tk.END, str(cliente))

    def actualizar_lista_ventas(self):
        # Actualiza la lista de ventas en la interfaz
        self.ventas_listbox.delete(0, tk.END)
        for venta in self.gestora.ventas:
            self.ventas_listbox.insert(tk.END, str(venta))

    def agregar_producto(self):
        # Agrega un nuevo producto al sistema
        try:
            id = int(self.producto_id.get())
            nombre = self.producto_nombre.get()
            categoria = self.producto_categoria.get()
            precio = float(self.producto_precio.get())
            stock = int(self.producto_stock.get())
            producto = self.gestora.crear_producto(id, nombre, categoria, precio, stock)
            self.gestora.agregar_producto(producto)
            self.actualizar_lista_productos()
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def agregar_cliente(self):
        # Agrega un nuevo cliente al sistema
        try:
            id = int(self.cliente_id.get())
            nombre = self.cliente_nombre.get()
            email = self.cliente_email.get()
            cliente = self.gestora.crear_cliente(id, nombre, email)
            self.gestora.agregar_cliente(cliente)
            self.actualizar_lista_clientes()
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def realizar_venta(self):
        # Realiza una nueva venta en el sistema
        try:
            cliente_id = int(self.venta_cliente_id.get())
            productos_vendidos = eval(self.venta_productos.get())  # Formato: [(ID, Cantidad), ...]
            venta = self.gestora.realizar_venta(cliente_id, productos_vendidos)
            self.actualizar_lista_ventas()
            self.actualizar_lista_productos()
            messagebox.showinfo("Éxito", f"Venta realizada correctamente.\n{venta}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Ejemplo de uso
if __name__ == "__main__":
    # Inicializa la aplicación con una instancia de GestoraVentas
    gestora = GestoraVentas()
    root = tk.Tk()
    app = InterfazGestoraVentas(root, gestora)
    root.mainloop()