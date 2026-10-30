"""Paquete Solicitudes: solicitudes de préstamo y cola FIFO."""

from __future__ import annotations

from collections import deque
from typing import Deque, Iterator, Optional


class Solicitud:
    """Solicitud de préstamo capturada por el bibliotecario."""

    def __init__(self, numero: int, alumno: str, codigo_libro: str) -> None:
        self.numero = numero
        self.alumno = alumno
        self.codigo_libro = codigo_libro

    def __repr__(self) -> str:
        return f"Solicitud(#{self.numero}, {self.alumno!r}, {self.codigo_libro!r})"


class ColaSolicitudes:
    """Cola de solicitudes pendientes (primero en llegar, primero en atenderse).

    Se implementa con collections.deque: encolar y desencolar son O(1).
    """

    def __init__(self) -> None:
        self._elementos: Deque[Solicitud] = deque()

    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0

    def tamano(self) -> int:
        return len(self._elementos)

    def encolar(self, solicitud: Solicitud) -> None:
        """Agrega la solicitud al final. O(1)."""
        self._elementos.append(solicitud)

    def frente(self) -> Optional[Solicitud]:
        """Consulta la primera solicitud sin retirarla. Devuelve None si está vacía. O(1)."""
        if self.esta_vacia():
            return None
        return self._elementos[0]

    def desencolar(self) -> Optional[Solicitud]:
        """Retira y devuelve la primera solicitud. Devuelve None si está vacía. O(1)."""
        if self.esta_vacia():
            return None
        return self._elementos.popleft()

    def recorrer(self) -> Iterator[Solicitud]:
        """Recorre del frente al final sin modificar la cola. O(n)."""
        for solicitud in self._elementos:
            yield solicitud

    def contiene_libro(self, codigo_libro: str) -> bool:
        """Indica si hay alguna solicitud pendiente para ese libro. O(n)."""
        for solicitud in self._elementos:
            if solicitud.codigo_libro == codigo_libro:
                return True
        return False
