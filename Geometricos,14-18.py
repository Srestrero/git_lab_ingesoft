def paralelas(a,b,c,d):
    return (a==b) and (c!=d)
def perpendiculares(a,b):
    return (a*b==-1)
def cumple_ninguna(a,b,c,d):
    return not(paralelas(a,b,c,d) or perpendiculares(a,b))
def intercepto_eje_x(a,b):
    return (-b)/a
def area_triangulo_inscrito(a):
    return ((a/tan(pi/6)*2)*((a/tan(pi/6)*2)*sin(pi/3)))/2
def area_cuadrado_circunscrito(a):
    return 4*(a**2)
def perimetro_cuadrado_circunscrito(a):
    return 8*a
def area_cuadrado_inscrito(a):
    return 2*(a**2)
def perimetro_cuadrado_inscrito(a):
    return 4*a*sqrt(2)
def area_pentagono_circunscrito(a):
    return 5*(a**2)*tan(36)
def perimetro_pentagono_circunscrito(a):
    return 10*a*tan(36)
def area_pentagono_inscrito(a):
    return (5/2)*(a**2)*sin(72)
def perimetro_pentagono_inscrito(a):
    return 5*(a/2)*sqrt(10-(2*sqrt(5)))
def area_hexagono_circunscrito(a):
    return 2*sqrt(30)*(a**2)
def perimetro_hexagono_circunscrito(a):
    return 6*((2*a*sqrt(3))/3)
def area_hexagono_inscrito(a):
    return (3*(a**2)*sqrt(3))/3
def perimetro_hexagono_inscrito(a):
    return 6*a

def total_telaraña(a):
    c=6*a
    i=1
    while i<=a:
        c+=6*i
        i+=1
    return c
def main():

    presenta="{0:c}".format(8275)
    presenta2="{0:c} ".format(43007)

    print(presenta2*3,presenta*15,"Numericos",presenta*15,presenta2*3,"\n")

    a=int(input("ingrese el numero del problema que desea realizar , recuerde del 14 al 18 :"))

    while a<14 or a>18:
        a=int(input("Recuerde solo es posible un numero del 14 al 18 :"))

    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 14-------------------------------------------------------------
    if a==14:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 14",presenta*15,presenta2*3,"\n")
        
        num_1=float(input("inserte la pendiente 1  :"))
        num_2=float(input("inserte la pendiente 2  :"))
        num_3=float(input("inserte la intercesion 1 al eje y :"))
        num_4=float(input("inserte la intercesion 2 al eje y :"))

        print("la recta es pararalela :",paralelas(num_1,num_2,num_3,num_4))
        print("la recta es perpendicular :",perpendiculares(num_1,num_2))
        print("No cumple ninguna de las anteriores :",cumple_ninguna(num_1,num_2,num_3,num_4))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 15------------------------------------------------------------
    if a==15:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 15",presenta*15,presenta2*3,"\n")

        num_1=float(input("inserte la pendiente 1  :"))
        num_2=float(input("inserte la pendiente 2  :"))
        num_3=float(input("inserte la intercesion 1 al eje y :"))
        num_4=float(input("inserte la intercesion 2 al eje y :"))

        print("la primera recta intercepta al eje en x=",intercepto_eje_x(num_1,num_3))
        print("la segunda recta intercepta al eje en x=",intercepto_eje_x(num_2,num_4))
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 16------------------------------------------------------------
    if a==16:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 16",presenta*15,presenta2*3,"\n")

        num_1=float(input("inserte el radio del circulo :"))

        print("El area del triangulo circunscrito al circulo de radio :",num_1,"es :",area_triangulo_inscrito(num_1))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 17------------------------------------------------------------
    if a==17:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 16",presenta*15,presenta2*3,"\n")

        num_1=float(input("inserte el radio del circulo :"))

        print("El area del cuadrado circunscrito al circulo de radio :",num_1,"es :",area_cuadrado_circunscrito(num_1))
        print("El perimetro del cuadrado circunscrito al circulo de radio :",num_1,"es :",perimetro_cuadrado_circunscrito(num_1))
        print("El area del cuadrado inscrito al circulo de radio :",num_1,"es :",area_cuadrado_inscrito(num_1))
        print("El perimetro del cuadrado inscrito al circulo de radio :",num_1,"es :",perimetro_cuadrado_inscrito(num_1))
        print("El area del pentagono circunscrito al circulo de radio :",num_1,"es :",area_pentagono_circunscrito(num_1))
        print("El perimetro del pentagono circunscrito al circulo de radio :",num_1,"es :",perimetro_pentagono_circunscrito(num_1))
        print("El area del pentagono inscrito al circulo de radio :",num_1,"es :",area_pentagono_inscrito(num_1))
        print("El perimetro del pentagono inscrito al circulo de radio :",num_1,"es :",perimetro_pentagono_inscrito(num_1))
        print("El area del hexagono circunscrito al circulo de radio :",num_1,"es :",area_hexagono_circunscrito(num_1))
        print("El perimetro del hexagono circunscrito al circulo de radio :",num_1,"es :",perimetro_hexagono_circunscrito(num_1))
        print("El area del hexagono inscrito al circulo de radio :",num_1,"es :",area_hexagono_inscrito(num_1))
        print("El perimetro del hexagono inscrito al circulo de radio :",num_1,"es :",perimetro_hexagono_inscrito(num_1))
    #-----------------------------------------------------PROBLEMA 18-------------------------------------------------------------
    if a==18:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 14",presenta*15,presenta2*3,"\n")
        
        num_1=int(input("inserte el radio el cual se va a llenar de telaraña :"))
        print("la telaraña total usada para cubrir con un patron hexagonal , un area de radio :",num_1,"es :",total_telaraña(num_1))
from math import *
main() 
#git no me dejaba subirlo