# Guion de la demostración del sistema

Duración sugerida: 10 a 12 minutos. Abrir una terminal en la carpeta `programa/`.

## Parte 1. Programa en vivo (5 min)

Ejecutar `python menu.py` y capturar estos datos:

| Paso | Opción | Datos | Qué decir |
|---|---|---|---|
| 1 | 1 (tres veces) | L01 El principito / Antoine de Saint-Exupéry; L02 Don Quijote de la Mancha / Miguel de Cervantes; L03 Alicia en el país de las maravillas / Lewis Carroll | Cada libro se agrega al final de la lista enlazada (RF01). |
| 2 | 1 | L01 / Repetido / X | Se rechaza el código repetido. |
| 3 | 4 (tres veces) | Ana-L01, Luis-L02, Marta-L03 | Las solicitudes entran a la cola en orden de llegada (RF04). |
| 4 | 5 | — | Se ve el frente de la cola: Ana (RF05). |
| 5 | 3 | L03 | No se puede eliminar: Marta lo solicitó (RF03, cambio CR-01). |
| 6 | 6 (dos veces) | — | Ana sale antes que Luis; cada préstamo se apila (RF06, RF07). |
| 7 | 2 | Enter | L01 y L02 aparecen como Prestado (RF02). |
| 8 | 7 | — | Se desapila el préstamo de Luis; L02 vuelve a Disponible (RF08). |
| 9 | 5 | — | Marta sigue pendiente: deshacer no regresa la solicitud a la cola. |
| 10 | 8 | — | Burbuja muestra Alicia, Don Quijote, El principito sobre una copia (RF09). |
| 11 | 2 y 5 | Enter | El catálogo y la cola no cambiaron por el ordenamiento. |
| 12 | 9 | — | Salir. |

## Parte 2. Prueba automática (1 min)

Ejecutar `python prueba_integrada.py`. Debe terminar con "15 verificaciones cumplidas, 0 fallidas". Opcional: `python -m unittest discover -s tests -v` (28 pruebas OK).

## Parte 3. Explicación con UML (3 min)

| Diagrama | Qué señalar |
|---|---|
| Casos de uso | El bibliotecario es el único actor; el alumno no opera la consola. |
| Clases | La lista contiene nodos y cada nodo guarda un Libro; el sistema usa lista, cola y pila. |
| Actividades | Las dos decisiones: [vacía]/[no vacía] y [disponible]/[prestado]. |
| Secuencia | El préstamo se apila solo en la rama [libro disponible]: esto pasó con Ana y Luis. |
| Componentes y despliegue | Seis archivos .py que corren en Python en la computadora de la biblioteca. |
| Paquetes | Catálogo, Solicitudes, Préstamos e Interfaz; «servicioBiblioteca» en SistemaBiblioteca. |

## Parte 4. Metodologías (2 min)

1. Presentar el cambio CR-01: impedir eliminar libros con solicitudes pendientes (paso 5 de la demostración).
2. Cascada: solicitud formal y revisión del impacto en requerimientos, diseño, código y pruebas ya aprobados.
3. Ágil: se agregó a la lista de pendientes en la revisión de la iteración 1 y se hizo en la iteración 2.
4. Conclusión: con revisiones semanales, el bibliotecario detectó tres defectos antes de la entrega.
