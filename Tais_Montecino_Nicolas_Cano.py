"""Historia de Usuario
Como jugador de un videojuego de rol, quiero una aplicación de consola que me permita gestionar el inventario
de mi personaje, para poder agregar los ítems que encuentro en mis aventuras, ver el listado completo de lo
que cargo, modificar las propiedades de un objeto cuando mejore y eliminar aquello que ya no me sirva o me
ocupe espacio.
Requisitos Técnicos
Programación Orientada a Objetos
• Clase Item: abstraer el ítem del juego con atributos de identificación y categoría, e implementar
__str__.
• Clase Inventario: inicializar internamente la lista de ítems y centralizar las operaciones CRUD.
Control de Flujo e Interfaz
• while: bucle principal infinito para mantener el programa abierto y mostrar el menú continuamente.
• match-case: dirigir el flujo del menú según la opción de texto seleccionada por el usuario.
• if/elif/else: validar datos (lista vacía, índice existente antes de editar/eliminar).
• for: recorrer la lista en la función de lectura, mostrando ítems numerados con su índice.
Operaciones CRUD sobre la Lista
• Crear: capturar datos por teclado, instanciar el objeto e incorporarlo con .append().
• Leer: validar con len() y recorrer con for mostrando índice y objeto.
• Actualizar: solicitar índice, ubicar el objeto por referencia y reasignar sus propiedades.
• Borrar: solicitar índice y remover el objeto con .pop().
Punto Extra (opcional)
• Implementar try-except capturando IndexError o ValueError en lugar de validaciones pasivas con
if/else.
• Implementar el ordenamiento (sort) por nombre y categoría."""