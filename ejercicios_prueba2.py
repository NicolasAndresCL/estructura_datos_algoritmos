# for i in range(2):
#     for j in range(2):
#         if i == j:
#             continue
# print(f"{i}{j}", end=" ")


# for i in range(2):
#     if i > 5:
#         break
#     else:
#         print("Finalizado")

# datos = [10, 20, 30]

# match datos:
#     case [f, *r]:
#         print(r)


# usuarios = ['Nico', 'Marian']

# for i, nombre in enumerate(usuarios):
#     print(f'{i}: {nombre}')

# for i in range(1, 4):
#     for j in range(1, 3):
#         if i == 2:
#             break
#         print(i, end='')

# def check():
#     print('Evaluado')
#     return True

# if False and check():
#     print('Exito')
# else:
#     print('Fallo')

# energia = 10
# comando = ''
# while energia > 0 and comando != 'salir':
#     comando = input()

# a = 0
# for i in range(5):
#     if i == 3:
#         continue
#     a += 1
#     print(a)

# for i in range(3, 0, -1):
#     print(i, end=' ')
# numero = int(input("Ingrese un número: "))
# match numero:
#     case n if n > 0:
#         print("Es positivo")
#     case n if n < 0:
#         print("Es negativo")
#     case _:
#         print("Es cero")

# a = 0

# while a < 10:
#     a += 2
#     if a == 6:
#         break
# else:
#     print('Fin')

# for i in range(0, 11, 2):
#     print(i)

# def evaluar(x): 
#     return x > 5 or x / 0 == 0 # Si x es mayor que 5, la segunda parte no se evalúa, evitando la división por cero.

# print(evaluar(10))
# data = {'id': 101, 'status': 'active'}
# for k, v in data.items():
#     print(k, v)

# x = [1, 2]
# match x:
#     case [a, b] if a > b:
#         print('A')
#     case [a, b]:
#         print('B')
#     case _:
#         print('C')

# numeros = [5, -2, 10]
# for n in numeros:
#     if n < 0:
#         continue
# print(n)

# x = 0
# for i in range(1, 4): # i toma los valores 1, 2, 3
#     x += i # x se actualiza a 1, luego a 3, y finalmente a 6
#     print(x) # Imprime 1, luego 3, y finalmente 6

# dato = {'tipo': 'admin', 'nivel': 5}
# match dato:
#     case {'tipo': tipo, **resto}: # El patrón coincide con cualquier diccionario que tenga la clave 'tipo', sin importar su valor, y captura el resto de las claves en 'resto'.
#         print('Encontrado')

# lista = [1, 2, 3]
# if len(lista) > 5 and lista[10] == 0:
#     print('A')
# elif len(lista) < 5 or lista[0] == 1:
#     print('B')
# else:
#     print('C')

# config = {'id': 1, 'data': {'meta': 'activo'}}
# match config:
#     case {'data': {'meta': valor}}:
#         print('Configuración encontrada')

# precios = {'pan': 500, 'leche': 1000}
# for p in precios.values():
#     if p > 800:
#         print(p)

# cuenta_atras = 3
# while cuenta_atras  -1:
#     print(cuenta_atras)
# cuenta_atras -= 1

# x = 0

# if x:
#     print("Sí")
# else:
#     print("No")

"""6. Escribe un programa que:
Pida un número
Indique si es positivo, negativo o cero

👉 Usa if / elif / else"""
# numero = int(input("Ingrese un número: "))
# if numero > 0:
#     print("Es positivo")
# elif numero < 0:
#     print("Es negativo")
# else:
#     print("Es cero")

"""7. Escribe un programa que:
Imprima los números del 1 al 5
👉 usando while"""

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
"""8. Escribe un programa que:
Pida un número
Muestre su tabla del 1 al 10

👉 usa for"""

# numero = int(input("Ingrese un número: "))
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

"""9. Login simple

Crea un programa que:

Usuario: "admin"
Contraseña: "1234"
Máximo 3 intentos
Si falla → "Acceso bloqueado"

👉 Usa while"""

# intentos = 0
# while intentos < 3:
#     usuario = input("Usuario: ")
#     contraseña = input("Contraseña: ")
    
#     if usuario == "admin" and contraseña == "1234":
#         print("Acceso concedido")
#         break
#     else:
#         intentos += 1
#         print("Credenciales incorrectas")
# else:
#     print("Acceso bloqueado")

"""10. Menú interactivo

Muestra este menú hasta que el usuario salga:

1. Saludar
2. Mostrar número aleatorio (puede ser fijo)
3. Salir

👉 Usa:

while
match"""
# import random

# while True:
#     print("\nMenú:")
#     print("1. Saludar")
#     print("2. Mostrar número aleatorio")
#     print("3. Salir")
#     print("-------------")
    
#     opcion = input("""
# Seleccione una opción: 
# """).strip()
    
#     match opcion:
#         case "1":
#             print("¡Hola!")
#             print("¿Cómo estás?")
#         case "2":
#             numero_aleatorio = random.randint(1, 100)
#             print(f"Número aleatorio: {numero_aleatorio}")
#             print("¡Suerte!")
#         case "3":
#             print("Saliendo del programa...")
#             print("¡Hasta luego!")
#             break
#         case _:
#             print("Opción no válida, por favor intente de nuevo.")
#             print("Recuerda seleccionar 1, 2 o 3.")

"""11. Número secreto
El programa tiene un número secreto (ej: 7)
El usuario debe adivinar
Indicar:
"Muy bajo"
"Muy alto"
"Correcto"
Termina cuando acierta"""

# numero_secreto = 7
# while True:
#     intento = int(input("Adivina el número secreto: "))
    
#     if intento < numero_secreto:
#         print("Muy bajo")
#     elif intento > numero_secreto:
#         print("Muy alto")
#     else:
#         print("Correcto")
#         break

# items = [1, 2, 3]
# match items:
#     case [a, b]:
#         print('Dos') # Si la lista tiene exactamente dos elementos, se asignan a 'a' y 'b', e imprime 'Dos'.
#     case [a, b, *resto]:
#         print('Varios') # Si la lista tiene al menos dos elementos, se asignan a 'a' y 'b', y el resto de los elementos se asignan a 'resto', e imprime 'Varios'.
#     case _: 
#         print('Otro') # Si la lista no coincide con los casos anteriores, se ejecuta este caso por defecto e imprime 'Otro'.

# x = 5
# while x > -1:
#     print(x)
#     x -= 1

# cuenta = 10
# while cuenta > 0:
#     print(cuenta)
#     cuenta -= 1

# for i in range(1):
#     print('A')
# else:
#     print('B')

# x = 5
# while x > 0:
#     print(x)
#     x -= 1

# energia = 10
# while energia > 0:
#     print('Operando...')
#     energia -= 1

# for i in range(10):
#     print(f'Procesando índice {i}')

# numeros = [1, 7, 10]
# for n in numeros:
#     if n == 7:
#         break
#     print(n)  

# items = ['a', 'b']
# for i, valor in enumerate(items):
#     print(i, valor)

