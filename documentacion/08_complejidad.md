# 8. Complejidad de las operaciones

*n* = número de libros en el catálogo; *m* = número de solicitudes en la cola.

| Operación | Código | Complejidad | Explicación |
|---|---|---|---|
| Buscar un libro en la lista enlazada | `ListaLibros.buscar()` | O(n) | Recorre nodo por nodo desde la cabeza hasta encontrar el código. |
| Recorrer el catálogo | `ListaLibros.recorrer()` | O(n) | Visita cada nodo una vez. |
| Agregar un libro | `ListaLibros.agregar()` | O(n) | Recorre hasta el último nodo para conservar el orden de registro. |
| Eliminar un libro | `ListaLibros.eliminar()` | O(n) | Busca el nodo y su anterior para desenlazarlo. |
| Encolar y desencolar con deque | `encolar()`, `desencolar()` | O(1) | `deque.append()` y `deque.popleft()` no desplazan elementos. |
| Consultar el frente | `frente()` | O(1) | Lee el primer elemento. |
| Apilar con append() en una lista de Python | `apilar()` | O(1) amortizado | A veces la lista debe crecer y copiar, pero en promedio es constante. |
| Desapilar al final con pop() | `desapilar()` | O(1) | Quita el último elemento sin desplazar los demás. |
| Burbuja | `burbuja_por_titulo()` | O(n²) en el peor caso | Hasta n-1 pasadas comparando vecinos. Con la salida temprana, una lista ya ordenada cuesta O(n). |

## Operaciones completas del sistema

| Operación | Complejidad | Motivo |
|---|---|---|
| `registrar_libro()` | O(n) | Busca el código repetido y recorre hasta el final para agregar. |
| `eliminar_libro()` | O(n + m) | Busca en la lista y revisa la cola con `contiene_libro()`. |
| `registrar_solicitud()` | O(n) | Busca que el libro exista; encolar es O(1). |
| `atender_siguiente()` | O(n) | Desencolar es O(1), pero buscar el libro es O(n). |
| `deshacer_prestamo()` | O(n) | Desapilar es O(1), pero buscar el libro para liberarlo es O(n). |
| `ordenar_por_titulo()` | O(n²) | Copia O(n) más burbuja O(n²). |

Atender y deshacer **no** son operaciones O(1) completas: aunque la cola y la pila responden en tiempo constante, ambas necesitan buscar el libro en la lista enlazada.
