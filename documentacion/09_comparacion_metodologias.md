# 9. Comparación final de metodologías

Se construyó un solo programa. El plan en cascada (sección 2) sirvió para planear el proyecto completo y la construcción real se hizo en tres iteraciones (sección 3). Esta comparación resume lo observado.

| Aspecto | Enfoque tradicional (cascada) | Enfoque ágil (adaptación inspirada en Scrum) |
|---|---|---|
| Planeación | Todo el alcance se define al inicio (15 días, 5 fases). | Se planea por iteración a partir de una lista priorizada. |
| Primer contacto del bibliotecario con el programa | Fase 5 (días 14-15). | Fin de la semana 1 (versión 0.1). |
| Cambio CR-01 | Solicitud formal; se revisan requerimientos, diseño, código y pruebas ya aprobados. | Se agrega a la lista de pendientes y se resuelve en la iteración 2. |
| Errores de interpretación | Se descubren tarde (al probar o al entregar). | Se descubrieron en cada revisión: códigos en minúsculas, acentos en el orden. |
| Documentación | Se produce por fases y queda completa antes de programar. | Se actualiza en cada iteración según la definición de terminado. |
| Control y evidencias | Muy claro: cada fase tiene un producto revisado. | Requiere disciplina para mantener código, pruebas y diagramas al día. |
| Participación del usuario | Al inicio (requerimientos) y al final (entrega). | Continua: revisión al final de cada semana. |
| Riesgo principal | Construir algo correcto según el documento pero distinto de lo que el usuario necesitaba. | Que el alcance crezca si no se priorizan los cambios. |

## Conclusiones del equipo

1. Para este proyecto, el enfoque ágil dio mejores resultados: tres de los cuatro defectos de la sección 7.4 los detectó el bibliotecario en las revisiones, antes de la entrega.
2. El plan tradicional fue útil para estimar el trabajo total y asignar responsables; las iteraciones usaron esa misma división de roles.
3. UML funcionó con ambos enfoques: en cascada los diagramas se hacen en la fase de diseño; en el trabajo iterativo se fueron completando (casos de uso y clases en la iteración 1, actividades y secuencia en la 2, componentes, despliegue y paquetes en la 3).
4. Si las reglas fueran estables y el usuario no pudiera participar cada semana, cascada sería una opción razonable para un sistema de este tamaño.
