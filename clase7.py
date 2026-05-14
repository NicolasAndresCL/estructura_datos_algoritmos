"""Guía Práctica: Crear una Calculadora en Python con Funciones
Objetivo
Construir una calculadora por consola en Python utilizando funciones. El programa debe
solicitar dos números, pedir una operación matemática y mostrar el resultado.
Reglas del ejercicio
• Utilizar funciones (def) para cada operación.
• Debe solicitar datos al usuario con input().
• Debe mostrar el resultado final.
Resultado esperado
El usuario ejecuta el programa, ingresa dos números, selecciona una operación y obtiene el
resultado.
Estructura obligatoria del programa
1. Crear funciones matemáticas
Debe crear una función independiente para cada operación:
• Una función para sumar.
• Una función para restar.
• Una función para multiplicar.
• Una función para dividir.
Cada función debe:
• Recibir dos parámetros.
• Retornar el resultado usando return.
2. Crear bloque principal del programa
Fuera de las funciones, desarrollar el flujo principal:
Paso A: Mostrar título
Mostrar en pantalla el nombre del programa.
Ejemplo:
CALCULADORA
Paso B: Solicitar datos
Pedir al usuario:
• Primer número.
• Segundo número.
Convertir ambos valores a número decimal o entero.
Paso C: Mostrar menú de opciones
Mostrar un menú con estas alternativas:
1. Suma
2. Resta
3. Multiplicación
4. División
Paso D: Guardar opción elegida
Solicitar al usuario que escriba una opción.
Paso E: Evaluar opción seleccionada
Usar una estructura condicional:
Puede utilizar:
• if / elif / else
• o match case
Según la opción ingresada:
• Llamar a la función correspondiente.
• Mostrar resultado.
Si escribe una opción incorrecta:
• Mostrar mensaje de error.
Lógica general del ejercicio
1. El usuario ingresa dos números.
2. El usuario elige operación.
3. El sistema identifica la opción.
4. Se llama a una función.
5. La función retorna resultado.
6. El resultado se imprime.
Desafío adicional (opcional)
Si termina antes:
• Permitir repetir operaciones en un ciclo.
• Agregar potencia.
• Agregar raíz cuadrada.
• Mejorar diseño visual con líneas y títulos.
• Validar letras en vez de números."""
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir por cero."

# Solicitar datos al usuario input y mostrar menú de opciones    

print("CALCULADORA")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Ingrese el número de la operación deseada: ")
if opcion == '1':
    resultado = sumar(num1, num2)
    print(f"El resultado de la suma es: {resultado}")
elif opcion == '2':
    resultado = restar(num1, num2)
    print(f"El resultado de la resta es: {resultado}")
elif opcion == '3':
    resultado = multiplicar(num1, num2)
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == '4':
    resultado = dividir(num1, num2)
    print(f"El resultado de la división es: {resultado}")
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    