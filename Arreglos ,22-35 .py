def crear_lista_2(a,b,c):
    if a<=b:
        c.append(a)
        crear_lista_2(a+1,b,c)
    return c
def crear_lista(a):
    lista=[]
    return tachar(crear_lista_2(2,a,lista))
def tachar(a):
    for i in a:
        for j in a:
            if j%i==0 and j!=i:
                a.remove(j)
    return a
def reales_2(a,b,c):
    if a<b:
        c.append(float(input("ingrese el elemento del arreglo de enteros : ")))
        return reales_2(a+1,b,c)
    return c
def reales():
    a=int(input("ingrese la longitud del arreglo de reales: "))
    lista=[]
    return reales_2(0,a,lista)
def enteros_2(a,b,c):
    if a<b:
        c.append(int(input("ingrese el elemento del arreglo de enteros : ")))
        return enteros_2(a+1,b,c)
    return c
def enteros():
    a=int(input("ingrese la longitud del arreglo de enteros: "))
    lista=[]
    return enteros_2(0,a,lista)
def sumar_lista(a):
    suma=0
    for i in range(0,len(a)):
        suma+=a[i]
    return suma
def promedio_lista_reales(a):
    return (sumar_lista(a)/len(a))
def promedio_lista_enteros(a):
    return int(sumar_lista(a)//len(a))
def producto_punto(a,b):
    sum=0
    for i in range(0,len(a)):
        sum+=a[i]*b[i]
    return sum
def minimo(a):
    j=0
    while j<len(a):
        i=0
        while i<len(a):
            if a[j]<=a[i]:
                i+=1
            else:
                i=0
                j+=1
        if i==len(a):
            return a[j]
def maximo(a):
    j=0
    while j<len(a):
        i=0
        while i<len(a):
            if a[j]>=a[i]:
                i+=1
            else:
                i=0
                j+=1
        if i==len(a):
            return a[j]
def producto_directo_2(a,b,c,d,e):
    if a<=b:
        e.append(c[a]*d[a])
        producto_directo_2(a+1,b,c,d,e)
    return e
def producto_directo(a,b):
    lista=[]
    return producto_directo_2(0,len(a)-1,a,b,lista)
def organiza_2(a,b,c):
    if b<c:
        if a[b]>a[b+1]:
            d=a[b+1]
            a[b+1]=a[b]
            a[b]=d
        a= organiza_2(a,b+1,c)
    if b==c-1:
        a= organiza_2(a,0,c-1)
    return a
def organiza(a):
    return organiza_2(a,0,len(a)-1)
def mediana_reales(a):
    if (len(a)%2)==0:
        return ((a[int(len(a)/2)] + a[int((len(a)/2)-1)])/2)
    return a[(len(a)//2)]
def mediana_enteros(a):
    if (len(a)%2)==0:
        return ((a[int(len(a)/2)] + a[int((len(a)/2)-1)])//2)
    return a[(len(a)//2)]
def organiza_ceros_2(a,b,c):
    if b<c:
        if a[b]==0:
            d=a[b+1]
            a[b+1]=0
            a[b]=d
        organiza_ceros_2(a,b+1,c)
    if b==c-1:
        organiza_ceros_2(a,0,c-1)
    return a
def organiza_ceros(a):
    return organiza_ceros_2(a,0,len(a)-1)
def decodifica_binario_invertido(a):
    sum=0
    for i in range(0,len(a)):
        sum+=(a[i]*(2**i))
    return int(sum)
def invierte_2(a,b,c,e):
    if c>=b:
        e.append(a[c])
        invierte_2(a,b,c-1,e)
    return e
def invierte(a):
    lista=[]
    return invierte_2(a,0,len(a)-1,lista)    
def numero_digitos_2(a,b):
    if a>=(2**b):
        return numero_digitos_2(a,b+1)
    return b
def numero_digitos(a):
    return (numero_digitos_2(a,0))    
def codifica_binario_2(a,b,c):
    if a>=(2**b) and b>=0:
        c.append(1)
        codifica_binario_2((a-2**b),b-1,c)
    elif a<(2**b) and b>=0:
        c.append(0)
        codifica_binario_2(a,b-1,c)
    return c
def codifica_binario_invertido(a):
    lista=[]
    return invierte(codifica_binario_2(a,numero_digitos(a)-1,lista))
def m_c_d_2(a,c,d,e):
    if ((e==0)and((a[e]%d)==0)and((a[e+1]%d)==0)):
        return m_c_d_2(a,d,minimo(a),e+2)
    elif ((e>1)and(e<len(a))and(c%d==0)and(a[e]%d==0)):
        return m_c_d_2(a,d,minimo(a),e+1)
    elif (d>1)and(e<len(a)):
        return m_c_d_2(a,c,d-1,e)
    return c 
def m_c_d(a):
    if len(a)>1:
        return m_c_d_2(a,1,minimo(a),0)
    return a[0]
def m_c_m_2(a,b,c,d):
    if (b==0):
        m=[a[b],a[b+1]]
        return m_c_m_2(a,b+2,c,(a[b]*a[b+1])/m_c_d(m))
    elif (b<c):
        m=[d,a[b]]
        return m_c_m_2(a,b+1,c,(d*a[b])/m_c_d(m))
    return d
def m_c_m(a):
    if len(a)>1:
        return int(m_c_m_2(a,0,len(a),1))
    return a[0]

def quickSort(a):
    if (a.len<1):
        return []
    var left = []
    

def main():
    presenta="{0:c}".format(8275)
    presenta2="{0:c} ".format(43007)
    print(presenta2*3,presenta*15,"Arreglos",presenta*15,presenta2*3,"\n")
    a=int(input("ingrese el numero del problema que desea realizar , recuerde del 22 al 34 :"))
    while a<22 or a>34:
        a=int(input("Recuerde solo es posible un numero del 22 al 34 :"))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 22------------------------------------------------------------
    if a==22:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 22",presenta*15,presenta2*3,"\n")
        num_1=int(input("inserte el numero hasta el cual se quieren hayar los primos atravez de la criba de eratostenes:"))
        print("La lista de numeros primos hasta ",num_1,"es :",tachar(crear_lista(num_1)))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 23------------------------------------------------------------
    if a==23:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 23",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            print("La suma de la lista de numeros enteros dada es : ",sumar_lista(lista_1))
        elif tipo_1==("R"):
            lista_1=reales()
            print("La suma de la lista de numeros reales dada es : ",sumar_lista(lista_1))
            
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 24------------------------------------------------------------
    if a==24:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 24",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            print("El promedio de la lista de numeros enteros dada es : ",promedio_lista_enteros(lista_1))
        elif tipo_1==("R"):
            lista_1=reales()
            print("El promedio de la lista de numeros reales dada es : ",promedio_lista_reales(lista_1))
            
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 25------------------------------------------------------------
    if a==25:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 25",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            lista_2=enteros()
            print("El producto punto de las listas de numeros enteros dadas es : ",producto_punto(lista_1,lista_2))
        elif tipo_1==("R"):
            lista_1=reales()
            lista_2=reales()
            print("El producto punto de las listas de numeros reales dadas es : ",producto_punto(lista_1,lista_2))
            
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 26------------------------------------------------------------
    if a==26:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 26",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            print("El minimo del arreglo de enteros dado es  : ",minimo(lista_1))
        elif tipo_1==("R"):
            lista_1=reales()
            print("El minimo del arreglo de reales dado es  : ",minimo(lista_1))
            
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 27------------------------------------------------------------
    if a==27:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 27",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            print("El maximo del arreglo de enteros dado es  : ",maximo(lista_1))
        elif tipo_1==("R"):
            lista_1=reales()
            print("El maximo del arreglo de reales dado es  : ",maximo(lista_1))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 28------------------------------------------------------------
    if a==28:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 28",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            lista_2=enteros()
            print("El producto directo de las listas de numeros enteros dadas es : ",producto_directo(lista_1,lista_2))
        elif tipo_1==("R"):
            lista_1=reales()
            lista_2=reales()
            print("El producto directo de las listas de numeros reales dadas es : ",producto_directo(lista_1,lista_2))
            
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 29------------------------------------------------------------
    if a==29:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 29",presenta*15,presenta2*3,"\n")
        tipo_1=str(input("inserte Z si quiere trabajar con enteros o R si quiere trabajar con reales : "))
        while tipo_1!=("Z") and tipo_1!=("R"):
            tipo_1=str(input("Recuerde solo Z o R : "))
        if tipo_1==("Z"):
            lista_1=enteros()
            print("La mediana del arreglo de enteros dado es  : ",mediana_enteros(organiza(lista_1)))
        elif tipo_1==("R"):
            lista_1=reales()
            print("La mediana del arreglo de reales dado es  : ",mediana_reales(organiza(lista_1)))
            
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 30------------------------------------------------------------
    if a==30:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 30",presenta*15,presenta2*3,"\n")
        lista_1=reales()
        print("La lista de manera ordenada tal que todos sus ceros estan al final es:",organiza_ceros(lista_1))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 31------------------------------------------------------------
    if a==31:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 31",presenta*15,presenta2*3,"\n")
        lista_1=enteros()
        print("La lista codificada en binario invertido corresponde al numero:",decodifica_binario_invertido(lista_1))

    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 32------------------------------------------------------------
    if a==32:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 32",presenta*15,presenta2*3,"\n")
        numero=int(input("Inserte el numero el cual desea convertir a binario invertido:"))
        print("El resultado de expresar el numero:",numero,"en binario invertido es:",codifica_binario_invertido(numero))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 33------------------------------------------------------------
    if a==33:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 33",presenta*15,presenta2*3,"\n")
        lista_1=enteros()
        print("El maximo comun divisor del arreglo dado es:",m_c_d(lista_1))
        
    #-----------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------PROBLEMA 34------------------------------------------------------------
    if a==34:
        print("\n",presenta2*3,presenta*15,"PROBLEMA 34",presenta*15,presenta2*3,"\n")
        lista_1=enteros()
        print("El minimo comun multiplo del arreglo dado es:",m_c_m(lista_1))
main()