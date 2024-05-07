def cifrar_cesar(texto, clave, abecedario):
    texto_cifrado = ''
    for caracter in texto:
        if caracter in abecedario:
            indice = (abecedario.index(caracter) + clave) % len(abecedario)
            texto_cifrado += abecedario[indice]
        else:
            texto_cifrado += caracter
    return texto_cifrado

def descifrar_cesar(texto_cifrado, clave, abecedario):
    texto = ''
    for caracter in texto_cifrado:
        if caracter in abecedario:
            indice = (abecedario.index(caracter) - clave) % len(abecedario)
            texto += abecedario[indice]
        else:
            texto += caracter
    return texto

def menu():
    print("+-------------------------------------------------------+")
    print("| Hola, soy Corvex y vamos a usar el algoritmo de Cesar |")
    print("+-------------------------------------------------------+")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    abecedario_espanol = 'abcdefghijklmnopqrstuvwxyzáéíóúüñ'
    abecedario_ascii = ''.join(chr(i) for i in range(32, 127))
    abecedario_alfanumerico_espanol = 'abcdefghijklmnopqrstuvwxyz0123456789áéíóúüñ'
    
    opcion = menu()
    
    if opcion == '1':
        mensaje = input("Ingrese el mensaje a cifrar: ")
        clave = int(input("Ingrese la clave de cifrado: "))
        print("+------------------------+")
        print("| Resultados del cifrado |")
        print("+------------------------+")
        print("| 1. Abecedario Español Normal:", cifrar_cesar(mensaje.lower(), clave, abecedario_espanol))
        print("| 2. Abecedario ASCII:", cifrar_cesar(mensaje, clave, abecedario_ascii))
        print("| 3. Abecedario Alfanumérico Español:", cifrar_cesar(mensaje.lower(), clave, abecedario_alfanumerico_espanol))
    elif opcion == '2':
        mensaje_cifrado = input("Ingrese el mensaje cifrado: ")
        clave = int(input("Ingrese la clave de descifrado: "))
        print("+---------------------------+")
        print("| Resultados del descifrado |")
        print("+---------------------------+")
        print("| 1. Abecedario Español Normal:", descifrar_cesar(mensaje_cifrado.lower(), clave, abecedario_espanol))
        print("| 2. Abecedario ASCII:", descifrar_cesar(mensaje_cifrado, clave, abecedario_ascii))
        print("| 3. Abecedario Alfanumérico Español:", descifrar_cesar(mensaje_cifrado.lower(), clave, abecedario_alfanumerico_espanol))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
