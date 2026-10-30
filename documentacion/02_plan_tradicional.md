# 2. Plan tradicional (modelo en cascada)

## 2.1 Concepto

Una metodología tradicional organiza el desarrollo con una planificación definida al inicio y etapas que tienen productos y revisiones establecidos. El ejemplo estudiado es el **modelo en cascada**: el trabajo avanza principalmente de forma secuencial y cada fase empieza cuando la anterior entregó y aprobó su evidencia. No todas las metodologías tradicionales funcionan exactamente igual [1, 2].

## 2.2 Equipo y roles

> Sustituir los nombres por los integrantes reales del equipo.

| Integrante | Rol principal |
|---|---|
| Integrante 1 | Líder de proyecto y analista |
| Integrante 2 | Diseñador (UML) |
| Integrante 3 | Programador |
| Integrante 4 | Responsable de pruebas y documentación |

## 2.3 Plan por fases

Duración total planeada: **15 días hábiles (3 semanas)**.

| Fase | Tareas | Responsable | Duración | Producto esperado |
|---|---|---|---|---|
| 1. Requerimientos | Entrevistar al bibliotecario; revisar ejemplos de registros en papel; redactar RF01-RF09, reglas y requerimientos de calidad; escribir la especificación de casos de uso; aprobación del bibliotecario. | Integrante 1 | Días 1-3 | Documento de requerimientos y reglas (sección 1) firmado. |
| 2. Diseño | Elegir estructuras (lista enlazada, cola con deque, pila con lista, burbuja); diseñar clases y módulos; dibujar los seis diagramas UML y los paquetes; definir el estereotipo «servicioBiblioteca»; revisar diseño contra requerimientos. | Integrante 2 | Días 4-6 | Diagramas UML y tabla de trazabilidad inicial. |
| 3. Implementación | Programar `catalogo.py`, `solicitudes.py`, `prestamos.py`, `ordenamiento.py`, `sistema.py` y `menu.py` según el diseño aprobado. | Integrante 3 | Días 7-11 | Código Python completo. |
| 4. Verificación | Escribir y ejecutar la tabla de pruebas (unitarias, de reglas, de menú y la prueba final integrada); registrar y corregir defectos; volver a probar. | Integrante 4 | Días 12-13 | Tabla de pruebas con resultados. |
| 5. Entrega y mantenimiento | Preparar el manual de usuario; demostrar el sistema al bibliotecario; abrir el registro de cambios para mejoras posteriores. | Integrante 1 con todo el equipo | Días 14-15 | Manual de usuario, registro de cambios y versión 1.0. |

Cada fase termina con una **revisión de fase**: el equipo compara la evidencia con la fase anterior y solo continúa cuando está aprobada.

## 2.4 Cronograma (diagrama de Gantt simplificado)

| Fase | S1 L-M-X | S1 J-V | S2 L-M | S2 X-J-V | S3 L | S3 M | S3 X-J-V |
|---|---|---|---|---|---|---|---|
| Requerimientos | ███ | | | | | | |
| Diseño | | ██ | █ | | | | |
| Implementación | | | █ | ███ | █ | | |
| Verificación | | | | | | ██ | |
| Entrega | | | | | | | ██ |

## 2.5 Ventajas y desventajas en este proyecto

| Ventajas | Desventajas |
|---|---|
| Permite definir desde el inicio qué se entregará (RF01-RF09 están cerrados antes de diseñar). | Un cambio tardío, como impedir eliminar libros con solicitudes pendientes, obliga a modificar requerimientos, diagramas, código y pruebas ya aprobados. |
| Facilita revisar cada etapa con evidencias (documento, diagramas, código, tabla de pruebas). | El bibliotecario no prueba el programa hasta la fase 5, casi al final del calendario. |
| Resulta comprensible cuando las reglas son estables, como en un catálogo escolar sencillo. | Una interpretación equivocada (por ejemplo, creer que la solicitud reserva el libro) puede descubrirse después de programar. |
