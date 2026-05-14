# [# promedio de nota =1 , nota =2, nota =3, nota =4, nota =5 y promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# nota1 = float(input("Ingrese la primera nota: "))
# nota2 = float(input("Ingrese la segunda nota: "))
# nota3 = float(input("Ingrese la tercera nota: "))
# nota4 = float(input("Ingrese la cuarta nota: "))
# nota5 = float(input("Ingrese la quinta nota: "))

# promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
# print(f"El promedio de las notas es: {promedio}")

# # hacerlo con for y una lista
# notas = []
# for i in range(1, 6):
#     nota = float(input(f"Ingrese la nota {i}: "))
#     notas.append(nota)

# promedio = sum(notas) / len(notas)
# print(f"El promedio de las notas es: {promedio}")]

# imprimir notas sobre 4, aprobado, inferior  a 4 reprobado, igual a 4 aprobado, mayor a 4 aprobado

notas = [3.3, 4.0 , 1.5, 6.3]

for nota in notas:
    if nota < 4.0:
        print(f"Nota: {nota} - Reprobado")
    elif nota == 4.0:
        print(f"Nota: {nota} - Aprobado")
    else:
        print(f"Nota: {nota} - Aprobado")
# Agregar contador de aprobados y reprobados
aprobados = 0
reprobados = 0
for nota in notas:
    if nota < 4.0:
        print(f"Nota: {nota} - Reprobado")
        reprobados += 1
    elif nota == 4.0:
        print(f"Nota: {nota} - Aprobado")
        aprobados += 1
    else:
        print(f"Nota: {nota} - Aprobado")
        aprobados += 1

print(f"Total de aprobados: {aprobados}")
print(f"Total de reprobados: {reprobados}")

# Ahora con un ciclo while
notas = [3.3, 4.0 , 1.5, 6.3]
i = 0
aprobados = 0
reprobados = 0

while i < len(notas):
    nota = notas[i]
    if nota < 4.0:
        print(f"Nota: {nota} - Reprobado")
        reprobados += 1
    elif nota == 4.0:
        print(f"Nota: {nota} - Aprobado")
        aprobados += 1
    else:
        print(f"Nota: {nota} - Aprobado")
        aprobados += 1
    i += 1

print(f"Total de aprobados: {aprobados}")
print(f"Total de reprobados: {reprobados}")

# Ahora con while true
notas = [3.3, 4.0 , 1.5, 6.3]
i = 0
aprobados = 0
reprobados = 0
while True:
    if i >= len(notas):
        break
    nota = notas[i]
    if nota < 4.0:
        print(f"Nota: {nota} - Reprobado")
        reprobados += 1
    elif nota == 4.0:
        print(f"Nota: {nota} - Aprobado")
        aprobados += 1
    else:
        print(f"Nota: {nota} - Aprobado")
        aprobados += 1
    i += 1  

print(f"Total de aprobados: {aprobados}")
print(f"Total de reprobados: {reprobados}")


# while True mas match

notas = [3.3, 4.0 , 1.5, 6.3]
i = 0
aprobados = 0
reprobados = 0

while True:
    if i >= len(notas):
        break
    nota = notas[i]
    match nota:
        case n if n < 4.0:
            print(f"Nota: {nota} - Reprobado")
            reprobados += 1
        case 4.0:
            print(f"Nota: {nota} - Aprobado")
            aprobados += 1
        case n if n > 4.0:
            print(f"Nota: {nota} - Aprobado")
            aprobados += 1
    i += 1
print(f"Total de aprobados: {aprobados}")
print(f"Total de reprobados: {reprobados}")


# Recuperaciones Hardware sabado 18 y 25 de abril | Prueba cap 3 y 4 viernes 17 de abril
# Prueba EDA jueves 9 Abril