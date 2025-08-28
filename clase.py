# Ejercicio: Imprimir los números impares del 1 al 99
'''
numero = 1
while numero <= 99:
    print(numero)
    numero += 2
'''
# Ejercicio: Imprimir los números del 100 al 0 de 5 en 5
'''
numero = 100
while numero >= 0:
    print(numero)
    numero -= 5
'''
# Solicitar 2 numeros al usuario e imprimir los pares entre ellos
'''
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 > numero2:

    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1
while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1
'''
# casos

control = True
while control == True:
    num1 = int(input("ingrese el primer numero "))
    num2 = int(input("ingrese el segundo numero "))
    print(" S. Sumar\n R. Restar\n M. Multiplicar\n D. Dividir\n E. Salir")
    opcion = input("Elija una opcion ")
    opcion = opcion.upper()
    match opcion:
        case "S":
            print("Modo seleccionado, suma")
            resultado = num1 + num2
        case "R":
            print("Modo seleccionado, resta")
            resultado = num1 - num2
        case "M":
            print("Modo seleccionado, multiplicacion")
            resultado = num1 * num2
        case "D":
            print("Modo seleccionado, sdv")
            resultado = num1 / num2
        case "E":
            break
        case _:
            print("modo no valido")
    print (f"Resultado = {resultado}")
