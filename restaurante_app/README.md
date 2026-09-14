# Restaurante App - Semana 13

## Datos del estudiante

- Nombre: Richard Arturo Tirira Díaz
- Carrera: Tecnología de la Información
- Asignatura: Programación Orientada a Objetos
- Semana: 13

## Descripción

Esta nueva base del proyecto Restaurante App tiene como objetivo
incorporar una interfaz gráfica de usuario utilizando Tkinter.
En esta etapa se implementa el inicio de sesión y la visualización
de productos y usuarios, manteniendo una separación entre modelos,
servicios e interfaz gráfica.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
