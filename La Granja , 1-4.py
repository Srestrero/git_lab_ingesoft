def total_leche(a,b,c):
    area_total=a*b
    producion=area_total*c*2
    return producion
def total_huevos(a):
    Totalgallinas=(a//3)
    unocadatres=(Totalgallinas//2)*10
    unocadacinco=(Totalgallinas//2)*6
    Totalhuevos=unocadacinco+unocadatres
    return Totalhuevos
def escorpiones(a,b,c):
    se_puede_vender=((a+b+c)//3)
    peso_vendido=0
    if se_puede_vender<=c:
        peso_vendido=(se_puede_vender*50)
    elif se_puede_vender>c :
        faltan=(se_puede_vender-c)
        if faltan<=b :
            peso_vendido=(c*50) + (faltan*30)  
        elif faltan >b:
            faltan-=b
            peso_vendido=(c*50) + (b*30)+(faltan*20)
    return peso_vendido
def corral(a,b,c,d,e):
    h_madera=4
    h_varilla=8
    h_alambre=5
    h_lata=1
    pre_ma=h_madera*a*e
    pre_va=h_varilla*b*e
    pre_al=h_alambre*c*e
    pre_la=h_lata*d*e
    if pre_ma<pre_al and pre_ma<pre_va and pre_ma<pre_la:
        mas_barato="madera"
    elif pre_va<pre_ma and pre_va<pre_al and pre_va<pre_la:
        mas_barato="varilla"
    elif pre_al<pre_va and pre_al<pre_ma and pre_al<pre_la:
        mas_barato="alambre"
    elif pre_la<pre_va and pre_la<pre_ma and pre_la<pre_al:
        mas_barato="lata"
    return mas_barato
def main():
    presenta="{0:c}".format(8275)
    presenta2="{0:c} ".format(43007)
    print(presenta2*3,presenta*15," LA GRANJA",presenta*15,presenta2*3,"\n")
    a=int(input("ingrese el numero del problema que desea realizar , recuerde del 1 al 4 :"))
    while a<1 or a>4:
        a=int(input("Recuerde solo es posible un numero del 1 al 4 :"))
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 1--------------------------------------------------------------
    if a==1:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 1",presenta*15,presenta2*3,"\n")
        
        #Suponemos un numero cualquiera  NATURAL de vacas y las dimensiones del pasto.
        largo=int(input("Introduzca un valor para el largo del pasto:"))
        ancho=int(input("Introduzca un valor para el ancho del pasto:"))
        numero_de_vacas=int(input("Introduzca un numero de vacas :"))
        
        print("El total producido de leche es :",total_leche(largo,ancho,numero_de_vacas))  

    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 2--------------------------------------------------------------
    if a==2 :
        print("\n",presenta2*3,presenta*15,"PROBLEMA 2",presenta*15,presenta2*3,"\n")
        
        #Suponemos un numero total NATURAL de aves.
        totalaves=int(input("introduzca un numero de aves :"))
        print("A final de mes tendremos :" ,total_huevos(totalaves), "huevos" )
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 3--------------------------------------------------------------
    if a==3:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 3",presenta*15,presenta2*3,"\n")
        
        #Suponemos un numero narural para cada tipo de escorpiones 
        escorpiones_livianos=int(input("Introduzca un numero de escorpiones ligeros :"))
        escorpiones_medianos=int(input("Introduzca un numero de escorpiones medianos :"))
        escorpiones_pesados=int(input("Introduzca un numero de escorpiones pesados :"))
        
        print("se vendieron escorpiones de tal manera que la poblacion no decresca de 2/3 para un peso total de ",escorpiones(escorpiones_livianos,escorpiones_medianos,escorpiones_pesados), "gramos")

    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 4--------------------------------------------------------------
    if a==4:   
        print("\n",presenta2*3,presenta*15,"PROBLEMA 4",presenta*15,presenta2*3,"\n")
        
        #Suponemos un numero NATURAL de metros del granero los cuales se vana arreglar   
        m_granero=int(input("introduzca un numero natural de metros :"))
        #Suponemos el precio (Numero Natural )por hilera de cada material
        pre_ma=int(input("introduzca un precio para la hilera de madera :"))
        pre_va=int(input("introduzca un precio para la hilera de valirra :"))
        pre_al=int(input("introduzca un precio para la hilera de alambre :"))
        pre_la=int(input("introduzca un precio para la hilera de lata :"))
        print("el material mas barato para arreglar el corral es :",corral(pre_ma,pre_va,pre_al,pre_la,m_granero))
main()
