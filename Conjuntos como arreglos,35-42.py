def crear_conjuntos_2(a, b, c):
    if a < b:
        c.append(int(input("ingrese el elemento del conjunto : ")))
        return crear_conjuntos_2(a+1, b, c)
    return c


def crear_conjuntos(a):
    lista = []
    return crear_conjuntos_2(0, a, lista)


def pertenece_2(a, b, c):
    if c < len(b) and a != b[c]:
        return pertenece_2(a, b, c+1)
    elif c < len(b) and a == b[c]:
        return True
    return False


def pertenece(a, b):
    return pertenece_2(a, b, 0)


def elimina_repetidos_2(a, b, c):
    if b == len(a):
        return a
    elif c == len(a):
        return elimina_repetidos_2(a, b+1, b+2)
    elif a[b] != a[c]:
        return elimina_repetidos_2(a, b, c+1)
    elif a[b] == a[c]:
        a.pop(c)
        return elimina_repetidos_2(a, b, c)


def elimina_repetidos(a):
    return elimina_repetidos_2(a, 0, 1)


def organiza_2(a, b, c):
    if b < c:
        if a[b] > a[b+1]:
            d = a[b+1]
            a[b+1] = a[b]
            a[b] = d
        a = organiza_2(a, b+1, c)
    if b == c-1:
        a = organiza_2(a, 0, c-1)
    return a


def organiza(a):
    return organiza_2(a, 0, len(a)-1)


def union_2(a, b, c):
    if c < len(b) and (not pertenece(b[c], a)):
        a.append(b[c])
    if c < len(b):
        return union_2(a, b, c+1)
    return a


def union(a, b):
    return organiza(union_2(elimina_repetidos(a), elimina_repetidos(b), 0))


def interseccion_2(a, b, c, d, e):
    if c == len(a):
        return e
    elif d == len(b):
        return interseccion_2(a, b, c+1, 0, e)
    elif a[c] != b[d]:
        return interseccion_2(a, b, c, d+1, e)
    elif a[c] == b[d]:
        e.append(a[c])
        return interseccion_2(a, b, c+1, 0, e)


def interseccion(a, b):
    lista = []
    return organiza(interseccion_2(elimina_repetidos(a), elimina_repetidos(b), 0, 0, lista))


def diferencia_2(a, b, c, d):
    if c < len(a) and (not pertenece(a[c], b)):
        d.append(a[c])
    if c < len(a):
        return diferencia_2(a, b, c+1, d)
    return d


def diferencia(a, b):
    lista = []
    return organiza(diferencia_2(elimina_repetidos(a), elimina_repetidos(b), 0, lista))


def diferencia_simetrica(a, b):
    return union(diferencia(a, b), diferencia(b, a))


def pertence_ambas(a, b, c):
    return pertenece(a, b), pertenece(a, c)


def contenido(a, b):
    c = union(a, b)
    if len(c) == len(elimina_repetidos(b)):
        return True
    return False


