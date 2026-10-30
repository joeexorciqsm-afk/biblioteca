# 7. Pruebas con resultados

## 7.1 Cómo ejecutarlas

Desde la carpeta `programa/`:

```
python -m unittest discover -s tests -v
python prueba_integrada.py
```

Resultado obtenido: **28 pruebas automáticas aprobadas** y **15 de 15 verificaciones** cumplidas en la prueba integrada. Las salidas completas están en `evidencias/`.

## 7.2 Tabla de pruebas

| ID | Requerimiento | Caso de prueba | Datos | Resultado esperado | Resultado obtenido |
|---|---|---|---|---|---|
| P01 | Estructuras | Lista vacía | Lista nueva | `buscar` → None, `eliminar` → False, sin errores | Aprobada |
| P02 | Estructuras | Agregar conserva el orden y el nodo guarda un Libro | A, B, C | Recorrido A, B, C; `cabeza.libro` es Libro | Aprobada |
| P03 | RF03 | Eliminar al inicio, en medio y al final | A, B, C, D | Queda solo B; tamaño 1 | Aprobada |
| P04 | RF06 | Cola FIFO y cola vacía | Ana, Luis | Sale Ana y luego Luis; vacía → None | Aprobada |
| P05 | RF08 | Pila LIFO y pila vacía | Ana, Luis | Sale Luis y luego Ana; vacía → None | Aprobada |
| P06 | RF09 | Burbuja ordena una copia | El principito, Don Quijote, Alicia | Alicia, Don Quijote, El principito; original sin cambios | Aprobada |
| P07 | RF09 | Acentos y mayúsculas | zorro, Árbol, casa | Árbol, casa, zorro | Aprobada |
| P08 | RF09 | Casos límite | Lista vacía y un libro | Sin errores | Aprobada |
| P09 | Regla R6 | Burbuja sin `sort()` ni `sorted()` | ordenamiento.py | No aparecen en el código | Aprobada |
| P10 | RF01 | Código repetido | L01 y " l01 " | Rechazados; siguen 3 libros | Aprobada |
| P11 | RF01 | Campos vacíos | Código, título o autor vacíos | Rechazados; catálogo vacío | Aprobada |
| P12 | RF02 | Disponibilidad visible | Prestar L01 | Estado "Prestado" | Aprobada |
| P13 | RF02 | Buscar código inexistente | L99 | Mensaje de no existe | Aprobada |
| P14 | RF03 | Eliminación permitida | L03 disponible | Eliminado | Aprobada |
| P15 | RF03 | Eliminar con solicitudes pendientes | Solicitud de Ana a L01 | Rechazado; L01 sigue | Aprobada |
| P16 | RF03 | Eliminar prestado o inexistente | L01 prestado, L99 | Rechazados | Aprobada |
| P17 | RF04 | Solicitud de código inexistente o sin alumno | L99; alumno vacío | No se encola | Aprobada |
| P18 | Regla R2 | La solicitud no reserva | Solicitud de Ana a L01 | L01 sigue Disponible | Aprobada |
| P19 | RF06 | Atender con cola vacía | Sin solicitudes | Mensaje; pila y catálogo sin cambios | Aprobada |
| P20 | RF06, RF07, R3 | Libro ya prestado | Ana y Luis piden L01 | Luis: "Sin disponibilidad"; cola vacía; 1 préstamo | Aprobada |
| P21 | RF08 | Deshacer con pila vacía | Sin préstamos | Mensaje sin error | Aprobada |
| P22 | Regla R4 | Deshacer no regresa la solicitud | Préstamo de Ana | L01 Disponible; cola vacía | Aprobada |
| P23 | RF09, R5 | Ordenar no altera catálogo ni cola | Solicitudes de Marta y Ana | Orden L03, L02, L01; catálogo y cola iguales | Aprobada |
| P24 | Integrada | Prueba final integrada (sección 7.3) | L01-L03; Ana, Luis, Marta | Todos los pasos cumplen | Aprobada |
| P25 | RC01 | Opciones inválidas | "abc", "0", "10", "" | 4 avisos "Opción no válida" | Aprobada |
| P26 | RC03 | Menú con estructuras vacías | Opciones 2, 5, 6, 7, 8, 3 | Mensajes claros, sin excepciones | Aprobada |
| P27 | Menú | Flujo completo desde el menú | Registrar, solicitar, atender | "Préstamo realizado"; 1 préstamo | Aprobada |
| P28 | RC04 | Fin de entrada (Ctrl+D) | Sin datos | "Hasta luego." sin error | Aprobada |

## 7.3 Prueba final integrada

Datos: L01 "El principito" (Antoine de Saint-Exupéry), L02 "Don Quijote de la Mancha" (Miguel de Cervantes), L03 "Alicia en el país de las maravillas" (Lewis Carroll). Ana pide L01, Luis pide L02 y Marta pide L03.

| Paso | Acción | Resultado obtenido | ¿Cumple? |
|---|---|---|---|
| 1 | Registrar L01, L02 y L03 | Tres libros registrados | Sí |
| 2 | Registrar otro L01 | "Ya existe un libro con el código L01." | Sí |
| 3 | Solicitudes de Ana, Luis y Marta | Cola: #1 Ana, #2 Luis, #3 Marta | Sí |
| 4 | Atender dos veces | Préstamo a Ana (L01) y luego a Luis (L02) | Sí |
| 5 | Revisar la pila | Pila (cima primero): Luis→L02, Ana→L01 | Sí |
| 6 | Deshacer | "Préstamo deshecho: Luis - L02" | Sí |
| 7 | Revisar L02 y la cola | L02 Disponible; cola: #3 Marta | Sí |
| 8 | Ordenar por título | L03 Alicia…, L02 Don Quijote…, L01 El principito | Sí |
| 9 | Revisar cola y catálogo después de ordenar | Cola: #3 Marta; catálogo: L01, L02, L03 | Sí |
| Extra | Cola vacía, pila vacía, código inexistente, eliminar L03 con solicitud de Marta | Mensajes claros; L03 no se elimina | Sí |

**Pasos 10 y 11 (exposición):** el escenario se explica con el diagrama de actividades (pasos 4 y 7), el de secuencia (préstamos de Ana y Luis) y el de clases (pila y cola). El cambio de requerimiento se presenta con la sección 4.

## 7.4 Defectos encontrados y corregidos

| Defecto | Detectado en | Corrección |
|---|---|---|
| "l01" se aceptaba como código distinto de "L01" | Revisión de la iteración 1 | `normalizar_codigo()` (P10) |
| Se podía eliminar un libro con solicitudes pendientes | Revisión de la iteración 1 (CR-01) | `contiene_libro()` en `eliminar_libro()` (P15) |
| "Árbol" se ordenaba después de "zorro" | Revisión de la iteración 3 | `clave_titulo()` sin acentos ni mayúsculas (P07) |
| Ctrl+D mostraba un error de Python | Pruebas de la iteración 3 | `EntradaTerminada` en el menú (P28) |
