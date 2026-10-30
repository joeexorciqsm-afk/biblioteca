# 1. Documento de requerimientos y reglas

## 1.1 Problema

Una biblioteca escolar lleva sus registros en papel. Con ese método es difícil saber qué libros están disponibles, quién pidió primero un préstamo y cómo corregir un préstamo registrado por error. El sistema de préstamos resuelve esas tres necesidades con un programa de consola en Python.

## 1.2 Alcance

- Cada código representa un **ejemplar** (si hay dos copias de un título, tienen códigos distintos).
- Quedan fuera de esta versión: devoluciones, multas, aplicación web y persistencia en archivo.
- Los datos viven en memoria mientras el programa está abierto.

## 1.3 Actores

| Actor | Tipo | Descripción |
|---|---|---|
| Bibliotecario | Actor directo | Opera la consola y captura las solicitudes que le comunican los alumnos. |
| Alumno | Interesado | Pide libros al bibliotecario. No usa el programa. Si en el futuro usara la consola, habría que agregarlo como actor y definir sus permisos. |

## 1.4 Requerimientos funcionales

| Código | Requerimiento | Criterio verificable |
|---|---|---|
| RF01 | Registrar libros con código único, título y autor | Se rechaza un código repetido (sin distinguir mayúsculas ni espacios) y cualquier campo vacío. |
| RF02 | Mostrar el catálogo y la disponibilidad de cada libro | La consulta muestra código, título, autor y estado (Disponible o Prestado) en orden de registro. También permite buscar un código. |
| RF03 | Eliminar únicamente libros disponibles y sin solicitudes pendientes | Se rechaza eliminar un libro prestado, un libro con solicitudes en la cola o un código inexistente. |
| RF04 | Registrar solicitudes de libros existentes | Se rechaza la solicitud si el código no existe o falta el nombre del alumno. Cada solicitud recibe un número consecutivo. |
| RF05 | Mostrar las solicitudes pendientes | Se listan del frente al final sin modificar la cola. |
| RF06 | Atender solicitudes en orden de llegada | La primera solicitud registrada es la primera atendida (Ana antes que Luis). |
| RF07 | Guardar cada préstamo exitoso en una pila | Solo se apila un préstamo cuando el libro estaba disponible. |
| RF08 | Deshacer el último préstamo exitoso | Se desapila el último préstamo y su libro vuelve a Disponible. |
| RF09 | Mostrar una copia del catálogo ordenada por título | La copia sale en orden alfabético (Alicia, Don Quijote, El principito) y el catálogo y la cola no cambian. |

## 1.5 Reglas de funcionamiento

| Clave | Regla | Dónde se cumple en el código |
|---|---|---|
| R1 | No se aceptan códigos repetidos ni campos obligatorios vacíos. | `SistemaBiblioteca.registrar_libro()`, `registrar_solicitud()` |
| R2 | Una solicitud no reserva el ejemplar: la disponibilidad se comprueba al atenderla. | `registrar_solicitud()` no cambia el libro; `atender_siguiente()` revisa `disponible`. |
| R3 | Si el libro está prestado, la solicitud se retira sin realizar otro préstamo. | Rama "prestado" de `atender_siguiente()`. |
| R4 | Deshacer libera el libro, pero no devuelve la solicitud a la cola. | `deshacer_prestamo()` |
| R5 | El catálogo original y la cola conservan su orden cuando se muestra la consulta ordenada. | `ordenar_por_titulo()` trabaja sobre una copia. |
| R6 | Burbuja se programa manualmente, sin `sort()` ni `sorted()`. | `ordenamiento.burbuja_por_titulo()` (prueba P09 lo comprueba). |
| R7 | Los códigos se comparan sin espacios extremos y en mayúsculas ("l01" = "L01"). | `normalizar_codigo()` (decisión del equipo). |
| R8 | El orden por título ignora mayúsculas y acentos ("Árbol" va antes que "casa"). | `ordenamiento.clave_titulo()` (decisión del equipo). |

## 1.6 Requerimientos de calidad

