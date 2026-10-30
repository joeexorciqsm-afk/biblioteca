# 6. Tabla de trazabilidad

Relaciona cada requerimiento con los modelos, el código y las pruebas que lo comprueban. Los identificadores de prueba (P01-P28) corresponden a los métodos de `programa/tests/test_biblioteca.py`.

| Requerimiento | Modelos relacionados | Código | Pruebas |
|---|---|---|---|
| RF01 Registrar libro | Casos de uso (CU01), clases | `SistemaBiblioteca.registrar_libro()`, `ListaLibros.agregar()`, `ListaLibros.buscar()` | P10 rechazar código repetido; P11 rechazar campos vacíos; P02; P24 paso 2 |
| RF02 Consultar catálogo | Casos de uso (CU02), clases | `obtener_catalogo()`, `buscar_libro()`, `ListaLibros.recorrer()` | P12 muestra disponibilidad; P13 código inexistente; P26 catálogo vacío |
| RF03 Eliminar libro | Casos de uso (CU03), clases, nota del diagrama de secuencia | `eliminar_libro()`, `ListaLibros.eliminar()`, `ColaSolicitudes.contiene_libro()` | P03; P14 eliminación permitida; P15 con solicitudes pendientes; P16 prestado o inexistente |
| RF04 Registrar solicitud | Casos de uso (CU04), clases | `registrar_solicitud()`, `ColaSolicitudes.encolar()` | P17 libro inexistente; P18 la solicitud no reserva |
| RF05 Consultar solicitudes | Casos de uso (CU05), clases | `obtener_solicitudes_pendientes()`, `ColaSolicitudes.recorrer()` | P23 la cola no cambia; P26 cola vacía |
| RF06 Atender solicitud | Casos de uso (CU06), actividades, secuencia | `atender_siguiente()`, `ColaSolicitudes.desencolar()` | P04 FIFO; P19 cola vacía; P20 libro prestado; P24 Ana sale antes que Luis |
| RF07 Guardar préstamo en pila | Casos de uso (CU06), clases, actividades, secuencia | `PilaPrestamos.apilar()` dentro de `atender_siguiente()` | P20 no se apila sin disponibilidad; P24 paso 5 ambos préstamos en la pila |
| RF08 Deshacer préstamo | Casos de uso (CU07), clases, secuencia (pila) | `deshacer_prestamo()`, `PilaPrestamos.desapilar()` | P05 LIFO; P21 pila vacía; P22 no regresa la solicitud; P24 el último libro prestado vuelve a disponible |
| RF09 Ordenar catálogo | Casos de uso (CU08), componentes (ordenamiento.py) | `ordenar_por_titulo()`, `burbuja_por_titulo()` | P06 Alicia, Don Quijote, El principito; P07 acentos; P08 casos límite; P09 sin sort/sorted; P23 y P24 no alteran catálogo ni cola |
| RC01-RC04 Calidad | Clases (MenuConsola) | `MenuConsola.leer_opcion()`, `ejecutar()` | P25 opciones inválidas; P26 estructuras vacías; P27 flujo completo; P28 fin de entrada |

**Ejemplo de congruencia:** el diagrama de secuencia muestra que `apilar(prestamo)` ocurre solo dentro de `[libro disponible]`. En el código, `self.prestamos.apilar()` está después de la comprobación `if not libro.disponible: return …`, y la prueba P20 verifica que, al atender una segunda solicitud del mismo libro, la pila sigue con un solo préstamo.
