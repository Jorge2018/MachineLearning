test=[2,5,3,1,8,0,4,32,10,-3,9] 

def ordenBurbuja(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1-j):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista 
#print(ordenBurbuja(test)) 


def seleccion(lista):
    largo = len(lista)
    for i in range(largo):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista 
print(seleccion(test))