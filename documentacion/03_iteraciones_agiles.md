# 3. Registro de las tres iteraciones (adaptación escolar inspirada en Scrum)

## 3.1 Concepto

El desarrollo ágil trabaja con entregas frecuentes, colaboración con el usuario y adaptación a lo que se aprende durante el desarrollo. Busca obtener software funcional y mejorarlo con retroalimentación. Ser ágil no significa dejar de planear ni de documentar [3, 4].

Se usó una **adaptación escolar inspirada en Scrum** con tres iteraciones de una semana. Scrum es un marco de trabajo que organiza el desarrollo en sprints con planificación, seguimiento diario, revisión y retrospectiva [5]. Esta adaptación no es una implementación completa de Scrum: el equipo no tiene un Product Owner ni un Scrum Master formales; el bibliotecario hace las veces de usuario que prioriza y revisa.

Cada iteración repitió estos momentos:

| Momento | Aplicación al proyecto |
|---|---|
| Seleccionar y planear | Elegir las funciones prioritarias de la lista de pendientes y acordar cuándo están terminadas. |
| Analizar y modelar | Precisar reglas y actualizar los diagramas que cambian. |
| Construir y probar | Programar y comprobar las funciones elegidas. |
| Revisar con el usuario | Mostrar una versión que funciona y recibir comentarios. |
| Mejorar el proceso | Identificar dificultades del equipo y acordar ajustes. |

## 3.2 Lista priorizada de pendientes (backlog inicial)

| Prioridad | Elemento | Requerimiento | Iteración |
|---|---|---|---|
| 1 | Registrar libros con código único | RF01 | 1 |
| 2 | Mostrar y buscar en el catálogo | RF02 | 1 |
| 3 | Eliminar libros disponibles | RF03 (versión inicial) | 1 |
| 4 | Registrar solicitudes de libros existentes | RF04 | 2 |
| 5 | Mostrar solicitudes pendientes | RF05 | 2 |
| 6 | Atender en orden de llegada y guardar el préstamo | RF06, RF07 | 2 |
| 7 | Deshacer el último préstamo | RF08 | 3 |
| 8 | Catálogo ordenado por título con burbuja | RF09 | 3 |
| 9 | Pruebas integradas y manual | Calidad | 3 |

**Definición de terminado (acordada en la iteración 1):** el código funciona desde el menú, tiene pruebas automáticas que pasan, los mensajes son comprensibles y los diagramas afectados están actualizados.

## 3.3 Iteración 1: Organizar el catálogo (semana 1)

**Objetivo:** registrar, buscar, mostrar y eliminar libros permitidos.

| Tarea | Responsable | Estado |
|---|---|---|
| Clases `Libro`, `NodoLibro` y `ListaLibros` (agregar, buscar, eliminar, recorrer) | Integrante 3 | Terminada |
| Esqueleto de `SistemaBiblioteca` y `Resultado` | Integrante 3 | Terminada |
| Menú con opciones 1, 2, 3 y 9 y validación de opciones | Integrante 2 | Terminada |
| Diagrama de casos de uso y primera versión del diagrama de clases (paquete Catálogo) | Integrante 2 | Terminada |
| Pruebas P01-P03, P10-P14 | Integrante 4 | Terminada |

**Resultado:** versión 0.1. El bibliotecario registró y eliminó libros desde la consola.

**Revisión con el usuario (comentarios del bibliotecario):**
- Escribió "l01" en minúsculas y el sistema lo aceptó como libro nuevo aunque ya existía "L01". Pidió que fueran el mismo código.
- Pidió poder buscar un libro por código sin ver todo el catálogo.
- Pidió que no se pueda eliminar un libro con solicitudes pendientes. Este es el **cambio de requerimiento** registrado (CR-01, sección 4). Como las solicitudes aún no existían, se agregó a la lista de pendientes para la iteración 2.

**Retrospectiva (mejorar el proceso):**
- Dificultad: el código del menú y las reglas estaban mezclados y era difícil probarlos.
- Ajuste: el sistema devuelve un `Resultado` con mensaje y el menú solo muestra; así las reglas se prueban sin teclado.

## 3.4 Iteración 2: Gestionar solicitudes (semana 2)

**Objetivo:** registrar solicitudes y atenderlas con una cola.

| Tarea | Responsable | Estado |
|---|---|---|
| Normalizar códigos (comentario de la iteración 1) y búsqueda por código en la opción 2 | Integrante 3 | Terminada |
| `Solicitud` y `ColaSolicitudes` con `deque` | Integrante 3 | Terminada |
| `registrar_solicitud()` y `atender_siguiente()`; `Prestamo` y `PilaPrestamos` básicos para RF07 | Integrante 3 | Terminada |
| CR-01: `eliminar_libro()` revisa `contiene_libro()` en la cola | Integrante 3 | Terminada |
| Diagramas de actividades y de secuencia de "Atender siguiente solicitud"; actualizar clases | Integrante 2 | Terminada |
| Pruebas P04, P15-P20 | Integrante 4 | Terminada |

**Resultado:** versión 0.2. Ana fue atendida antes que Luis y el préstamo quedó en la pila.

**Revisión con el usuario:**
- Preguntó qué pasa si un alumno pide un libro que ya está prestado. Se confirmó la regla R2/R3: la solicitud se acepta, no reserva y, al atenderla, se retira sin préstamo. Se agregó un aviso al registrarla.
- Aprobó la consulta de solicitudes con la marca "<- frente".

**Retrospectiva:**
- Dificultad: el diagrama de secuencia usaba nombres en camelCase (`atenderSiguiente`) y el código en snake_case.
- Ajuste: los diagramas usan exactamente los nombres del código (`atender_siguiente()`, `esta_vacia()`, `buscar(codigo)`).

## 3.5 Iteración 3: Corregir y organizar (semana 3)

**Objetivo:** deshacer con una pila, ordenar por título e integrar pruebas.

| Tarea | Responsable | Estado |
|---|---|---|
| `deshacer_prestamo()` con `desapilar()` | Integrante 3 | Terminada |
| `burbuja_por_titulo()` sin `sort()` ni `sorted()`, sobre una copia | Integrante 3 | Terminada |
| Menú completo (opciones 1-9) y manejo de Ctrl+C / Ctrl+D | Integrante 2 | Terminada |
| Diagramas de componentes, despliegue y paquetes; leyenda del estereotipo | Integrante 2 | Terminada |
| Pruebas P05-P09, P21-P28 y script `prueba_integrada.py` | Integrante 4 | Terminada |
| Manual de usuario, tabla de trazabilidad y registro de cambios | Integrante 1 | Terminada |

**Resultado:** versión 1.0. Las 28 pruebas automáticas y las 15 verificaciones de la prueba integrada pasan.

**Revisión con el usuario:**
- Notó que "Álgebra" quedaba después de "Zoología" porque la "Á" se comparaba como un carácter distinto. Se corrigió comparando sin acentos ni mayúsculas (regla R8, prueba P07).
- Aprobó que deshacer no regrese la solicitud a la cola.

**Retrospectiva:**
- Dificultad: mantener diagramas, código y pruebas al día en la misma semana.
- Ajuste propuesto para futuras versiones: revisar la tabla de trazabilidad al cerrar cada tarea, no al final de la iteración.
