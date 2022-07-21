#def tamano_grande(lista):
#    largo=len(lista)
#    indice=lista.index(lista[0])
#    while largo > indice:
#        valor=lista[indice]
#        if valor > 0:
#            lista[indice]='BIG'
#        indice +=1
#    print(lista)    
#tamano_grande([2,-4,1,-6,5])

#def tamano_grande_for(lista):
#    for a in range(len(lista)):
#        valor=lista[a]
#        if valor > 0:
#            lista[a]='BIG'
#    print(lista)
#tamano_grande_for([2,-4,1,-6,5])    
####################################################

#def cuenta_positivos(lista):
#    lst=[]
#    indice=lista.index(lista[0])
#    largo=len(lista)
#    while largo > indice:
#        valor=lista[indice]
#        if valor > 0:
#            lst.append(valor)
#        indice +=1
#    largo_lst=len(lst)
#    lista[-1]=largo_lst
#    print(lista)
#cuenta_positivos([1,6,-4,-2,-7,-2])

#def cuenta_positivos_for(lista):
#    lst=[]
#    for a in range(len(lista)):
#        valor=lista[a]
#        if valor > 0:
#            lst.append(a)
#    largo_lst=len(lst)
#    lista[-1]=largo_lst
#    print(lista)

#cuenta_positivos_for([1,6,4,-2,-7,2])
#####################################################

#def suma_total(lista):
#    lst=[]
#    indice=lista.index(lista[0])
#    largo=len(lista)
#    valor=0
#    while largo > indice:
#        valor += lista[indice]
#        indice += 1
#    print(valor)

#suma_total([1,2,-3,5,15])

#def suma_total_for(lista):
#    total=0
#    for i in range(len(lista)):
#        total +=lista[i]
#    return total

#print(suma_total_for([1, 2]))

########################################################

#def promedio(lista):
#    indice=lista.index(lista[0])
#    largo=len(lista)
#    valor=0
#    while largo > indice:
#        valor += lista[indice]
#        indice +=1
#    prom=valor/largo
#    print(prom)
#promedio([5,6,7])

#def promedio_for(lista):
#    total=0
#    prom=0
#    for i in range(len(lista)):
#        total +=lista[i]
#    prom=total/(len(lista))
#    return prom
#print(promedio_for([5,6,7,8]))
##########################################################

#def largo_lst(lista):
#    largo = len(lista)
#    print(largo)
#largo_lst([])

###########################################################

#def minimo_lst(lista):
#    largo=len(lista)
#    if largo==0:
#        print('False')
#    else:
#        minimo=min(lista)
#        print(minimo)
#minimo_lst([])
###########################################################

#def maximo_lst(lista):
#    largo=len(lista)
#    if largo==0:
#        print('False')
#    else:
#        maximo=max(lista)
#        print(maximo)
#maximo_lst([])
###########################################################

#def analisis_fin(lista):
#    largo=len(lista)
#    indice=lista.index(lista[0])
#    dicc={}
#    valor=0
#    minimo=min(lista)
#    maximo=max(lista)
#    while largo > indice:
#        valor += lista[indice]
#        indice +=1
#    prom=valor/largo
#    dicc['sumTotal']=valor
#    dicc['promedio']=prom
#    dicc['minimo']=minimo
#    dicc['maximo']=maximo
#    dicc['longitud']=largo
#    print(dicc)
#analisis_fin([5,6,7,8])

#def analisis_fin_for(lista):
#    dicc={}
#    valor=0
#    minimo=min(lista)
#    maximo=max(lista)
#    for i in range(len(lista)):
#        valor += lista[i]
#    prom=valor/len(lista)    
#    dicc['sumTotal']=valor
#    dicc['promedio']=prom
#    dicc['minimo']=minimo
#    dicc['maximo']=maximo
#    dicc['longitud']=len(lista)
#    return dicc 

#print(analisis_fin_for([5,6,7,8]))
    
##############################################################

#def reversa(lista):
#    largo=len(lista)
#    indice=lista.index(lista[0])
#    valor=0
#    while largo > indice:
#        valor=lista[-1]
#        lista.remove(valor)
#        lista.insert(indice,valor)
#        indice +=1
#    print(lista)


#reversa([1,2,3,4,5,6,7,8,9,10,-3])

#def reversa_for(lista):
#    valor=0
#    for i in range(len(lista)):
#        valor=lista[-1]
#        lista.remove(valor)
#        lista.insert(i,valor)
#    return lista

#print(reversa_for([1,2,3,4,5,6,7,8,9,10,-3]))

# Ejercicio propuesto 1
#print("Ingresa Entero Postivo")
#numero=input()
#numero=int(numero)
#if numero > 0:
#    dato=(numero*(numero+1)/2)
#else:
#    print('Error')
#    exit()
#print(dato)

# Ejercicio propuesto 2
peso_pay=112
peso_mun=75
pesos=(112,75)
lista=[]
print("Ingresa cantidad Payasos:")
num_pay= input()
num_pay=int(num_pay)
total_pay=peso_pay*pesos[0]
print("Ingresa cantidad Muñecos:")
num_mun= input()
num_mun=int(num_mun)
total_mun=peso_mun*pesos[1]
lista.append(total_pay+total_mun)
print("El peso por cant de Payasos es:",total_pay)
print("El peso por cant de Muñecos es:",total_mun)
print("El peso total:",lista)




