control = True
while control == True:
    print("ingrese el numero ATA")
    print(" 110. caso1 \n 220. caso2 \n 330. caso3 \n 000. Salir\n")
    opcion = input("Elija una opcion ")
    match opcion:
        case "110":
            print("Modo seleccionado, Piloto Automatico")
            contr = True
            while contr == True:
                print("ingrese la seccion que desea ver")
                print(" 1. que es\n 2. simulacion\n 0. salir\n")
                opcio = input("Elija una opcion ")
                match opcio:
                    case "1":
                        print("Que es")
                        print("holamundo")
                    case "2":
                        print("Simulacion")
                        print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encentra en condiciones seguras o si está entrando en perdida.")

                    case "0":
                        print("Regresando")
                    case _:
                        print("modo no valido")
        case "220":
            print("Modo seleccionado, Piloto Automatico")
            cont = True
            while cont == True:
                ind = int(input("ingrese la seccion que desea ver"))
                print(" 1. que es\n 2. simulacion\n")
                opci = input("Elija una opcion")
                match opci:
                    case "1":
                        print("Que es")
                        print("holamundo")
                    case "2":
                        print("Simulacion")
                    case "0":
                        print("Que es")
                        print("holamundo")
                    case _:
                        print("modo no valido")
        case "330":
            print("Modo seleccionado, Piloto Automatico")
            con = True
            while con == True:
                ind = int(input("ingrese la seccion que desea ver"))
                print(" 1. que es\n 2. simulacion\n")
                opc = input("Elija una opcion")
                match opc:
                    case "1":
                        print("Que es")
                        print("holamundo")
                    case "2":
                        print("Simulacion")
                    case "0":
                        print("Que es")
                        print("holamundo")
                    case _:
                        print("modo no valido")
        case "000":
            break
        case _:
            print("modo no valido")


    '''
    print (f"Resultado = {resultado}")
    '''
