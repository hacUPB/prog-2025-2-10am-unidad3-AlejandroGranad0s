control = True
while control == True:
    print("ingrese el numero ATA")
    print(" 110. Velocidad de perdida \n 220. caso2 \n 330. caso3 \n 000. Salir\n")
    opcion = input("Elija una opcion ")
    match opcion:
        case "110":
            print("Modo seleccionado, Velocidad de perdida")
            contr = True
            while contr == True:
                print("ingrese la seccion que desea ver")
                print(" 1. que es\n 2. simulacion\n 0. salir\n")
                opcio = input("Elija una opcion ")
                match opcio:
                    case "1":
                        print("Que es")
                        print("fenómeno aerodinámico donde el ala de un avión pierde sustentación porque el ángulo de ataque excede un límite crítico, haciendo que el flujo de aire sobre el ala se vuelva turbulento. Esto resulta en una pérdida de control y una rápida caída de altura. La recuperación implica disminuir el ángulo de ataque y aumentar la velocidad, generalmente bajando el morro del avión y añadiendo potencia. ")
                    case "2":
                        print("Simulacion")
                        print("El programa simulará el vuelo de una aeronave en el cual verificará en cada instante si la aeronave se encentra en condiciones seguras o si está entrando en perdida.")
                        cont = 0
                        while cont < 10 :
                            w = int(input("Ingrese el peso: "))
                            s = int(input("Ingrese la superficie alar: "))
                            c = int(input("ingrese el coeficiente de sustentacion: "))
                            d = int(input("Ingrese la densidad del aire:"))
                            print("calculando procedimiento: ")
                            v_stall = (2*w)/(d*s*c)
                            v_stal = pow(v_stall, 0.5)
                            list[cont] = v_stal
                            cont = cont + 1
                            print("Ingrese 0 si desea salir o ingrese el valor de la velocidad para continuar")
                            v_actual = int(input("Ingrese el valor de la velocidad"))
                            if v_actual == 0 :
                                break
                            if v_actual > v_stal:
                                print("Seguro: el avion esta por encima de la velocidad de perdida")
                            else:
                                print("Precaucion, velocidad de perdida, aumentar velocidad")
                        for indice, valor in enumerate(cont):
                            print(f"Indice: {indice}, Valor: {valor}")
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
