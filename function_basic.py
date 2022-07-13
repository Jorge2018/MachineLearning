#def cuentaregresiva(a):
#    lst=[]
#    while a >= 0:
#        lst.append(a)
#        a -=1
#    print(lst)
#cuentaregresiva(14)
#########################################################
#def print_return(lista):
#    print(lista[0])
#    return lista[1]
#lista=[11,24] 
#print(print_return(lista))
##########################################################
#def primer_largo (lista):
#    cont=0
#    cont=len(lista)
#    print(int(lista[0] + cont))
#primer_largo([2,2,3,4,8])
###########################################################
#def largo_valor(a,b):
#    val_a=int(a)
#    val_b=int(b)
#    cont=0
#    lst=[]
#    while cont < val_a:
#        lst.append(val_b)
#        cont +=1
#    print(lst)
#largo_valor(10,3)
############################################################
def valor_may(lista):
    valor=0
    largo=0
    lst=[]
    if len(lista) < 2:
        print('False') 
    else:
        largo=len(lista) # 6
        valor=lista[1]   # 2
        indice = lista.index(valor) + 1 # 2
                    
        while largo >= indice:
            maximo=max(lista)
            if maximo > valor:
                lst.append(maximo)
                lista.remove(maximo)       
            indice += 1
        print(len(lst))        
        return (lst)    

print(valor_may([50,4,31,2,1,7]))


