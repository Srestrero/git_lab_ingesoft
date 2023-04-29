def podar_hojas(a,b,c):
    return a/(b*c)
def interes_simple(a,b):
    return ((a*b)/100)*7
def interes_compuesto(a,b):
    suma=0
    n=1
    while n<=7:
        suma+=((a*b)/100)
        b+=((a*b)/100)
        n+=1
    return suma
def fichas_a_r(a):
    list=[1,2]
    if 1<=a and a<=2:
        return list[a-1]
    i=3
    while i <= a:
        list.append((list[-1])+(list[-2]))
        i+=1
    return list[-1]
def fichas_a_r_i(a):
    list=[1,2,4]
    if 1<=a and a<=3:
        return list[a-1]
    i=4
    while i <= a:
        list.append(list[-1]+list[-2]+list[-3])
        i+=1
    return list[-1]
def main():
    presenta="{0:c}".format(8275)
    presenta2="{0:c} ".format(43007)
    print(presenta2*3,presenta*15,"Varios",presenta*15,presenta2*3,"\n")
    a=int(input("ingrese el numero del problema que desea realizar , recuerde del 19 al 21 :"))
    while a<19 or a>21:
        a=int(input("Recuerde solo es posible un numero del 19 al 21 :"))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 19------------------------------------------------------------
    if a==19:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 19",presenta*15,presenta2*3,"\n")
        num_1=int(input("inserte la cantidad de hojas que se desean podar:"))
        num_2=int(input("inserte la cantidad de hojas que posee cada rama:"))
        num_3=int(input("inserte la cantidad de ramas que posee cada arbol:"))
        print("Para obtener :",num_1,"hojas es necesario podar :",podar_hojas(num_1,num_2,num_3),"arboles")
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 20------------------------------------------------------------
    if a==20:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 20",presenta*15,presenta2*3,"\n")
        num_1=int(input("inserte el interes del prestamo: "))
        num_2=int(input("inserte la cantidad de dinero prestada: "))
        print("el interes de un prestamo de :",num_2,"pesos con un interes simple de",num_1,"diario , durante 7 dias es:",interes_simple(num_1,num_2))
        print("el interes de un prestamo de :",num_2,"pesos con un interes compuesto de",num_1,"diario , durante 7 dias es:",interes_compuesto(num_1,num_2))

    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 21------------------------------------------------------------
    if a==21:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 20",presenta*15,presenta2*3,"\n")
        num_1=int(input("inserte las dimensiones de la base de la namera 1*n :"))
        print("Existen ",fichas_a_r(num_1),"maneras de llenar una base de 1 *",num_1,"con fichas rojas 1*1 y azules 1*2")
        print("Existen ",fichas_a_r_i(num_1),"maneras de llenar una base de 1 *",num_1,"con fichas rojas 1*1 , azules 1*2 y amarillas 1*3")
main()
    