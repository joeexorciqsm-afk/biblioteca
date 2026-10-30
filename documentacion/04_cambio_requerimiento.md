# 4. Registro del cambio de requerimiento

## 4.1 Solicitud de cambio CR-01

| Campo | Contenido |
|---|---|
| Identificador | CR-01 |
| Fecha | Revisión de la iteración 1 |
| Solicitante | Bibliotecario |
| Descripción | Impedir la eliminación de libros que tengan solicitudes pendientes. |
| Motivo | Si se elimina un libro con solicitudes en la cola, al atenderlas el sistema buscaría un libro que ya no existe y el alumno perdería su turno sin explicación. |
| Requerimiento afectado | RF03: pasa de "eliminar libros disponibles" a "eliminar únicamente libros disponibles **y sin solicitudes pendientes**". |
| Prioridad | Alta |
| Estado | Implementado y probado en la iteración 2 (versión 0.2) |

## 4.2 Impacto en el producto

| Elemento | Cambio realizado |
|---|---|
| Requerimientos | Se modificó RF03 y su criterio verificable. |
| Diseño (clases) | Se agregó `ColaSolicitudes.contiene_libro(codigo)`. |
| Diseño (secuencia) | Se agregó la nota "Se supone que el libro existe…": el cambio garantiza esa suposición. |
| Código | `SistemaBiblioteca.eliminar_libro()` consulta la cola antes de desenlazar el nodo. |
| Pruebas | Nueva prueba P15 y verificación adicional en `prueba_integrada.py`. |

## 4.3 Cómo se gestionaría con cada enfoque

**Enfoque tradicional (cascada).** El cambio llega cuando los requerimientos ya están aprobados. Se registra una solicitud formal de cambio y se analiza su impacto en cada producto ya entregado: documento de requerimientos, diagramas de clases y secuencia, código y tabla de pruebas. Si se aprueba, se actualizan todos esos documentos en orden, se ajusta el cronograma y se vuelven a revisar las fases afectadas. Si la implementación ya terminó, el costo es mayor porque hay que regresar a fases cerradas.

**Enfoque ágil (adaptación inspirada en Scrum).** El cambio se agrega a la lista priorizada de pendientes. El equipo decide en la siguiente planificación cuándo atenderlo, sin comprometer el objetivo de la iteración en curso. En este proyecto se pidió en la revisión de la iteración 1 y se hizo en la iteración 2, junto con las solicitudes, porque depende de que la cola exista. Los diagramas y pruebas afectados se actualizaron en la misma iteración, según la definición de terminado.
