import numpy as np
#2 -> brownie
#1 -> galleta
#10 -> pastel
cantVent=[17,40,1]
precio=[2,1,10]
arr_cantVent=np.array(cantVent)
arr_precio=np.array(precio)

total=arr_cantVent*arr_precio
print(total)