"""Paquete Préstamos: registros de préstamo y pila LIFO para deshacer."""

from __future__ import annotations

from typing import Iterator, List, Optional


class Prestamo:
    """Préstamo realizado con éxito."""

    def __init__(self, alumno: str, codigo_libro: str) -> None:
        self.alumno = alumno
        self.codigo_libro = codigo_libro

    def __repr__(self) -> str:
        return f"Prestamo({self.alumno!r}, {self.codigo_libro!r})"


class PilaPrestamos:
    """Historial de préstamos (último en entrar, primero en salir).

    Usa una lista de Python: append() es O(1) amortizado y pop() al final es O(1).
    """

    def __init__(self) -> None:
        self._elementos: List[Prestamo] = []

    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0

    def tamano(self) -> int:
        return len(self._elementos)

    def apilar(self, prestamo: Prestamo) -> None:
        self._elementos.append(prestamo)

    def cima(self) -> Optional[Prestamo]:
        """Consulta el último préstamo sin retirarlo. Devuelve None si está vacía."""
        if self.esta_vacia():
            return None
        return self._elementos[-1]

    def desapilar(self) -> Optional[Prestamo]:
        """Retira y devuelve el último préstamo. Devuelve None si está vacía."""
        if self.esta_vacia():
            return None
        return self._elementos.pop()

    def recorrer(self) -> Iterator[Prestamo]:
        """Recorre desde la cima (más reciente) hasta la base, sin modificar la pila."""
        indice = len(self._elementos) - 1
        while indice >= 0:
            yield self._elementos[indice]
            indice -= 1
