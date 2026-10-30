"""Ordenamiento burbuja programado manualmente (sin sort() ni sorted())."""

from __future__ import annotations

import unicodedata
from typing import List

from catalogo import Libro


def clave_titulo(titulo: str) -> str:
    """Normaliza el título para compararlo: sin acentos, sin mayúsculas y sin espacios extremos.

    Así "Álgebra" queda junto a "algebra" y no después de la "z".
    """
    descompuesto = unicodedata.normalize("NFD", titulo.strip())
    sin_acentos = "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")
    return sin_acentos.casefold()


def burbuja_por_titulo(libros: List[Libro]) -> List[Libro]:
    """Devuelve una COPIA de la lista ordenada por título con el método burbuja.

    La lista recibida no se modifica. Compara elementos vecinos y los
    intercambia cuando están en desorden. Si en una pasada no hay
    intercambios, la lista ya está ordenada y se termina antes.
    Complejidad: O(n²) en el peor caso, O(n) en el mejor caso (ya ordenada).
    """
    copia: List[Libro] = []
    for libro in libros:
        copia.append(libro)

    n = len(copia)
    for pasada in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - pasada):
            if clave_titulo(copia[j].titulo) > clave_titulo(copia[j + 1].titulo):
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return copia
