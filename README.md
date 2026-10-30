# Proyecto Biblioteca: Sistema de préstamos

Materia: Estructura de datos · Profesor: Eliseo Izquierdo

Programa de consola en Python que usa una **lista enlazada** (catálogo), una **cola** (solicitudes), una **pila** (historial de préstamos para deshacer) y **ordenamiento burbuja** (catálogo por título), con su documentación de metodologías y seis diagramas UML.

## Contenido

```
Proyecto_Biblioteca/
├── Documento_Completo_Proyecto_Biblioteca.docx   Todo el proyecto en un solo Word
├── Entregables/           Un Word por cada uno de los 9 entregables (sección 14)
│   ├── 01_Programa_de_consola/   Word + carpeta programa/
│   ├── 02_Documento_de_requerimientos_y_reglas.docx
│   ├── 03_Plan_tradicional.docx
│   ├── 04_Registro_de_las_tres_iteraciones.docx
│   ├── 05_Seis_diagramas_UML/    Word + carpeta diagramas/ (.png y .puml)
│   ├── 06_Paquetes_y_ejercicio_de_extensiones.docx
│   ├── 07_Tabla_de_trazabilidad.docx
│   ├── 08_Pruebas_con_resultados.docx
│   └── 09_Comparación_de_metodologías_y_demostración.docx
├── README.md
├── programa/
│   ├── menu.py            Interfaz: menú de consola (ejecutar este)
│   ├── sistema.py         «servicioBiblioteca»: reglas y coordinación
│   ├── catalogo.py        Libro, NodoLibro, ListaLibros (lista enlazada)
│   ├── solicitudes.py     Solicitud, ColaSolicitudes (deque)
│   ├── prestamos.py       Prestamo, PilaPrestamos (lista de Python)
│   ├── ordenamiento.py    Burbuja manual (sin sort ni sorted)
│   ├── prueba_integrada.py  Demostración paso a paso de la sección 12
│   └── tests/test_biblioteca.py  28 pruebas automáticas (unittest)
├── diagramas/             7 diagramas UML: fuente PlantUML (.puml) e imagen (.png)
├── documentacion/         Cada entregable en Markdown
└── evidencias/            Salidas reales de las pruebas y de una sesión de consola
```

## Cómo ejecutar

Requiere Python 3.8 o superior. No usa bibliotecas externas.

```
cd programa
python menu.py                              # programa
python prueba_integrada.py                  # prueba final integrada
python -m unittest discover -s tests -v     # pruebas automáticas
```

## Entregables (sección 14 del proyecto)

| # | Entregable | Dónde está |
|---|---|---|
| 1 | Programa de consola funcional | `programa/` |
| 2 | Documento de requerimientos y reglas | `documentacion/01_requerimientos.md` |
| 3 | Plan tradicional con fases, ventajas y desventajas | `documentacion/02_plan_tradicional.md` |
| 4 | Registro de las tres iteraciones | `documentacion/03_iteraciones_agiles.md` y `04_cambio_requerimiento.md` |
| 5 | Seis diagramas UML | `diagramas/01` a `06` y `documentacion/05_modelado_uml.md` |
| 6 | Paquetes y ejercicio de extensiones | `diagramas/07_paquetes.png` y sección 5.9-5.10 |
| 7 | Tabla de trazabilidad | `documentacion/06_trazabilidad.md` |
| 8 | Pruebas con resultados | `documentacion/07_pruebas.md` y `evidencias/` |
| 9 | Comparación de metodologías y demostración | `documentacion/09_comparacion_metodologias.md`, `prueba_integrada.py` |
| Extra | Complejidad | `documentacion/08_complejidad.md` |
| Extra | Manual de usuario y registro de cambios | `documentacion/10_manual_y_cambios.md` |

Antes de entregar, sustituir "Integrante 1…4" por los nombres reales del equipo (portada del documento y sección 2.2).
