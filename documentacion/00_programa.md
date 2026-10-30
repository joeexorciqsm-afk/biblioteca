# Programa de consola en Python

## Descripción

El programa organiza el catálogo y los préstamos de una biblioteca escolar. El bibliotecario lo opera desde la consola con un menú de nueve opciones. No usa bibliotecas externas: solo la biblioteca estándar de Python (`collections.deque`, `unicodedata`, `typing`).

## Estructuras de datos usadas

| Estructura | Aplicación | Clase | Archivo | Operaciones |
|---|---|---|---|---|
| Lista dinámica enlazada | Catálogo de libros | `ListaLibros`, `NodoLibro`, `Libro` | catalogo.py | `agregar()`, `buscar()`, `eliminar()`, `recorrer()` |
| Cola | Solicitudes pendientes | `ColaSolicitudes`, `Solicitud` | solicitudes.py | `encolar()`, `frente()`, `desencolar()` |
| Pila | Historial de préstamos | `PilaPrestamos`, `Prestamo` | prestamos.py | `apilar()`, `cima()`, `desapilar()` |
| Ordenamiento burbuja | Catálogo por título | función `burbuja_por_titulo()` | ordenamiento.py | Compara títulos vecinos y los intercambia |

## Archivos del programa

| Archivo | Responsabilidad |
|---|---|
| menu.py | Interacción con el usuario (archivo que se ejecuta) |
| sistema.py | Coordinación de reglas y operaciones («servicioBiblioteca») |
| catalogo.py | Lista enlazada y libros |
| solicitudes.py | Cola de solicitudes |
| prestamos.py | Pila de préstamos |
| ordenamiento.py | Algoritmo burbuja |
| prueba_integrada.py | Demostración paso a paso de la prueba final integrada |
| tests/test_biblioteca.py | 28 pruebas automáticas |

## Cómo ejecutarlo

Requiere Python 3.8 o superior. Desde la carpeta `programa/`:

```
python menu.py
python prueba_integrada.py
python -m unittest discover -s tests -v
```

En algunos equipos el comando es `python3` o `py`.

## Ejemplo de uso

```
==============================================
   SISTEMA DE PRÉSTAMOS - BIBLIOTECA ESCOLAR
==============================================
 1. Registrar libro
 2. Consultar catálogo
 3. Eliminar libro
 4. Registrar solicitud de préstamo
 5. Consultar solicitudes pendientes
 6. Atender siguiente solicitud
 7. Deshacer último préstamo
 8. Mostrar libros ordenados por título
 9. Salir
----------------------------------------------
Elija una opción (1-9): 6

[OK] Préstamo realizado: «El principito» (L01) para Ana.
```

La sesión de consola completa está en `evidencias/sesion_consola_ejemplo.txt`.
