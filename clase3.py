num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0:
    print(f"{num1} es un número par.")
else:
    print(f"{num1} es un número impar.")

if num2 % 2 == 0:
    print(f"{num2} es un número par.")
else:
    print(f"{num2} es un número impar.")
    
if num1 < num2:
    print(f"{num1} es menor que {num2}.")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}.")
else:
    print(f"{num1} es igual a {num2}.") 
    
    