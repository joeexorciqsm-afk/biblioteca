"""Paquete Interfaz: menú de consola y entrada de datos.

Ejecutar con:  python menu.py
"""

from __future__ import annotations

from typing import Callable, List, Optional

from sistema import Resultado, SistemaBiblioteca

OPCIONES = [
    "Registrar libro",
    "Consultar catálogo",
    "Eliminar libro",
    "Registrar solicitud de préstamo",
    "Consultar solicitudes pendientes",
    "Atender siguiente solicitud",
    "Deshacer último préstamo",
    "Mostrar libros ordenados por título",
    "Salir",
]


class EntradaTerminada(Exception):
    """Se cerró la entrada estándar (Ctrl+D / Ctrl+Z) o se interrumpió (Ctrl+C)."""


class MenuConsola:
    """Interacción con el bibliotecario. Depende de SistemaBiblioteca."""

    def __init__(self, sistema: SistemaBiblioteca,
                 entrada: Callable[[str], str] = input,
                 salida: Callable[[str], None] = print) -> None:
        self.sistema = sistema
        self._entrada = entrada
        self._salida = salida

    # --------------------------------------------------------- entrada
    def leer_texto(self, mensaje: str) -> str:
        try:
            return self._entrada(mensaje)
        except (EOFError, KeyboardInterrupt):
            raise EntradaTerminada()

    def leer_opcion(self) -> Optional[int]:
        texto = self.leer_texto(f"Elija una opción (1-{len(OPCIONES)}): ").strip()
        if not texto.isdigit():
            return None
        numero = int(texto)
        if 1 <= numero <= len(OPCIONES):
            return numero
        return None

    # --------------------------------------------------------- salida
    def mostrar(self, texto: str = "") -> None:
        self._salida(texto)

    def mostrar_resultado(self, resultado: Resultado) -> None:
        prefijo = "[OK]" if resultado.exito else "[!]"
        self.mostrar(f"{prefijo} {resultado.mensaje}")

    def mostrar_opciones(self) -> None:
        self.mostrar()
        self.mostrar("=" * 46)
        self.mostrar("   SISTEMA DE PRÉSTAMOS - BIBLIOTECA ESCOLAR")
        self.mostrar("=" * 46)
        for numero, texto in enumerate(OPCIONES, start=1):
            self.mostrar(f" {numero}. {texto}")
        self.mostrar("-" * 46)

    def mostrar_tabla_libros(self, libros: List) -> None:
        if not libros:
            self.mostrar("El catálogo está vacío.")
            return
        self.mostrar(f"{'Código':<8} {'Título':<38} {'Autor':<26} Estado")
        self.mostrar("-" * 84)
        for libro in libros:
            self.mostrar(f"{libro.codigo:<8} {libro.titulo[:38]:<38} {libro.autor[:26]:<26} {libro.estado()}")
        self.mostrar(f"Total: {len(libros)} libro(s).")

    # --------------------------------------------------------- opciones
    def opcion_registrar_libro(self) -> None:
        codigo = self.leer_texto("Código: ")
        titulo = self.leer_texto("Título: ")
        autor = self.leer_texto("Autor: ")
        self.mostrar_resultado(self.sistema.registrar_libro(codigo, titulo, autor))

    def opcion_consultar_catalogo(self) -> None:
        codigo = self.leer_texto("Código a buscar (Enter para ver todo el catálogo): ").strip()
        if codigo:
            resultado = self.sistema.buscar_libro(codigo)
            if resultado.exito:
                self.mostrar_tabla_libros([resultado.dato])
            else:
                self.mostrar_resultado(resultado)
            return
        self.mostrar("CATÁLOGO (orden de registro)")
        self.mostrar_tabla_libros(self.sistema.obtener_catalogo())

    def opcion_eliminar_libro(self) -> None:
        codigo = self.leer_texto("Código del libro a eliminar: ")
        self.mostrar_resultado(self.sistema.eliminar_libro(codigo))

    def opcion_registrar_solicitud(self) -> None:
        alumno = self.leer_texto("Nombre del alumno: ")
        codigo = self.leer_texto("Código del libro: ")
        self.mostrar_resultado(self.sistema.registrar_solicitud(alumno, codigo))

    def opcion_consultar_solicitudes(self) -> None:
        pendientes = self.sistema.obtener_solicitudes_pendientes()
        if not pendientes:
            self.mostrar("No hay solicitudes pendientes.")
            return
        self.mostrar("SOLICITUDES PENDIENTES (del frente al final)")
        for posicion, s in enumerate(pendientes, start=1):
            marca = "  <- frente" if posicion == 1 else ""
            self.mostrar(f" {posicion}. #{s.numero} {s.alumno} - {s.codigo_libro}{marca}")

    def opcion_atender(self) -> None:
        self.mostrar_resultado(self.sistema.atender_siguiente())

    def opcion_deshacer(self) -> None:
        self.mostrar_resultado(self.sistema.deshacer_prestamo())

    def opcion_ordenar(self) -> None:
        self.mostrar("CATÁLOGO ORDENADO POR TÍTULO (copia; el catálogo original no cambia)")
        self.mostrar_tabla_libros(self.sistema.ordenar_por_titulo())

    # --------------------------------------------------------- ciclo principal
    def ejecutar(self) -> None:
        acciones = {
            1: self.opcion_registrar_libro,
            2: self.opcion_consultar_catalogo,
            3: self.opcion_eliminar_libro,
            4: self.opcion_registrar_solicitud,
            5: self.opcion_consultar_solicitudes,
            6: self.opcion_atender,
            7: self.opcion_deshacer,
            8: self.opcion_ordenar,
        }
        try:
            while True:
                self.mostrar_opciones()
                opcion = self.leer_opcion()
                if opcion is None:
                    self.mostrar(f"[!] Opción no válida. Escriba un número del 1 al {len(OPCIONES)}.")
                    continue
                if opcion == 9:
                    break
                self.mostrar()
                acciones[opcion]()
        except EntradaTerminada:
            self.mostrar()
        self.mostrar("Hasta luego.")


def main() -> None:
    MenuConsola(SistemaBiblioteca()).ejecutar()


if __name__ == "__main__":
    main()
