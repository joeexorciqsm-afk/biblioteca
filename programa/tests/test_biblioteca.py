"""Pruebas automáticas del sistema de biblioteca.

Ejecutar desde la carpeta programa/:
    python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

CARPETA_PROGRAMA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CARPETA_PROGRAMA)

from catalogo import Libro, ListaLibros  # noqa: E402
from menu import MenuConsola  # noqa: E402
from ordenamiento import burbuja_por_titulo  # noqa: E402
from prestamos import PilaPrestamos, Prestamo  # noqa: E402
from sistema import SistemaBiblioteca  # noqa: E402
from solicitudes import ColaSolicitudes, Solicitud  # noqa: E402


def sistema_con_libros():
    s = SistemaBiblioteca()
    s.registrar_libro("L01", "El principito", "Antoine de Saint-Exupéry")
    s.registrar_libro("L02", "Don Quijote de la Mancha", "Miguel de Cervantes")
    s.registrar_libro("L03", "Alicia en el país de las maravillas", "Lewis Carroll")
    return s


# --------------------------------------------------------------------- estructuras
class PruebasListaLibros(unittest.TestCase):
    def test_P01_lista_vacia(self):
        lista = ListaLibros()
        self.assertTrue(lista.esta_vacia())
        self.assertIsNone(lista.buscar("X"))
        self.assertFalse(lista.eliminar("X"))
        self.assertEqual(lista.a_lista(), [])

    def test_P02_agregar_conserva_orden_y_nodo_guarda_libro(self):
        lista = ListaLibros()
        for c in ("A", "B", "C"):
            lista.agregar(Libro(c, "t" + c, "a"))
        self.assertEqual([l.codigo for l in lista.recorrer()], ["A", "B", "C"])
        self.assertIsInstance(lista.cabeza.libro, Libro)
        self.assertEqual(len(lista), 3)

    def test_P03_eliminar_cabeza_medio_y_final(self):
        lista = ListaLibros()
        for c in ("A", "B", "C", "D"):
            lista.agregar(Libro(c, "t", "a"))
        self.assertTrue(lista.eliminar("A"))
        self.assertTrue(lista.eliminar("C"))
        self.assertTrue(lista.eliminar("D"))
        self.assertEqual([l.codigo for l in lista.recorrer()], ["B"])
        self.assertEqual(len(lista), 1)


class PruebasColaYPila(unittest.TestCase):
    def test_P04_cola_fifo_y_vacia(self):
        cola = ColaSolicitudes()
        self.assertIsNone(cola.desencolar())
        self.assertIsNone(cola.frente())
        cola.encolar(Solicitud(1, "Ana", "L01"))
        cola.encolar(Solicitud(2, "Luis", "L02"))
        self.assertEqual(cola.frente().alumno, "Ana")
        self.assertEqual(cola.desencolar().alumno, "Ana")
        self.assertEqual(cola.desencolar().alumno, "Luis")
        self.assertTrue(cola.esta_vacia())

    def test_P05_pila_lifo_y_vacia(self):
        pila = PilaPrestamos()
        self.assertIsNone(pila.desapilar())
        pila.apilar(Prestamo("Ana", "L01"))
        pila.apilar(Prestamo("Luis", "L02"))
        self.assertEqual(pila.cima().alumno, "Luis")
        self.assertEqual(pila.desapilar().alumno, "Luis")
        self.assertEqual(pila.desapilar().alumno, "Ana")
        self.assertTrue(pila.esta_vacia())


class PruebasBurbuja(unittest.TestCase):
    def test_P06_burbuja_ordena_sin_alterar_original(self):
        libros = [Libro("1", "El principito", "x"), Libro("2", "Don Quijote", "x"), Libro("3", "Alicia", "x")]
        ordenados = burbuja_por_titulo(libros)
        self.assertEqual([l.titulo for l in ordenados], ["Alicia", "Don Quijote", "El principito"])
        self.assertEqual([l.titulo for l in libros], ["El principito", "Don Quijote", "Alicia"])

    def test_P07_burbuja_ignora_acentos_y_mayusculas(self):
        libros = [Libro("1", "zorro", "x"), Libro("2", "Árbol", "x"), Libro("3", "casa", "x")]
        self.assertEqual([l.titulo for l in burbuja_por_titulo(libros)], ["Árbol", "casa", "zorro"])

    def test_P08_burbuja_casos_limite(self):
        self.assertEqual(burbuja_por_titulo([]), [])
        uno = [Libro("1", "Solo", "x")]
        self.assertEqual(burbuja_por_titulo(uno)[0].titulo, "Solo")

    def test_P09_no_usa_sort_ni_sorted(self):
        with open(os.path.join(CARPETA_PROGRAMA, "ordenamiento.py"), encoding="utf-8") as f:
            codigo = [linea for linea in f if not linea.strip().startswith(("#", '"""'))]
        texto = "".join(codigo)
        self.assertNotIn(".sort(", texto)
        self.assertNotIn("sorted(", texto)


