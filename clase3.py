'''
variable de entrada
Nombre          Tipo
Opcion          str
Temperatura     float

variable de salida
Nombre          Tipo
Conversion      float

Variable de control
opcion
'''
'''
opcion = "Z"
while opcion != "Q":
    opcion = input("F. Farenheit a Celcius\n C. Celcius a farenheit\n Q. Salir\n")
    opcion = opcion.upper()
    if opcion != "Q":
        temperatura = float(input("Ingrese la temperatura a convertir: "))
        match opcion:
            case "F":
                Conversion = (temperatura - 32) *(5/9)
                print(f"{temperatura}°F = {Conversion}°C")
            case "C":
                Conversion = (temperatura *9/5) + 32
                print(f"{temperatura}°C = {Conversion}°F")
            case _:
                print("opcion no valida")
    else:
        print("Saliendo del programa...")
'''

#primos

'''
Variable de entrada
numero      int

Variable de salida
divisores
'''
'''
numero = int(input("Ingrese un numero entero mayor que 1: "))
cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1
if cont == 2:
    print(f"{numero} es primo")
else:
    print(f"Los divisores de {numero} son: ")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
'''






