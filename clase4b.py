# Una profesora notas en una lista = [5.5, 6.0, 3.8, 4.9, 2.9] utilizando un ciclo for, muestre cada nota en pantalla, aprobado con nota mayor o = a 4, reprobado nota menor a 4. Ademas contar cuantos estudiantes aprobaron y cuantos reprobaron. 

notas = [5.5, 6.0, 3.8, 4.9, 2.9]
aprobados = 0
reprobados = 0

for nota in notas:
    print(f"""----------------------------------------
""")
    if nota >= 4:
        print(f"""----------------------------------------
Nota: {nota} - Aprobado""")
        aprobados += 1
    else:
        print(f"""----------------------------------------
Nota: {nota} - Reprobado""")
        reprobados += 1
print(f"""----------------------------------------
Estudiantes aprobados: {aprobados}""")
print(f"Estudiantes reprobados: {reprobados}")

"""🧩 Ejercicio Práctico: Uso de while
Un sistema debe validar el acceso de un usuario mediante una contraseña.

👉 Desarrolla un programa que:
Solicite al usuario ingresar una contraseña 
Repita la solicitud mientras la contraseña sea incorrecta 
Cuando la contraseña sea correcta, muestre el mensaje:“Acceso permitido” 

🔐 Condición
La contraseña correcta es: "1234"
"""

password = input("Ingrese la contraseña: ")
while password != "1234":
    print("Contraseña incorrecta. Intente de nuevo.")
    password = input("Ingrese la contraseña: ")
print("Acceso permitido")


"""🧩 Ejercicio Práctico Integrador
Se desea desarrollar un pequeño sistema de menú para gestionar una lista de números.
numeros = [2, 5, 8, 10, 3]

👉 Desarrolla un programa que:
Muestre un menú con las siguientes opciones: 
1: Mostrar todos los números 
2: Mostrar solo números pares 
3: Calcular la suma total 
0: Salir 
Utilice un ciclo while para repetir el menú hasta que el usuario elija salir 
Utilice match para manejar las opciones del menú 
Utilice un ciclo for para recorrer la lista en cada opción 
"""
numeros = [2, 5, 8, 10, 3]

while True:
    print("""----------------------------------------
Menú: """)
    print("1: Mostrar todos los números")
    print("2: Mostrar solo números pares")
    print("3: Calcular la suma total")
    print("0: Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("Todos los números:")
            for num in numeros:
                print(num)
        case "2":
            print("Números pares:")
            for num in numeros:
                if num % 2 == 0:
                    print(num)
        case "3":
            suma = sum(numeros)
            print(f"La suma total es: {suma}")
        case "0":
            print("Programa finalizado.")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")

""""Enunciado
Se requiere desarrollar un programa en Python que permita trabajar con una lista de notas.

Lista inicial:
notas = [4.5, 5.2, 3.9, 6.1]

El programa debe mostrar un menú con las siguientes opciones:
1. Mostrar todas las notas
2. Mostrar notas aprobadas (>= 4.0)
3. Calcular el promedio
4. Contar notas reprobadas
0. Salir
Requisitos
- Utilizar un ciclo while para mantener el programa en ejecución
- Utilizar match para manejar las opciones del menú
- Utilizar for para recorrer la lista
- No modificar la lista original
- Validar opciones incorrectas
Desafío Adicional (Décimas)
"""
notas = [4.5, 5.2, 3.9, 6.1]
while True:
    print("""----------------------------------------
Menú: """)
    print("1. Mostrar todas las notas")
    print("2. Mostrar notas aprobadas")
    print("3. Calcular el promedio")
    print("4. Contar notas reprobadas")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("Todas las notas:")
            for nota in notas:
                print(nota)
        case "2":
            print("Notas aprobadas:")
            for nota in notas:
                if nota >= 4.0:
                    print(nota)
        case "3":
            promedio = sum(notas) / len(notas)
            print(f"El promedio es: {promedio:.2f}")
        case "4":
            reprobadas = sum(1 for nota in notas if nota < 4.0)
            print(f"Cantidad de notas reprobadas: {reprobadas}")
        case "0":
            print("Programa finalizado.")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")

#  Mostrar la nota más alta
print(f"La nota más alta es: {max(notas)}")

# Mostrar la cantidad de notas aprobadas
print(f"Cantidad de notas aprobadas: {sum(1 for nota in notas if nota >= 4.0)}")