# --------------------------------------------------------------------- reglas del sistema
class PruebasSistema(unittest.TestCase):
    def test_P10_RF01_rechaza_codigo_repetido(self):
        s = sistema_con_libros()
        r = s.registrar_libro("L01", "Otro", "Otro")
        self.assertFalse(r.exito)
        r2 = s.registrar_libro(" l01 ", "Otro", "Otro")  # mismo código con minúsculas y espacios
        self.assertFalse(r2.exito)
        self.assertEqual(len(s.obtener_catalogo()), 3)

    def test_P11_RF01_rechaza_campos_vacios(self):
        s = SistemaBiblioteca()
        self.assertFalse(s.registrar_libro("", "T", "A").exito)
        self.assertFalse(s.registrar_libro("L09", "   ", "A").exito)
        self.assertFalse(s.registrar_libro("L09", "T", "").exito)
        self.assertEqual(s.obtener_catalogo(), [])

    def test_P12_RF02_catalogo_muestra_disponibilidad(self):
        s = sistema_con_libros()
        self.assertTrue(all(l.disponible for l in s.obtener_catalogo()))
        s.registrar_solicitud("Ana", "L01")
        s.atender_siguiente()
        self.assertEqual(s.buscar_libro("L01").dato.estado(), "Prestado")

    def test_P13_RF02_buscar_codigo_inexistente(self):
        s = sistema_con_libros()
        self.assertFalse(s.buscar_libro("L99").exito)

    def test_P14_RF03_eliminar_permitido(self):
        s = sistema_con_libros()
        self.assertTrue(s.eliminar_libro("L03").exito)
        self.assertIsNone(s.catalogo.buscar("L03"))

    def test_P15_RF03_no_elimina_con_solicitud_pendiente(self):
        s = sistema_con_libros()
        s.registrar_solicitud("Ana", "L01")
        r = s.eliminar_libro("L01")
        self.assertFalse(r.exito)
        self.assertIn("solicitudes pendientes", r.mensaje)
        self.assertIsNotNone(s.catalogo.buscar("L01"))

    def test_P16_RF03_no_elimina_prestado_ni_inexistente(self):
        s = sistema_con_libros()
        s.registrar_solicitud("Ana", "L01")
        s.atender_siguiente()
        self.assertFalse(s.eliminar_libro("L01").exito)
        self.assertFalse(s.eliminar_libro("L99").exito)

    def test_P17_RF04_solicitud_de_libro_inexistente(self):
        s = sistema_con_libros()
        r = s.registrar_solicitud("Ana", "L99")
        self.assertFalse(r.exito)
        self.assertTrue(s.solicitudes.esta_vacia())
        self.assertFalse(s.registrar_solicitud("", "L01").exito)

    def test_P18_RF04_solicitud_no_reserva(self):
        s = sistema_con_libros()
        s.registrar_solicitud("Ana", "L01")
        self.assertTrue(s.catalogo.buscar("L01").disponible)

    def test_P19_RF06_cola_vacia_no_modifica_nada(self):
        s = sistema_con_libros()
        r = s.atender_siguiente()
        self.assertFalse(r.exito)
        self.assertTrue(s.prestamos.esta_vacia())
        self.assertTrue(all(l.disponible for l in s.obtener_catalogo()))

    def test_P20_RF06_libro_prestado_retira_solicitud_sin_prestamo(self):
        s = sistema_con_libros()
        s.registrar_solicitud("Ana", "L01")
        s.registrar_solicitud("Luis", "L01")
        s.atender_siguiente()
        r = s.atender_siguiente()
        self.assertFalse(r.exito)
        self.assertIn("Sin disponibilidad", r.mensaje)
        self.assertTrue(s.solicitudes.esta_vacia())
        self.assertEqual(s.prestamos.tamano(), 1)

    def test_P21_RF08_pila_vacia(self):
        s = sistema_con_libros()
        self.assertFalse(s.deshacer_prestamo().exito)

    def test_P22_RF08_deshacer_no_regresa_solicitud(self):
        s = sistema_con_libros()
        s.registrar_solicitud("Ana", "L01")
        s.atender_siguiente()
        s.deshacer_prestamo()
        self.assertTrue(s.catalogo.buscar("L01").disponible)
        self.assertTrue(s.solicitudes.esta_vacia())

    def test_P23_RF09_ordenar_no_altera_catalogo_ni_cola(self):
        s = sistema_con_libros()
        s.registrar_solicitud("Marta", "L03")
        s.registrar_solicitud("Ana", "L01")
        antes_catalogo = [l.codigo for l in s.obtener_catalogo()]
        antes_cola = [x.numero for x in s.obtener_solicitudes_pendientes()]
        ordenados = s.ordenar_por_titulo()
        self.assertEqual([l.codigo for l in ordenados], ["L03", "L02", "L01"])
        self.assertEqual([l.codigo for l in s.obtener_catalogo()], antes_catalogo)
        self.assertEqual([x.numero for x in s.obtener_solicitudes_pendientes()], antes_cola)


