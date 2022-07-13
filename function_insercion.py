lista=[2,5,3,1,8,0,4,32,10,-3,9] 

def orden_insercion(lista):
    largo=len(lista)
    for i in range(largo):
        for j in range(i,0,-1):
            if(lista[j-1] > lista[j]):
                #print( lista[j-1], lista[j])
                var=lista[j]
                lista[j]=lista[j-1]
                lista[j-1]=var
    return lista
 


print (orden_insercion(lista))
