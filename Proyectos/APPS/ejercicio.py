# Suma
"""
valorUno = int(input("Dime un numero: "))
valorDos = int(input("Dime otro numero: "))

resultado = valorUno + valorDos

print("La suma de ", valorUno, " y ", valorDos, " es: ", resultado)
"""

# IVA
"""
print("Estoy fabricado para sacar el IVA de cualquier objeto")

objeto = input("Dime que objeto es: ")
precio = int(input("Dime el precio: "))

precioIva = precio * 0.12
print("El IVA de ", objeto, " es: ", precioIva)

precioSinIva = precio / 1.12
print("El precio sin IVA de ", objeto, " es: ", precioSinIva)
"""

# Mayor menor
"""
print("Voy a ayudarte a ver que numero es mayor/menor que otro :)")
numeroUno = int(input("Dime un numero: "))
numeroDos = int(input("Dime otro numero: "))

if numeroUno > numeroDos:
    print(numeroUno, " es mayor que ", numeroDos)
else:
    print(numeroUno, " es menor que ", numeroDos)
"""
"""
# intervalos de numeros
S = "*"
solicitar = 1
while solicitar > 0:
    numero = int(input("Dime un número entre el 0 y el 100: "))
    if (numero >= 1 and numero < 10):
        print(S, "Tu numero esta en los primeros numeros")
    elif (numero >= 10 and numero < 20):
        print(S, "Tu numero esta en las primeras decenas")
    elif (numero >= 20 and numero < 30):
        print(S, "Tu numero esta en las segundas decenas")
    elif (numero >= 30 and numero < 40):
        print(S, "Tu numero esta en las terceras decenas")
    elif (numero >= 40 and numero < 50):
        print(S, "Tu numero esta en las cuartas decenas")
    elif (numero >= 50 and numero < 60):
        print(S, "Tu numero esta en las quintas decenas")
    elif (numero >= 60 and numero < 70):
        print(S, "Tu numero esta en las sextas decenas")
    elif (numero >= 70 and numero < 80):
        print(S, "Tu numero esta en las septimas decenas")
    elif (numero >= 80 and numero < 90):
        print(S, "Tu numero esta en las octavas decenas")
    elif (numero >= 90 and numero < 100):
        print(S, "Tu numero esta en las novenas decenas")
    elif (numero == 100):
        print(S, "Tu numero es 100")
    else:
        print(S, "Ese numero no te pedi")
    print(" ")
"""