# --------------------------------------------------------------------- prueba final integrada
class PruebaFinalIntegrada(unittest.TestCase):
    def test_P24_escenario_integrado(self):
        s = SistemaBiblioteca()
        # 1. Registrar L01, L02 y L03
        self.assertTrue(s.registrar_libro("L01", "El principito", "Antoine de Saint-Exupéry").exito)
        self.assertTrue(s.registrar_libro("L02", "Don Quijote de la Mancha", "Miguel de Cervantes").exito)
        self.assertTrue(s.registrar_libro("L03", "Alicia en el país de las maravillas", "Lewis Carroll").exito)
        # 2. No se acepta otro L01
        self.assertFalse(s.registrar_libro("L01", "Duplicado", "X").exito)
        # 3. Solicitudes de Ana, Luis y Marta en ese orden
        s.registrar_solicitud("Ana", "L01")
        s.registrar_solicitud("Luis", "L02")
        s.registrar_solicitud("Marta", "L03")
        # 4. Atender a Ana y después a Luis
        self.assertIn("Ana", s.atender_siguiente().mensaje)
        self.assertIn("Luis", s.atender_siguiente().mensaje)
        # 5. Ambos préstamos están en la pila (Luis en la cima)
        self.assertEqual([p.alumno for p in s.obtener_historial_prestamos()], ["Luis", "Ana"])
        # 6. Deshacer el préstamo de Luis
        r = s.deshacer_prestamo()
        self.assertEqual(r.dato.alumno, "Luis")
        # 7. L02 vuelve a disponible y Marta sigue pendiente
        self.assertTrue(s.catalogo.buscar("L02").disponible)
        self.assertFalse(s.catalogo.buscar("L01").disponible)
        self.assertEqual([x.alumno for x in s.obtener_solicitudes_pendientes()], ["Marta"])
        # 8. Catálogo ordenado por título
        titulos = [l.titulo for l in s.ordenar_por_titulo()]
        self.assertEqual(titulos, ["Alicia en el país de las maravillas", "Don Quijote de la Mancha", "El principito"])
        # 9. El ordenamiento no altera la cola ni el catálogo original
        self.assertEqual([x.alumno for x in s.obtener_solicitudes_pendientes()], ["Marta"])
        self.assertEqual([l.codigo for l in s.obtener_catalogo()], ["L01", "L02", "L03"])


# --------------------------------------------------------------------- menú (requerimientos de calidad)
class PruebasMenu(unittest.TestCase):
    def ejecutar_menu(self, entradas):
        salida = []
        datos = iter(entradas)

        def entrada(_mensaje):
            try:
                return next(datos)
            except StopIteration:
                raise EOFError

        sistema = SistemaBiblioteca()
        MenuConsola(sistema, entrada=entrada, salida=salida.append).ejecutar()
        return sistema, "\n".join(salida)

    def test_P25_menu_valida_opciones(self):
        _, texto = self.ejecutar_menu(["abc", "0", "10", "", "9"])
        self.assertEqual(texto.count("Opción no válida"), 4)
        self.assertIn("Hasta luego", texto)

    def test_P26_menu_estructuras_vacias_sin_errores(self):
        _, texto = self.ejecutar_menu(["2", "", "5", "6", "7", "8", "3", "L01", "9"])
        self.assertIn("El catálogo está vacío", texto)
        self.assertIn("No hay solicitudes pendientes", texto)
        self.assertIn("No hay préstamos para deshacer", texto)
        self.assertIn("No existe un libro con el código L01", texto)

    def test_P27_menu_flujo_completo(self):
        sistema, texto = self.ejecutar_menu([
            "1", "L01", "El principito", "Saint-Exupéry",
            "4", "Ana", "L01",
            "6",
            "9",
        ])
        self.assertIn("Préstamo realizado", texto)
        self.assertEqual(sistema.prestamos.tamano(), 1)

    def test_P28_menu_fin_de_entrada(self):
        _, texto = self.ejecutar_menu([])  # Ctrl+D sin escribir nada
        self.assertIn("Hasta luego", texto)


if __name__ == "__main__":
    unittest.main(verbosity=2)
