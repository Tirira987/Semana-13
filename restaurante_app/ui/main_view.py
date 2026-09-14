import tkinter as tk
from tkinter import ttk


class MainView(ttk.Frame):

    def __init__(
        self,
        parent,
        restaurante_servicio,
        usuario,
        on_logout
    ):
        super().__init__(parent)

        self.restaurante_servicio = restaurante_servicio
        self.usuario = usuario
        self.on_logout = on_logout

        self.crear_interfaz()

    def crear_interfaz(self):

        ttk.Label(
            self,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        ttk.Label(
            self,
            text=f"Bienvenido, {self.usuario.nombre}"
        ).pack(pady=5)

        marco_botones = ttk.Frame(self)
        marco_botones.pack(pady=15)

        ttk.Button(
            marco_botones,
            text="Productos",
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            marco_botones,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            marco_botones,
            text="Ventas (pendiente)",
            command=self.mostrar_ventas_pendiente
        ).grid(row=0, column=2, padx=5)

        self.area_resultado = tk.Text(
            self,
            width=70,
            height=15
        )
        self.area_resultado.pack(
            padx=20,
            pady=10
        )

        marco_informacion = ttk.Frame(self)
        marco_informacion.pack(pady=5)

        ttk.Label(
            marco_informacion,
            text=(
                f"Productos: "
                f"{self.restaurante_servicio.obtener_cantidad_productos()}"
            )
        ).grid(row=0, column=0, padx=20)

        ttk.Label(
            marco_informacion,
            text=(
                f"Usuarios: "
                f"{self.restaurante_servicio.obtener_cantidad_usuarios()}"
            )
        ).grid(row=0, column=1, padx=20)

        ttk.Button(
            self,
            text="Cerrar sesión",
            command=self.on_logout
        ).pack(pady=15)

        self.mostrar_productos()

    def limpiar_area(self):
        self.area_resultado.delete(
            "1.0",
            tk.END
        )

    def mostrar_productos(self):

        self.limpiar_area()

        productos = (
            self.restaurante_servicio
            .obtener_productos()
        )

        self.area_resultado.insert(
            tk.END,
            "=== PRODUCTOS ===\n\n"
        )

        for producto in productos:

            self.area_resultado.insert(
                tk.END,
                f"ID: {producto.id_producto}\n"
                f"Nombre: {producto.nombre}\n"
                f"Precio: ${producto.precio:.2f}\n"
                f"Categoría: {producto.categoria}\n"
                f"Stock: {producto.stock}\n"
                f"{'-' * 40}\n"
            )

    def mostrar_usuarios(self):

        self.limpiar_area()

        usuarios = (
            self.restaurante_servicio
            .obtener_usuarios()
        )

        self.area_resultado.insert(
            tk.END,
            "=== USUARIOS ===\n\n"
        )

        for usuario in usuarios:

            self.area_resultado.insert(
                tk.END,
                f"ID: {usuario.id_usuario}\n"
                f"Nombre: {usuario.nombre}\n"
                f"Rol: {usuario.rol}\n"
                f"{'-' * 40}\n"
            )

    def mostrar_ventas_pendiente(self):

        self.limpiar_area()

        self.area_resultado.insert(
            tk.END,
            "=== VENTAS ===\n\n"
            "Módulo de ventas pendiente para "
            "una futura semana."
        )