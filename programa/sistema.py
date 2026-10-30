"""Componente sistema: «servicioBiblioteca».

SistemaBiblioteca coordina las reglas de negocio y las operaciones sobre el
catálogo (lista enlazada), las solicitudes (cola) y los préstamos (pila).
No lee del teclado ni imprime: devuelve un Resultado que el menú muestra.
"""

from __future__ import annotations

from typing import Any, List

from catalogo import Libro, ListaLibros
from ordenamiento import burbuja_por_titulo
from prestamos import PilaPrestamos, Prestamo
from solicitudes import ColaSolicitudes, Solicitud


class Resultado:
    """Respuesta de una operación: si tuvo éxito, un mensaje comprensible y un dato opcional."""

    def __init__(self, exito: bool, mensaje: str, dato: Any = None) -> None:
        self.exito = exito
        self.mensaje = mensaje
        self.dato = dato

    def __repr__(self) -> str:
        return f"Resultado({self.exito}, {self.mensaje!r})"


def normalizar_codigo(codigo: str) -> str:
    """Los códigos se comparan sin espacios extremos y en mayúsculas ("l01" == "L01")."""
    return codigo.strip().upper()


class SistemaBiblioteca:
    """«servicioBiblioteca»: coordina catálogo, cola de solicitudes y pila de préstamos."""

    def __init__(self) -> None:
        self.catalogo = ListaLibros()
        self.solicitudes = ColaSolicitudes()
        self.prestamos = PilaPrestamos()
        self._siguiente_numero = 1

    # ------------------------------------------------------------------ RF01
    def registrar_libro(self, codigo: str, titulo: str, autor: str) -> Resultado:
        codigo = normalizar_codigo(codigo)
        titulo = titulo.strip()
        autor = autor.strip()
        if not codigo or not titulo or not autor:
            return Resultado(False, "Código, título y autor son obligatorios.")
        if self.catalogo.buscar(codigo) is not None:
            return Resultado(False, f"Ya existe un libro con el código {codigo}.")
        libro = Libro(codigo, titulo, autor)
        self.catalogo.agregar(libro)
        return Resultado(True, f"Libro {codigo} «{titulo}» registrado.", libro)

    # ------------------------------------------------------------------ RF02
    def obtener_catalogo(self) -> List[Libro]:
        return self.catalogo.a_lista()

    def buscar_libro(self, codigo: str) -> Resultado:
        codigo = normalizar_codigo(codigo)
        if not codigo:
            return Resultado(False, "Debe escribir un código.")
        libro = self.catalogo.buscar(codigo)
        if libro is None:
            return Resultado(False, f"No existe un libro con el código {codigo}.")
        return Resultado(True, "Libro encontrado.", libro)

    # ------------------------------------------------------------------ RF03
    def eliminar_libro(self, codigo: str) -> Resultado:
        codigo = normalizar_codigo(codigo)
        if not codigo:
            return Resultado(False, "Debe escribir un código.")
        libro = self.catalogo.buscar(codigo)
        if libro is None:
            return Resultado(False, f"No existe un libro con el código {codigo}.")
        if not libro.disponible:
            return Resultado(False, f"No se puede eliminar {codigo}: está prestado.")
        if self.solicitudes.contiene_libro(codigo):
            return Resultado(False, f"No se puede eliminar {codigo}: tiene solicitudes pendientes.")
        self.catalogo.eliminar(codigo)
        return Resultado(True, f"Libro {codigo} «{libro.titulo}» eliminado.", libro)

    # ------------------------------------------------------------------ RF04
    def registrar_solicitud(self, alumno: str, codigo: str) -> Resultado:
        alumno = alumno.strip()
        codigo = normalizar_codigo(codigo)
        if not alumno or not codigo:
            return Resultado(False, "El nombre del alumno y el código del libro son obligatorios.")
        libro = self.catalogo.buscar(codigo)
        if libro is None:
            return Resultado(False, f"No existe un libro con el código {codigo}. Solicitud no registrada.")
        solicitud = Solicitud(self._siguiente_numero, alumno, codigo)
        self._siguiente_numero += 1
        self.solicitudes.encolar(solicitud)
        aviso = "" if libro.disponible else " Aviso: el libro está prestado en este momento."
        return Resultado(
            True,
            f"Solicitud #{solicitud.numero} de {alumno} para {codigo} registrada.{aviso}",
            solicitud,
        )

    # ------------------------------------------------------------------ RF05
    def obtener_solicitudes_pendientes(self) -> List[Solicitud]:
        return [s for s in self.solicitudes.recorrer()]

    # ------------------------------------------------------------ RF06, RF07
    def atender_siguiente(self) -> Resultado:
        """Atiende la solicitud del frente (ver diagramas de actividades y de secuencia)."""
        if self.solicitudes.esta_vacia():
            return Resultado(False, "No hay solicitudes pendientes.")
        solicitud = self.solicitudes.desencolar()
        libro = self.catalogo.buscar(solicitud.codigo_libro)
        if libro is None:
            # No debería ocurrir: se valida al registrar y no se eliminan libros con solicitudes.
            return Resultado(False, f"Solicitud #{solicitud.numero} retirada: el libro {solicitud.codigo_libro} ya no existe.")
        if not libro.disponible:
            return Resultado(
                False,
                f"Sin disponibilidad: {solicitud.alumno} no obtuvo «{libro.titulo}» ({libro.codigo}). "
                f"La solicitud #{solicitud.numero} se retiró.",
                solicitud,
            )
        libro.cambiar_disponibilidad(False)
        prestamo = Prestamo(solicitud.alumno, libro.codigo)
        self.prestamos.apilar(prestamo)
        return Resultado(True, f"Préstamo realizado: «{libro.titulo}» ({libro.codigo}) para {solicitud.alumno}.", prestamo)

    # ------------------------------------------------------------------ RF08
    def deshacer_prestamo(self) -> Resultado:
        """Retira el último préstamo y libera el libro. No devuelve la solicitud a la cola."""
        if self.prestamos.esta_vacia():
            return Resultado(False, "No hay préstamos para deshacer.")
        prestamo = self.prestamos.desapilar()
        libro = self.catalogo.buscar(prestamo.codigo_libro)
        if libro is not None:
            libro.cambiar_disponibilidad(True)
        return Resultado(
            True,
            f"Préstamo deshecho: {prestamo.alumno} - {prestamo.codigo_libro}. El libro vuelve a estar disponible.",
            prestamo,
        )

    def obtener_historial_prestamos(self) -> List[Prestamo]:
        """Préstamos de la cima (más reciente) a la base."""
        return [p for p in self.prestamos.recorrer()]

    # ------------------------------------------------------------------ RF09
    def ordenar_por_titulo(self) -> List[Libro]:
        """Copia del catálogo ordenada con burbuja. El catálogo y la cola no cambian."""
        return burbuja_por_titulo(self.catalogo.a_lista())
