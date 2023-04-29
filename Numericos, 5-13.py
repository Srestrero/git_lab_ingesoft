def potencia(a, b):
    return a ** b


def divisible(a, b):
    resultado = a % b
    if resultado == 0:
        return True
    else:
        return False


def es_primo(a):
    dividase = 2
    n_dedivisores = 0
    while dividase < a - 1:
        comprobando = a % dividase
        dividase += 1
        if comprobando == 0:
            return False
    if n_dedivisores == 0:
        return True


def Factores_primos(a):
    primos_1 = []
    i = 2
    while i <= a:
        while a % i == 0:
            primos_1.append(i)
            a = a / i
        i += 1
    print(primos_1)
    return primos_1


def Primos_relativos(a, b):
    for x in a:
        for y in b:
            if x == y:
                return False
    return True


def multiplo(a, b, c):
    suma = b + c
    mod = a % suma
    if mod == 0:
        return True
    elif mod != 0:
        return False


def evalua_ecucacion(a, b, c, d):
    e = (a * (d ** 2)) + (b * d) + c
    return e


def coeficiente_lineal_d(a, z):
    c = 2 * a * z
    return c


def Valor_derivada(a, b, z):
    c = (2 * a * z) + b
    return c


def Pertenece_fibonacci(x):
    l = [0, 1]
    while l[-1] < x:
        l.append(l[-1] + l[-2])
    if x == l[-1]:
        return True
    else:
        return False


def main():
    presenta = "{0:c}".format(8275)
    presenta2 = "{0:c} ".format(43007)
    print(presenta2 * 3, presenta * 15, "Numericos", presenta * 15, presenta2 * 3, "\n")
    a = int(input("ingrese el numero del problema que desea realizar , recuerde del 5 al 13 :"))
    while a < 5 or a > 13:
        a = int(input("Recuerde solo es posible un numero del 5 al 13 :"))
    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 5--------------------------------------------------------------
    if a == 5:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 5", presenta * 15, presenta2 * 3, "\n")

        # suponemos la base , un NUMERO ENTERO
        num_1 = int(input("inserte una base :"))
        # suponemos el exponente , un NUMERO NATURAL
        num_2 = int(input("inserte un exponente :"))
        print("la potencia resultante es :", potencia(num_1, num_2))

    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 6--------------------------------------------------------------
    if a == 6:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 6", presenta * 15, presenta2 * 3, "\n")

        # suponemos dos numeros REALES cualesquierase
        num_1 = float(input("inserte un dividendo :"))
        num_2 = float(input("inserte un divisor :"))
        if divisible(num_1, num_2):
            print(num_1, "si es divisible entre ", num_2)
        else:
            print(num_1, "no es divisible entre ", num_2)

    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 7--------------------------------------------------------------
    if a == 7:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 7", presenta * 15, presenta2 * 3, "\n")

        # suponemos un numero NATURAL mayor a 1
        num_1 = int(input("inserte un natural mayor a 1:"))
        if es_primo(num_1):
            print(num_1, "es primo")
        else:
            print(num_1, " no es primo")

    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 8--------------------------------------------------------------
    if a == 8:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 8", presenta * 15, presenta2 * 3, "\n")

        # suponemos dos NUMEROS NATURALES cuals quierase
        num = int(input("inserte un numero natural mayor a 1 :"))
        num2 = int(input("inserte otro numero natural mayor a 1 :"))
        if Primos_relativos(Factores_primos(num), Factores_primos(num2)):
            print(num, "y", num2, "son primos relativos")
        else:
            print(num, "y", num2, "no son primos relativos ya que comparten a lo menos un factor diferente a 1")

    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 9--------------------------------------------------------------
    if a == 9:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 9", presenta * 15, presenta2 * 3, "\n")

        # suponemos tres NUMEROS NATURALES cualquiera
        num = int(input("inserte un numero natural , el cual se desea saber si es multiplo de una suma :"))
        num1 = int(input("inserte otro numero natural el cual sera sumado con el siguiente :"))
        num2 = int(input("inserte otro numero natural :"))
        if multiplo(num, num1, num2):
            print(num, "si es multiplo de ", num1, "+", num2)
        else:
            print(num, "no es multiplo de ", num1, "+", num2)

    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 10--------------------------------------------------------------
    if a == 10:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 10", presenta * 15, presenta2 * 3, "\n")

        num1 = int(input("inserte el coeficiente \"a\" de la ecucacion : "))
        num2 = int(input("inserte el coeficiente \"b\" de la ecucacion : "))
        num3 = int(input("inserte el coeficiente \"c\" de la ecucacion : "))
        num4 = int(input("inserte el valor de la literal \"x\" : "))
        print("el resultado de evaluar una ecucacion de grado 2 ax^2-bx+c con coeficentes a=", num1, "b=", num2, "c=",
              num3, "con parte literal , x=", num4, "es : ", evalua_ecucacion(num1, num2, num3, num4))

    # -----------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 11--------------------------------------------------------------
    if a == 11:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 11", presenta * 15, presenta2 * 3, "\n")

        num1 = int(input("inserte el coeficiente \"a\" de la ecucacion : "))
        num2 = int(input("inserte el coeficiente \"b\" de la ecucacion : "))
        num3 = int(input("inserte el coeficiente \"c\" de la ecucacion : "))
        num4 = int(input("inserte el valor de la literal \"z\" : "))

        print("El coeficiente lineal de la derivada de  una ecucacion de grado 2 ax^2-bx+c con coeficentes a=", num1,
              "b=", num2, "c=", num3, "con parte literal , x=", num4, "es : ", coeficiente_lineal_d(num1, num4))

    # ------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 12--------------------------------------------------------------
    if a == 12:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 12", presenta * 15, presenta2 * 3, "\n")

        num1 = float(input("inserte el coeficiente \"a\" de la ecucacion : "))
        num2 = float(input("inserte el coeficiente \"b\" de la ecucacion : "))
        num3 = float(input("inserte el coeficiente \"c\" de la ecucacion : "))
        num4 = float(input("inserte el valor de la literal \"z\" : "))

        print("El valor de la deriravada de  una ecucacion de grado 2 ax^2-bx+c con coeficentes a=", num1, "b=", num2,
              "c=", num3, "con parte literal , x=", num4, "es : ", Valor_derivada(num1, num2, num4))

    # ------------------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------PROBLEMA 13--------------------------------------------------------------
    if a == 13:
        print("\n", presenta2 * 3, presenta * 15, "PROBLEMA 13", presenta * 15, presenta2 * 3, "\n")

        num = int(input("inserte el numero a verificar : "))
        if num == 0:
            print(num, "pertenece a la serie de fibonacci y es el termino 1")
        elif num == 1:
            print(num, "pertenece a la serie de fibonacci y es el termino 2 o 3")
        else:
            if Pertenece_fibonacci(num):
                print(num, "pertenece a la serie de fibonacci")
            else:
                print(num, "No pertenece a la serie de fibonacci")


main()