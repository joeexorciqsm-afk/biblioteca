# 10. Manual de usuario y registro de cambios

## 10.1 Requisitos

- Python 3.8 o superior (no requiere instalar bibliotecas externas).
- Una terminal: Símbolo del sistema o PowerShell en Windows, Terminal en macOS o Linux.

## 10.2 Cómo iniciar

```
cd programa
python menu.py
```

En algunos equipos el comando es `python3 menu.py` o `py menu.py`.

## 10.3 Menú

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
```

| Opción | Qué hace | Datos que pide |
|---|---|---|
| 1 | Agrega un libro como Disponible. | Código, título y autor (obligatorios). |
| 2 | Muestra todo el catálogo o busca un código. | Un código, o Enter para ver todo. |
| 3 | Elimina un libro si está disponible y nadie lo ha solicitado. | Código. |
| 4 | Pone una solicitud al final de la cola. El libro debe existir. | Nombre del alumno y código. |
| 5 | Lista las solicitudes del frente al final. | Nada. |
| 6 | Atiende la solicitud del frente: presta el libro si está disponible. | Nada. |
| 7 | Deshace el último préstamo y libera el libro. | Nada. |
| 8 | Muestra una copia del catálogo en orden alfabético. | Nada. |
| 9 | Cierra el programa. | Nada. |

Los mensajes que empiezan con `[OK]` indican que la operación se realizó; los que empiezan con `[!]` explican por qué no se realizó.

## 10.4 Preguntas frecuentes

- **¿Registrar una solicitud aparta el libro?** No. La disponibilidad se revisa al atenderla.
- **¿Qué pasa si atiendo una solicitud de un libro prestado?** La solicitud se retira de la cola y se informa "Sin disponibilidad". No se crea un préstamo.
- **Si deshago un préstamo, ¿el alumno vuelve a la cola?** No. Si todavía quiere el libro, se registra una solicitud nueva.
- **¿Se guardan los datos al cerrar?** No. Esta versión trabaja en memoria.

## 10.5 Registro de cambios

| Versión | Iteración | Cambios |
|---|---|---|
| 0.1 | 1 | Catálogo con lista enlazada: registrar, consultar y eliminar libros. Menú con validación de opciones. |
| 0.2 | 2 | Códigos sin distinguir mayúsculas. Búsqueda por código. Cola de solicitudes y atención en orden de llegada. Pila de préstamos. CR-01: no se eliminan libros con solicitudes pendientes. |
| 1.0 | 3 | Deshacer último préstamo. Catálogo ordenado con burbuja (ignora acentos). Salida limpia con Ctrl+C / Ctrl+D. 28 pruebas automáticas y prueba integrada. |

## 10.6 Mejoras posteriores propuestas (fuera del alcance de esta versión)

| Mejora | Impacto |
|---|---|
| Guardar y cargar los datos en `biblioteca.json` | Nuevo artefacto en el diagrama de despliegue y nuevo componente de persistencia. |
| Registrar devoluciones | Nuevo caso de uso; el libro vuelve a Disponible sin usar la pila de deshacer. |
| Permitir que los alumnos usen la consola | Nuevo actor Alumno con permisos limitados (solo solicitar y consultar). |
