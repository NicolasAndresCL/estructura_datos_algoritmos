# si paga con tarjeta 50 % de descuento
# mayor o = 10000 mostrar tiene descuento tiene 25% de descuento
# menor a 10000 mostrar no tiene descuento

# tipo_pago = input("Ingrese el tipo de pago (efectivo/tarjeta): ").strip().lower()
# precio = float(input("Ingrese el precio del producto: "))

# if tipo_pago == "tarjeta":
#     descuento = precio * 0.50
#     precio_final = precio - descuento
#     print(f"Pago con tarjeta. Descuento del 50% aplicado. Precio final: {precio_final:.1f}")
# # elif tipo_pago == "efectivo":
# #     if precio >= 10000:
# #         descuento = precio * 0.25
# #         precio_final = precio - descuento
# #         print(f"Pago en efectivo. Descuento del 25% aplicado. Precio final: {precio_final:.1f}")
# #     else:
# #         print(f"Pago en efectivo. No tiene descuento. Precio final: {precio:.1f}")

# # # Realizar el mismo ejercicio pero con un ciclo while para que el usuario pueda ingresar varios productos hasta que decida salir
# # while True:
# #     tipo_pago = input("Ingrese el tipo de pago (efectivo/tarjeta) o 'salir' para terminar: ").strip().lower()
# #     if tipo_pago == "salir":
# #         break
# #     precio = float(input("Ingrese el precio del producto: "))
# #     if tipo_pago == "tarjeta":
# #         descuento = precio * 0.50
# #         precio_final = precio - descuento
# #         print(f"Pago con tarjeta. Descuento del 50% aplicado. Precio final: {precio_final:.1f}")
# #     elif tipo_pago == "efectivo":
# #         if precio >= 10000:
# #             descuento = precio * 0.25
# #             precio_final = precio - descuento
# #             print(f"Pago en efectivo. Descuento del 25% aplicado. Precio final: {precio_final:.1f}")
# #         else:
# #             print(f"Pago en efectivo. No tiene descuento. Precio final: {precio:.1f}")

# # # Realizar el mismo ejercicio pero con un ciclo while + match case para que el usuario pueda ingresar varios productos hasta que decida salir

# # while True:
# #     tipo_pago = input("Ingrese el tipo de pago (efectivo/tarjeta) o 'salir' para terminar: ").strip().lower()
# #     if tipo_pago == "salir":
# #         break
# #     precio = float(input("Ingrese el precio del producto: "))
    
# #     match tipo_pago:
# #         case "tarjeta":
# #             descuento = precio * 0.50
# #             precio_final = precio - descuento
# #             print(f"Pago con tarjeta. Descuento del 50% aplicado. Precio final: {precio_final:.1f}")
# #         case "efectivo":
# #             if precio >= 10000:
# #                 descuento = precio * 0.25
# #                 precio_final = precio - descuento
# #                 print(f"Pago en efectivo. Descuento del 25% aplicado. Precio final: {precio_final:.1f}")
# #             else:
# #                 print(f"Pago en efectivo. No tiene descuento. Precio final: {precio:.1f}")
# #         case _:
# #             print("Tipo de pago no reconocido. Por favor, ingrese 'efectivo' o 'tarjeta'.")

# # Realizar el mismo ejercicio pero con un ciclo for para que el usuario pueda ingresar varios productos hasta que decida salir

# num_productos = int(input("¿Cuántos productos desea ingresar? "))
# for _ in range(num_productos):
#     tipo_pago = input("Ingrese el tipo de pago (efectivo/tarjeta): ").strip().lower()
#     precio = float(input("Ingrese el precio del producto: "))
    
#     if tipo_pago == "tarjeta":
#         descuento = precio * 0.50
#         precio_final = precio - descuento
#         print(f"Pago con tarjeta. Descuento del 50% aplicado. Precio final: {precio_final:.1f}")
#     elif tipo_pago == "efectivo":
#         if precio >= 10000:
#             descuento = precio * 0.25
#             precio_final = precio - descuento
#             print(f"Pago en efectivo. Descuento del 25% aplicado. Precio final: {precio_final:.1f}")
#         else:
#             print(f"Pago en efectivo. No tiene descuento. Precio final: {precio:.1f}")
#     else:
#         print("Tipo de pago no reconocido. Por favor, ingrese 'efectivo' o 'tarjeta'.")

# print("¡Gracias por su compra!")
# print("¡Hasta luego!")

# # Realizar el mismo ejercicio pero con un ciclo for + while + match case para que el usuario pueda ingresar varios productos hasta que decida salir

# num_productos = int(input("¿Cuántos productos desea ingresar? "))
# for _ in range(num_productos):
#     while True:
#         tipo_pago = input("Ingrese el tipo de pago (efectivo/tarjeta): ").strip().lower()
#         if tipo_pago in ["efectivo", "tarjeta"]:
#             break
#         print("Tipo de pago no reconocido. Por favor, ingrese 'efectivo' o 'tarjeta'.")

#     precio = float(input("Ingrese el precio del producto: "))
    
#     match tipo_pago:
#         case "tarjeta":
#             descuento = precio * 0.50
#             precio_final = precio - descuento
#             print(f"Pago con tarjeta. Descuento del 50% aplicado. Precio final: {precio_final:.1f}")
#         case "efectivo":
#             if precio >= 10000:
#                 descuento = precio * 0.25
#                 precio_final = precio - descuento
#                 print(f"Pago en efectivo. Descuento del 25% aplicado. Precio final: {precio_final:.1f}")
#             else:
#                 print(f"Pago en efectivo. No tiene descuento. Precio final: {precio:.1f}")

# i = 0
# while i < 3:
#     print(i)
#     i = i + 1

#     x = 2
# match x:
#     case 1:
#         print("Uno")
#     case 2:
#         print("Dos")

numeros = [2, 6, 8, 3, 10, 1, 7, 4]

contador = 0

suma = 0

for n in numeros:

    suma = suma + n

    if n > 5:

        contador = contador + 1

print("Cantidad mayor que 5:", contador)

promedio = suma / len(numeros)
print("Promedio:", promedio)
if promedio >= 5:
    print("Promedio alto")
else:
    print("Promedio bajo")
i = 0
while i < len(numeros):
    print("Número:", numeros[i])
    if numeros[i] > promedio:
        print("Sobre el promedio")
    else:
        print("Bajo el promedio")
    i = i + 1
print("Recorrido finalizado")   