import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:

    def __init__(self):
        self.ruta_datos = Path(__file__).resolve().parent.parent / "datos"

    def _cargar_datos(self, nombre_archivo: str):
        ruta = self.ruta_datos / nombre_archivo

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"No se encontró el archivo: {ruta}"
            )

        except json.JSONDecodeError:
            raise ValueError(
                f"El archivo {nombre_archivo} no contiene JSON válido."
            )

    def cargar_productos(self):
        datos = self._cargar_datos("productos.json")

        return [
            Producto.desde_diccionario(producto)
            for producto in datos
        ]

    def cargar_usuarios(self):
        datos = self._cargar_datos("usuarios.json")

        return [
            Usuario.desde_diccionario(usuario)
            for usuario in datos
        ]