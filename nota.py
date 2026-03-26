notas = float(input("Ingrese una nota entre el 1 y el 7: "))

if 1 <= notas <= 7:
    if notas >= 6: 
        print("Aprobado")
    elif notas >= 4: 
        print("Suficiente")
    else:
        print("Reprobado")
else:
    print("Error: La nota debe estar entre 1 y 7")
    
