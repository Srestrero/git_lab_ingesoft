def lectura_inicial_2(a,b,c,d):
    if b==len(a):
        return d
    elif b<len(a):
        if (a[b]=="+"or a[b]=="-")and(c!=""):
            d.append(c)
            c=""
            c+=a[b]
            return lectura_inicial_2(a,b+1,c,d)
        if (b+1)==len(a):
            c+=a[b]
            d.append(c)
            return lectura_inicial_2(a,b+1,c,d)
        else :
            c+=a[b]
            return lectura_inicial_2(a,b+1,c,d) 
def lectura_inicial(a):
    lista=[]
    c=""
    return lectura_inicial_2(a,0,c,lista)   
def lectura_coeficiente_2(a,b,c,d,e):
    if b==len(a):
        return e
    elif b<len(a):
        if c==len(a[b]) and a[b][c-1]=="x":
            e.append(1)
            d=""
            return lectura_coeficiente_2(a,b+1,0,d,e)
        elif c==(len(a[b])) and a[b][c-1]!="x":
            e.append(int(d))
            e.append(0)
            return lectura_coeficiente_2(a,b+1,0,d,e)
        elif c==len(a[b]):
            d=""
            return lectura_coeficiente_2(a,b+1,0,d,e)
        elif c<len(a[b]) and a[b][c]=="^":
            d=a[b][c+1]
            e.append(int(d))
            d=""
            return lectura_coeficiente_2(a,b+1,0,d,e)
        elif c<len(a[b]) and (a[b][c]!="x" and a[b][c]!="^" ) :
            d+=a[b][c]
            return lectura_coeficiente_2(a,b,c+1,d,e)
        elif c<len(a[b]) and (a[b][c]=="x" or (a[b][c]=="^")):
            if (d=="")or (d=="+"):
                e.append(1)
            elif d=="-":
                e.append(-1)
            else:
                e.append(int(d))
            d=""
            return lectura_coeficiente_2(a,b,c+1,d,e)
def lectura_coeficiente(a):
    lista=[]
    d=""
    return lectura_coeficiente_2(a,0,0,d,lista)
def lectura_final_2(a,b,c,d):
    if b==len(a):
        return d
    elif b%2!=1:
        c.append(a[b])
        return lectura_final_2(a,b+1,c,d)
    else:
        c.append(a[b])
        d.append(c)
        c=[]
        return lectura_final_2(a,b+1,c,d)
def lectura_final(a):
    lista1=[]
    lista2=[]
    return lectura_final_2(lectura_coeficiente(lectura_inicial(a)),0,lista2,lista1)
def evaluar_2(a,b,c,d):
    if b==len(a):
        return d
    elif b<len(a):
        d=(a[b][0]*(c**a[b][1]))+evaluar_2(a,b+1,c,d)
        return d
def evaluar(a,b):
    return int(evaluar_2(a,0,b,0))      
def sumar_2(a,b,c,d,e):
    if (c==len(a)) and (d==len(b)):
        return e
    elif (c==len(a)):
        e.append(b[d])
        return sumar_2(a,b,c,d+1,e)
    elif (d==len(b)):
        e.append(a[c])
        return sumar_2(a,b,c+1,d,e)
    elif (a[c][1]>b[d][1]) :
        e.append(a[c])
        return sumar_2(a,b,c+1,d,e)
    elif (a[c][1]<b[d][1]) :
        e.append(b[d])
        return sumar_2(a,b,c,d+1,e)
    elif (a[c][1]==b[d][1]) :
        sum=a[c][0]+b[d][0]
        lista=[sum,a[c][1]]
        e.append(lista)
        return sumar_2(a,b,c+1,d+1,e)   
def sumar(a,b):
    lista=[]
    return sumar_2(a,b,0,0,lista)
def resta_2(a,b,c,d,e):
    if (c==len(a)) and (d==len(b)):
        return e
    elif (c==len(a)):
        e.append(b[d])
        return resta_2(a,b,c,d+1,e)
    elif (d==len(b)):
        e.append(a[c])
        return resta_2(a,b,c+1,d,e)
    elif (a[c][1]>b[d][1]) :
        e.append(a[c])
        return resta_2(a,b,c+1,d,e)
    elif (a[c][1]<b[d][1]) :
        e.append(b[d])
        return resta_2(a,b,c,d+1,e)
    elif (a[c][1]==b[d][1]) :
        res=a[c][0]-b[d][0]
        lista=[res,a[c][1]]
        e.append(lista)
        return resta_2(a,b,c+1,d+1,e)   
def resta(a,b):
    lista=[]
    return resta_2(a,b,0,0,lista)    
def multiplica_2(a,b,c,d,e,f):
    if c==len(a):
        return e
    elif c<len(a):
        if d==len(b):
            e=sumar(e,f)
            f=[]
            return multiplica_2(a,b,c+1,0,e,f)
        elif d<len(b):
            mul1=a[c][0]*b[d][0]
            mul2=a[c][1]+b[d][1]
            f.append([mul1,mul2])
            return multiplica_2(a,b,c,d+1,e,f)
