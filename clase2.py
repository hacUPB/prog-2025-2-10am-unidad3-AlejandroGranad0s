#fibonacci
'''
numero = int(input("ingrese el numero en terminos de la serie: "))
if numero <=0:
    print("por favor, ingrese un numero entero positivo")
elif numero == 1:
    print("serie de fibonacci")
    print(0)
else:
    a = 0
    b = 1
    contador = 2
    print ("serie de fibonacci")
    print (a)
    print (b)

    while contador < numero:
        siguiente = a + b
        print (siguiente)
        a = b
        b = siguiente
        contador += 1
'''
# tabla de multiplicar
'''
numero = int(input("ingrese el numero entero que desea: "))
if numero <= 0:
    print("el numero debe ser mayor que cero.")
else:
    contador=1
    while contador <= 15:
        print (f"{numero}x{contador}={numero*contador}")
        contador += 1
'''
# bucle for
'''
for cont in range(5, 20, 1):
    print(cont)
'''
# usando f(range)
'''
numero = int(input("ingrese un numero entero positivo: "))
while numero < 1:
      numero = int(input("Ingrese un numero entero positivo: "))
acum = 0
for cont in range(1, numero+1):
        if cont % 2 == 0:
            acum += cont
print(f"la suma de los pares es: {acum}")
'''
# imprimir mensaje
'''
mensaje = "Universidad Pontificia Bolivariana"
numero = int(input("ingrese el numero entero positivo de las veces que desea imprimir: "))
while numero < 0:
    numero = int(input("ingrese un numero entero positivo: "))
for cont in range(0, numero):
    print(f"{mensaje}")
'''
