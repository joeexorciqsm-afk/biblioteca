"""Demostración de la prueba final integrada (sección 12 del proyecto).

Ejecutar con:  python prueba_integrada.py
Muestra cada paso, el estado de las estructuras y si se cumplió lo esperado.
"""

from sistema import SistemaBiblioteca

aprobados = 0
fallidos = 0


def verificar(descripcion, condicion):
    global aprobados, fallidos
    if condicion:
        aprobados += 1
        print(f"   [CUMPLE] {descripcion}")
    else:
        fallidos += 1
        print(f"   [FALLA]  {descripcion}")


def estado(s):
    cat = ", ".join(f"{l.codigo}:{l.estado()}" for l in s.obtener_catalogo()) or "(vacío)"
    cola = ", ".join(f"#{x.numero} {x.alumno}->{x.codigo_libro}" for x in s.obtener_solicitudes_pendientes()) or "(vacía)"
    pila = ", ".join(f"{p.alumno}->{p.codigo_libro}" for p in s.obtener_historial_prestamos()) or "(vacía)"
    print(f"   Catálogo: {cat}")
    print(f"   Cola (frente primero): {cola}")
    print(f"   Pila (cima primero): {pila}")


s = SistemaBiblioteca()

print("PASO 1. Registrar L01, L02 y L03")
for datos in [("L01", "El principito", "Antoine de Saint-Exupéry"),
              ("L02", "Don Quijote de la Mancha", "Miguel de Cervantes"),
              ("L03", "Alicia en el país de las maravillas", "Lewis Carroll")]:
    print("  ", s.registrar_libro(*datos).mensaje)
verificar("Hay 3 libros en el catálogo", len(s.obtener_catalogo()) == 3)

print("\nPASO 2. Intentar registrar otro libro con código L01")
r = s.registrar_libro("L01", "Libro duplicado", "Autor X")
print("  ", r.mensaje)
verificar("Se rechaza el código repetido", not r.exito and len(s.obtener_catalogo()) == 3)

print("\nPASO 3. Registrar solicitudes de Ana, Luis y Marta, en ese orden")
for alumno, codigo in [("Ana", "L01"), ("Luis", "L02"), ("Marta", "L03")]:
    print("  ", s.registrar_solicitud(alumno, codigo).mensaje)
estado(s)
verificar("La cola tiene Ana, Luis, Marta",
          [x.alumno for x in s.obtener_solicitudes_pendientes()] == ["Ana", "Luis", "Marta"])

print("\nPASO 4. Atender a Ana y después a Luis")
r1 = s.atender_siguiente()
print("  ", r1.mensaje)
r2 = s.atender_siguiente()
print("  ", r2.mensaje)
verificar("Ana sale antes que Luis", "Ana" in r1.mensaje and "Luis" in r2.mensaje)

print("\nPASO 5. Verificar que ambos préstamos estén en la pila")
estado(s)
verificar("La pila contiene Luis (cima) y Ana",
          [p.alumno for p in s.obtener_historial_prestamos()] == ["Luis", "Ana"])

print("\nPASO 6. Deshacer el préstamo de Luis")
r = s.deshacer_prestamo()
print("  ", r.mensaje)
verificar("Se deshizo el préstamo de Luis", r.exito and r.dato.alumno == "Luis")

print("\nPASO 7. Comprobar que L02 vuelve a estar disponible y Marta sigue pendiente")
estado(s)
verificar("L02 está disponible", s.buscar_libro("L02").dato.disponible)
verificar("Marta sigue pendiente", [x.alumno for x in s.obtener_solicitudes_pendientes()] == ["Marta"])

print("\nPASO 8. Mostrar el catálogo ordenado por título (burbuja)")
cola_antes = [x.numero for x in s.obtener_solicitudes_pendientes()]
catalogo_antes = [l.codigo for l in s.obtener_catalogo()]
ordenados = s.ordenar_por_titulo()
for libro in ordenados:
    print(f"   {libro.codigo}  {libro.titulo}  ({libro.estado()})")
verificar("Orden: Alicia, Don Quijote, El principito",
          [l.codigo for l in ordenados] == ["L03", "L02", "L01"])

print("\nPASO 9. Demostrar que el ordenamiento no altera la cola ni el catálogo")
estado(s)
verificar("La cola no cambió", [x.numero for x in s.obtener_solicitudes_pendientes()] == cola_antes)
verificar("El catálogo conserva el orden de registro", [l.codigo for l in s.obtener_catalogo()] == catalogo_antes)

print("\nPRUEBAS ADICIONALES")
vacio = SistemaBiblioteca()
print("   Cola vacía:", vacio.atender_siguiente().mensaje)
verificar("Cola vacía no provoca error", not vacio.atender_siguiente().exito)
print("   Pila vacía:", vacio.deshacer_prestamo().mensaje)
verificar("Pila vacía no provoca error", not vacio.deshacer_prestamo().exito)
r = s.registrar_solicitud("Pedro", "L99")
print("   Código inexistente:", r.mensaje)
verificar("Se rechaza la solicitud de un código inexistente", not r.exito)
r = s.eliminar_libro("L03")
print("   Eliminar L03 (Marta lo solicitó):", r.mensaje)
verificar("No se elimina un libro con solicitudes pendientes", not r.exito)

print(f"\nRESULTADO: {aprobados} verificaciones cumplidas, {fallidos} fallidas.")