def multiplica(a,b):
    lista1=[]
    lista2=[]
    return multiplica_2(a,b,0,0,lista1,lista2)
def divide_2(a,b,c,d):
    if c==len(a) or a[c][1]<b[0][1]:
        return d
    elif c<len(a):
        div1=a[c][0]//b[0][0]
        div2=a[c][1]-b[0][1]
        lista=[]
        lista.append([div1,div2])
        d.append([div1,div2])
        a=resta(a,multiplica(lista,b))
        return divide_2(a,b,c+1,d)
def divide(a,b):
    lista=[]
    return divide_2(a,b,0,lista)
def residuo_2(a,b,c,d):
    if c==len(a) or a[c][1]<b[0][1]:
        return a
    elif c<len(a):
        div1=a[c][0]//b[0][0]
        div2=a[c][1]-b[0][1]
        lista=[]
        lista.append([div1,div2])
        d.append([div1,div2])
        a=resta(a,multiplica(lista,b))
        return residuo_2(a,b,c+1,d)
def residuo(a,b):
    lista=[]
    return residuo_2(a,b,0,lista)
def main():
    fin=True
    while fin:
        presenta="{0:c}".format(8275)
        presenta2="{0:c} ".format(43007)
        print(presenta2*3,presenta*15,"Polinomios como arreglos",presenta*15,presenta2*3,"\n")
        print("ingrese un numero deacuerdo a la opcion que desea realizar con los dos conjuntos")
        print("ingrese [1] , si quiere evaluar los polinomios dado un x o una literal")
        print("ingrese [2] , si quiere sumar los polinomios")
        print("ingrese [3] , si quiere restar los polinomios ´el primero menos el segundo´")
        print("ingrese [4] , si quiere multiplicar los polinomios")
        print("ingrese [5] , si quiere dividir los polinimos ´el primero sobre el segundo´ ")
        print("ingrese [6] , si quiere encontrar el residuo de la division de los polinomios ´el primero sobre el segundo´ ")
        print("ingrese [7] , si desea salir del programa")
        opcion=(int(input("inserte la opcion deseada : ")))
        while opcion<1 or opcion>7:
            opcion=(int(input("Recuerde solo se pueden realizar 7 opciones : ")))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 43------------------------------------------------------------
        if opcion==1:
            print("\n",presenta2*3,presenta*15,"PROBLEMA 43-Evalua",presenta*15,presenta2*3,"\n")
            poli1=lectura_final(str(input("ingrese el polinomio a evaluar , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            num1=(int(input("ingrese el valor de la literal o ´x´ la cual desea evaluar en el polimonio dado : ")))
            print("el resultado de evaluar",num1,"en el polinomio dado ",poli1,"es :" ,evaluar(poli1,num1))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 44------------------------------------------------------------
        if opcion==2:
            print("\n",presenta2*3,presenta*15,"PROBLEMA 44-Sumar",presenta*15,presenta2*3,"\n")
            poli1=lectura_final(str(input("ingrese el primer polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            poli2=lectura_final(str(input("ingrese el segundo polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            print("La suma de los poliniomos dados es :",sumar(poli1,poli2))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 45------------------------------------------------------------
        if opcion==3:
            print("\n",presenta2*3,presenta*15,"PROBLEMA 45-Restar",presenta*15,presenta2*3,"\n")
            poli1=lectura_final(str(input("ingrese el primer polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            poli2=lectura_final(str(input("ingrese el segundo polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            print("La resta de los poliniomos dados es :",resta(poli1,poli2))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 46------------------------------------------------------------
        if opcion==4:
            print("\n",presenta2*3,presenta*15,"PROBLEMA 46-Multiplicacion",presenta*15,presenta2*3,"\n")
            poli1=lectura_final(str(input("ingrese el primer polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            poli2=lectura_final(str(input("ingrese el segundo polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            print("La multiplicacion de los poliniomos dados es :",multiplica(poli1,poli2))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 47------------------------------------------------------------
        if opcion==5:
            print("\n",presenta2*3,presenta*15,"PROBLEMA 47-Division sintetica",presenta*15,presenta2*3,"\n")
            poli1=lectura_final(str(input("ingrese el primer polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            poli2=lectura_final(str(input("ingrese el segundo polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            print("La division sintetica de los poliniomos dados es :",divide(poli1,poli2))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 48------------------------------------------------------------
        if opcion==6:
            print("\n",presenta2*3,presenta*15,"PROBLEMA 48-Residuo",presenta*15,presenta2*3,"\n")
            poli1=lectura_final(str(input("ingrese el primer polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            poli2=lectura_final(str(input("ingrese el segundo polinomio , recuerde que para identificar la potencicion debe usar ^ y para separar los polinomios use un +  o - nunca un espacio: ")))
            print("El residuo de la division sintetica de los poliniomos dados es :",residuo(poli1,poli2))
        #-----------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------PROBLEMA 49------------------------------------------------------------
        if opcion==7:
            print("Gracias por usar el programa")
            fin=False
main()
