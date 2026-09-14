from typing import Optional

from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, productos, usuarios):
        self._productos = productos
        self._usuarios = usuarios

        self._indice_productos = {
            producto.id_producto: producto
            for producto in productos
        }

        self._indice_usuarios = {
            usuario.id_usuario: usuario
            for usuario in usuarios
        }

    def validar_acceso(
        self,
        nombre_usuario: str,
        contrasena: str
    ) -> Optional[Usuario]:

        for usuario in self._usuarios:
            if (
                usuario.nombre_usuario == nombre_usuario
                and usuario.contrasena == contrasena
            ):
                return usuario

        return None

    def obtener_productos(self):
        return list(self._productos)

    def obtener_usuarios(self):
        return list(self._usuarios)

    def buscar_producto(
        self,
        id_producto: int
    ):
        return self._indice_productos.get(id_producto)

    def buscar_usuario(
        self,
        id_usuario: int
    ):
        return self._indice_usuarios.get(id_usuario)

    def obtener_cantidad_productos(self) -> int:
        return len(self._productos)

    def obtener_cantidad_usuarios(self) -> int:
        return len(self._usuarios)