| Código | Requerimiento | Cómo se cumple |
|---|---|---|
| RC01 | Validar las opciones del menú | Texto, números fuera de 1-9 o Enter vacío muestran "Opción no válida" y se vuelve a pedir. |
| RC02 | Mostrar mensajes comprensibles | Cada operación devuelve un `Resultado` con un mensaje en español; el menú lo muestra con `[OK]` o `[!]`. |
| RC03 | Evitar errores con estructuras vacías | Cola, pila y lista devuelven `None` o `False` en lugar de lanzar excepciones; el sistema informa "No hay solicitudes pendientes" o "No hay préstamos para deshacer". |
| RC04 | Terminar de forma ordenada | Ctrl+C o Ctrl+D cierran el programa con "Hasta luego." sin mostrar errores. |

## 1.7 Especificación de casos de uso

### CU01 Registrar libro
- **Actor:** Bibliotecario. **Requerimientos:** RF01.
- **Flujo principal:** 1) Elige la opción 1. 2) Escribe código, título y autor. 3) El sistema valida que no haya campos vacíos. 4) Busca el código en la lista. 5) Agrega el libro al final de la lista como Disponible. 6) Informa el registro.
- **Alternativas:** campo vacío → se informa y no se registra; código repetido → se informa y no se registra.

### CU02 Consultar catálogo
- **Actor:** Bibliotecario. **Requerimientos:** RF02.
- **Flujo principal:** 1) Elige la opción 2. 2) Presiona Enter. 3) El sistema recorre la lista desde la cabeza y muestra cada libro con su estado.
- **Alternativas:** escribe un código → se muestra solo ese libro o "No existe un libro con el código…"; catálogo vacío → "El catálogo está vacío".

### CU03 Eliminar libro
- **Actor:** Bibliotecario. **Requerimientos:** RF03.
- **Flujo principal:** 1) Elige la opción 3. 2) Escribe el código. 3) El sistema busca el libro. 4) Verifica que esté disponible. 5) Verifica que no tenga solicitudes en la cola. 6) Desenlaza el nodo. 7) Informa.
- **Alternativas:** código inexistente, libro prestado o con solicitudes pendientes → se informa el motivo y no se elimina.

### CU04 Registrar solicitud de préstamo
- **Actor:** Bibliotecario (captura lo que pide el alumno). **Requerimientos:** RF04.
- **Flujo principal:** 1) Elige la opción 4. 2) Escribe el nombre del alumno y el código. 3) El sistema comprueba que el libro exista. 4) Crea la solicitud con número consecutivo. 5) La encola. 6) Informa.
- **Alternativas:** campo vacío o código inexistente → no se encola. Libro prestado → se encola de todos modos y se avisa (la solicitud no reserva).

### CU05 Consultar solicitudes pendientes
- **Actor:** Bibliotecario. **Requerimientos:** RF05.
- **Flujo principal:** 1) Elige la opción 5. 2) El sistema recorre la cola del frente al final y marca el frente.
- **Alternativa:** cola vacía → "No hay solicitudes pendientes".

### CU06 Atender siguiente solicitud
- **Actor:** Bibliotecario. **Requerimientos:** RF06 y RF07.
- **Precondición del flujo exitoso:** existe una solicitud pendiente y su libro está disponible.
- **Flujo principal:** 1) El bibliotecario selecciona la opción. 2) El sistema retira la solicitud del frente. 3) Busca el libro. 4) Verifica que esté disponible. 5) Lo marca como prestado. 6) Apila el registro del préstamo. 7) Informa el resultado.
- **Alternativas:** cola vacía → se informa y no se modifica ninguna estructura. Libro prestado → se retira la solicitud, se informa la falta de disponibilidad y no se crea un préstamo.
- **Resultado exitoso:** un libro pasa a prestado, se retira una solicitud y se agrega un registro a la pila.

### CU07 Deshacer último préstamo
- **Actor:** Bibliotecario. **Requerimientos:** RF08.
- **Flujo principal:** 1) Elige la opción 7. 2) El sistema desapila el último préstamo. 3) Busca el libro. 4) Lo marca como disponible. 5) Informa qué préstamo se deshizo.
- **Alternativa:** pila vacía → "No hay préstamos para deshacer".
- **Nota:** la solicitud original no vuelve a la cola (regla R4).

### CU08 Consultar catálogo ordenado por título
- **Actor:** Bibliotecario. **Requerimientos:** RF09.
- **Flujo principal:** 1) Elige la opción 8. 2) El sistema copia los libros de la lista. 3) Ordena la copia con burbuja. 4) La muestra.
- **Alternativa:** catálogo vacío → "El catálogo está vacío".
