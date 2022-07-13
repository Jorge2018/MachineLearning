import random

def randInt(val_a = '', val_b = ''):
    if(val_a == '' and val_b !=''):  ### Solo el valor b
        val_a = 0
        valor_0=random.random() * val_b
        valor_fin=round(valor_0)
    elif(val_a != '' and val_b ==''):### Solo el valor a
        valor_fin=0
        while valor_fin < val_a:
            val_b = 100
            valor_0=random.random() * val_b
            valor_fin=round(valor_0)
    elif(val_a != '' and val_b !=''):### Ambos valores
        valor_fin=0
        if val_a > val_b:
            val_a,val_b=val_b,val_a
        while valor_fin < val_a or valor_fin > val_b:
            valor_0=random.random() * val_b
            valor_fin=round(valor_0)
    else:                            ### Sin valores
        valor=random.random()     
        valor_fin=round(valor * 100)
    return valor_fin

print(randInt(val_a=15, val_b=5))