def main():
    fin = True
    while fin:
        presenta = "{0:c}".format(8275)
        presenta2 = "{0:c} ".format(43007)
        print(presenta2*3, presenta*15, "Conjuntos como Arreglos",
              presenta*15, presenta2*3, "\n")
        print("ingrese un numero deacuerdo a la opcion que desea realizar con los dos conjuntos")
        print("ingrese [1] , si quiere calcular la union de los conjuntos")
        print(
            "ingrese [2] , si quiere calcular la intersecion entre los conjuntos")
        print(
            "ingrese [3] , si quiere calcular la diferencia de los conjuntos")
        print(
            "ingrese [4] , si quiere calcular la diferencia simetrica de los conjuntos")
        print(
            "ingrese [5] , si quiere calcular si un numero pertenece o no a cada uno de los conjuntos")
        print(
            "ingrese [6] , si quiere calcular si el primer conjunto se encuentra contenido o no en el segundo conjunto")
        print("ingrese [7] , si desea salir del programa")
        opcion = (int(input("inserte la opcion deseada : ")))
        while opcion < 1 or opcion > 7:
            opcion = (
                int(input("Recuerde solo se pueden realizar 7 opciones : ")))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 35------------------------------------------------------------
        if opcion == 1:
            print("\n", presenta2*3, presenta*15,
                  "PROBLEMA 35-Union", presenta*15, presenta2*3, "\n")
            num_1 = int(
                input("inserte la longitud que tendra el primer conjunto:"))
            lista1 = crear_conjuntos(num_1)
            num_2 = int(
                input("inserte la longitud que tendra el segundo conjunto:"))
            lista2 = crear_conjuntos(num_2)
            print("El conjunto resultante de la union de los dos conjuntos dados es :", union(
                lista1, lista2))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 36------------------------------------------------------------
        if opcion == 2:
            print("\n", presenta2*3, presenta*15,
                  "PROBLEMA 36-Interseccion", presenta*15, presenta2*3, "\n")
            num_1 = int(
                input("inserte la longitud que tendra el primer conjunto:"))
            lista1 = crear_conjuntos(num_1)
            num_2 = int(
                input("inserte la longitud que tendra el segundo conjunto:"))
            lista2 = crear_conjuntos(num_2)
            print("El conjunto resultante de la interseccion de los dos conjuntos dados es :",
                  interseccion(lista1, lista2))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 37------------------------------------------------------------
        if opcion == 3:
            print("\n", presenta2*3, presenta*15,
                  "PROBLEMA 37-Diferencia", presenta*15, presenta2*3, "\n")
            num_1 = int(
                input("inserte la longitud que tendra el primer conjunto:"))
            lista1 = crear_conjuntos(num_1)
            num_2 = int(
                input("inserte la longitud que tendra el segundo conjunto:"))
            lista2 = crear_conjuntos(num_2)
            print("El conjunto resultante de la diferencia del primer conjunto respecto al segundo es :",
                  diferencia(lista1, lista2))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 38------------------------------------------------------------
        if opcion == 4:
            print("\n", presenta2*3, presenta*15,
                  "PROBLEMA 38-Diferencia simetrica", presenta*15, presenta2*3, "\n")
            num_1 = int(
                input("inserte la longitud que tendra el primer conjunto:"))
            lista1 = crear_conjuntos(num_1)
            num_2 = int(
                input("inserte la longitud que tendra el segundo conjunto:"))
            lista2 = crear_conjuntos(num_2)
            print("El conjunto resultante de la diferencia simetrica de ambos conjuntos es :",
                  diferencia_simetrica(lista1, lista2))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 39------------------------------------------------------------
        if opcion == 5:
            print("\n", presenta2*3, presenta*15,
                  "PROBLEMA 39-Pertenece", presenta*15, presenta2*3, "\n")
            num_1 = int(
                input("inserte la longitud que tendra el primer conjunto:"))
            lista1 = crear_conjuntos(num_1)
            num_2 = int(
                input("inserte la longitud que tendra el segundo conjunto:"))
            lista2 = crear_conjuntos(num_2)
            num_3 = int(input(
                "inserte el numero el cual desea determinar si pertenece o no a cada uno de los conjuntos :"))
            print("El numero dado ", num_3, "pertenece respectivamente a cada conjunto dado :",
                  pertence_ambas(num_3, lista1, lista2))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 40------------------------------------------------------------
        if opcion == 6:
            print("\n", presenta2*3, presenta*15,
                  "PROBLEMA 40-Contenido", presenta*15, presenta2*3, "\n")
            num_1 = int(
                input("inserte la longitud que tendra el primer conjunto:"))
            lista1 = crear_conjuntos(num_1)
            num_2 = int(
                input("inserte la longitud que tendra el segundo conjunto:"))
            lista2 = crear_conjuntos(num_2)
            print("El primer conjunto esta contenido en el segundo :",
                  contenido(lista1, lista2))
        # -----------------------------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------PROBLEMA 41------------------------------------------------------------
        if opcion == 7:
            print("Gracias por usar el programa")
            fin = False


main()
