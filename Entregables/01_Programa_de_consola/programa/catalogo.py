"""Paquete Catálogo: libros, nodos y lista dinámica enlazada.

Cada código representa un ejemplar. La lista conserva el orden de registro
y se recorre desde la cabeza.
"""

from __future__ import annotations

from typing import Iterator, List, Optional


class Libro:
    """Ejemplar de la biblioteca."""

    def __init__(self, codigo: str, titulo: str, autor: str) -> None:
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """Marca el libro como disponible (True) o prestado (False)."""
        self.disponible = disponible

    def estado(self) -> str:
        return "Disponible" if self.disponible else "Prestado"

    def __repr__(self) -> str:
        return f"Libro({self.codigo!r}, {self.titulo!r}, {self.autor!r}, {self.estado()})"


class NodoLibro:
    """Nodo de la lista enlazada: guarda un objeto Libro y el enlace al siguiente."""

    def __init__(self, libro: Libro) -> None:
        self.libro = libro
        self.siguiente: Optional[NodoLibro] = None


class ListaLibros:
    """Lista simplemente enlazada que funciona como catálogo."""

    def __init__(self) -> None:
        self.cabeza: Optional[NodoLibro] = None
        self._tamano = 0

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def __len__(self) -> int:
        return self._tamano

    def agregar(self, libro: Libro) -> None:
        """Agrega el libro al final para conservar el orden de registro. O(n)."""
        nuevo = NodoLibro(libro)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamano += 1

    def buscar(self, codigo: str) -> Optional[Libro]:
        """Devuelve el libro con ese código o None si no existe. O(n)."""
        actual = self.cabeza
        while actual is not None:
            if actual.libro.codigo == codigo:
                return actual.libro
            actual = actual.siguiente
        return None

    def eliminar(self, codigo: str) -> bool:
        """Desenlaza el nodo con ese código. Devuelve True si lo eliminó. O(n)."""
        anterior: Optional[NodoLibro] = None
        actual = self.cabeza
        while actual is not None:
            if actual.libro.codigo == codigo:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamano -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def recorrer(self) -> Iterator[Libro]:
        """Recorre la lista desde la cabeza. O(n)."""
        actual = self.cabeza
        while actual is not None:
            yield actual.libro
            actual = actual.siguiente

    def a_lista(self) -> List[Libro]:
        """Copia las referencias de los libros a una lista de Python (no altera la lista enlazada)."""
        return [libro for libro in self.recorrer()]
