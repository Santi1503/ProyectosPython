# declaracion de variables
S = "hola cabros"
A = "Como estan?"
D = "Como les va"
O = "Chingate esta"
P = "Messi"

# imprimir variables
print(f"{S} - {A} - {D} - {O} - {P}")
print(S + "-" + A + "-" + D + "-" + O + "-" + P)

# Entrada de datos
nombre = input("Dime tu nombre: ")

print(f"Hola {nombre}")

# condiciones
""""
altura = int(input("Dime tu altura: "))
if altura >= 165:
    print("Eres una persona alta " + nombre)
else:
    print("Eres una persona baja " + nombre)
"""
# Funciones

"""
def mostrarAltura():

    altura = int(input("Dime tu altura: "))
    if altura >= 165:
        print("Eres una persona alta " + nombre)
    else:
        print("Eres una persona baja " + nombre)
# se puede reutilizar el codigo solamente llamandolo basicamente
"""

# listas
personas = ["Santiago", "Francisco", "Martin"]
print(personas[2])

for persona in personas:
    print("+ " + persona)
