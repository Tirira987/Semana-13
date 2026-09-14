import tkinter as tk
from tkinter import messagebox

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self, root):

        self.root = root

        self.root.title("Restaurante App")
        self.root.geometry("750x650")
        self.root.resizable(False, False)

        self.archivo_servicio = ArchivoServicio()

        try:
            productos = (
                self.archivo_servicio
                .cargar_productos()
            )

            usuarios = (
                self.archivo_servicio
                .cargar_usuarios()
            )

        except (FileNotFoundError, ValueError) as error:

            messagebox.showerror(
                "Error",
                str(error),
                parent=self.root
            )

            self.root.destroy()
            return

        self.restaurante_servicio = RestauranteServicio(
            productos,
            usuarios
        )

        self.contenedor = tk.Frame(self.root)
        self.contenedor.pack(
            fill="both",
            expand=True
        )

        self.vista_actual = None

        self.mostrar_login()

    def limpiar_vista(self):

        if self.vista_actual is not None:
            self.vista_actual.destroy()

    def mostrar_login(self):

        self.limpiar_vista()

        self.vista_actual = LoginView(
            self.contenedor,
            self.restaurante_servicio,
            self.mostrar_principal
        )

        self.vista_actual.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

    def mostrar_principal(self, usuario):

        self.limpiar_vista()

        self.vista_actual = MainView(
            self.contenedor,
            self.restaurante_servicio,
            usuario,
            self.mostrar_login
        )

        self.vista_actual.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


def main():

    root = tk.Tk()

    Aplicacion(root)

    root.mainloop()


if __name__ == "__main__":
    main()