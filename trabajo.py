control = True
while control == True:
    ata = int(input("ingrese el numero ATA"))
    print(" 04. limitaciones de Aeronavegabilidad\n 05. Limite de Mantenimiento\n 06. Dimensiones y Areas \n 07. Izaje y Apuntalamiento\n 08. Nivelacion y Pesaje\n 09. Remolque y carreteo\n 10. Estacionamiento, amarre, almacenamiento, y retorno a servicio\n 11. Rotulos\n 12. Servicing\n 18. Analisis de vibracion\n 21. Air conditioning\n 22. AFCS\n 23. Communications\n")
    opcion = input("Elija una opcion ")
    opcion = opcion.upper()
    match opcion:
        case "04":
            print("Modo seleccionado, limitaciones de Aeronavegabilidad")
            resultado = num1 + num2
        case "05":
            print("Modo seleccionado, Limite de Mantenimiento")
            resultado = num1 - num2
        case "06":
            print("Modo seleccionado, Dimensiones y Areas")
            resultado = num1 * num2
        case "07":
            print("Modo seleccionado, Izaje y Apuntalamiento")
            resultado = num1 / num2
        case "08":
            print("Modo seleccionado, Nivelacion y Pesaje")
            resultado = num1 + num2
        case "09":
            print("Modo seleccionado, Remolque y carreteo")
            resultado = num1 - num2
        case "10":
            print("Modo seleccionado, Estacionamiento, amarre, almacenamiento, y retorno a servicio")
            resultado = num1 * num2
        case "11":
            print("Modo seleccionado, Rotulos")
            resultado = num1 / num2
        case "12":
            print("Modo seleccionado, Servicing")
            resultado = num1 + num2
        case "18":
            print("Modo seleccionado, Analisis de vibracion")
            resultado = num1 - num2
        case "21":
            print("Modo seleccionado, multiplicacion")
            resultado = num1 * num2
        case "22":
            print("Modo seleccionado, suma")
            resultado = num1 + num2
        case "23":
            print("Modo seleccionado, resta")
            resultado = num1 - num2
        case "000":
            break
        case _:
            print("modo no valido")
    print (f"Resultado = {resultado}")
