# si paga con tarjeta 50 % de descuento
# mayor o = 10000 mostrar tiene descuento tiene 25% de descuento
# menor a 10000 mostrar no tiene descuento

tipo_pago = input("Ingrese el tipo de pago (efectivo/tarjeta): ").strip().lower()
precio = float(input("Ingrese el precio del producto: "))

if tipo_pago == "tarjeta":
    descuento = precio * 0.50
    precio_final = precio - descuento
    print(f"Pago con tarjeta. Descuento del 50% aplicado. Precio final: {precio_final:.1f}")
elif tipo_pago == "efectivo":
    if precio >= 10000:
        descuento = precio * 0.25
        precio_final = precio - descuento
        print(f"Pago en efectivo. Descuento del 25% aplicado. Precio final: {precio_final:.1f}")
    else:
        print(f"Pago en efectivo. No tiene descuento. Precio final: {precio:.1f}")