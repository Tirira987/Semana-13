import tkinter as tk
from tkinter import ttk


class LoginView(ttk.Frame):

    def __init__(
        self,
        parent,
        restaurante_servicio,
        on_login_success
    ):
        super().__init__(parent)

        self.restaurante_servicio = restaurante_servicio
        self.on_login_success = on_login_success

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ttk.Label(
            self,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        ttk.Label(
            self,
            text="Inicio de sesión"
        ).pack(pady=5)

        ttk.Label(
            self,
            text="Usuario:"
        ).pack(pady=(15, 5))

        self.entrada_usuario = ttk.Entry(
            self,
            width=30
        )
        self.entrada_usuario.pack()

        ttk.Label(
            self,
            text="Contraseña:"
        ).pack(pady=(15, 5))

        self.entrada_contrasena = ttk.Entry(
            self,
            width=30,
            show="*"
        )
        self.entrada_contrasena.pack()

        self.mensaje = ttk.Label(
            self,
            text=""
        )
        self.mensaje.pack(pady=10)

        ttk.Button(
            self,
            text="Ingresar",
            command=self.iniciar_sesion
        ).pack(pady=10)

        ttk.Label(
            self,
            text="Prueba: richi / 6666"
        ).pack(pady=5)

        ttk.Label(
            self,
            text="También: maria / 1234"
        ).pack()

        self.entrada_usuario.focus()

    def iniciar_sesion(self):

        nombre_usuario = (
            self.entrada_usuario.get().strip()
        )

        contrasena = self.entrada_contrasena.get()

        if not nombre_usuario or not contrasena:
            self.mensaje.config(
                text="Ingrese usuario y contraseña."
            )
            return

        usuario = self.restaurante_servicio.validar_acceso(
            nombre_usuario,
            contrasena
        )

        if usuario is not None:

            self.on_login_success(usuario)

        else:

            self.mensaje.config(
                text="Usuario o contraseña incorrectos."
            )

            self.entrada_contrasena.delete(0, tk.END)
            self.entrada_contrasena.focus()