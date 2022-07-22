
###########  Basico
#for i in range (0,150,1):
#    print(i)
###########  Basico while
#i=0
#while i < 150:
#    print(i)
#    i += 1


###########  multipos de 5
#for i in range (5,1000,5):
#    print(i)
###########  multiplos de 5 while
#i=5
#while i < 1000:
#    print(i)
#    i += 5


###########  contar estilo dojo
for a in range (1,101,1):    
    var_5=(str(a).endswith("5"))
    var_10=(str(a).endswith("0"))
    if a % 5 == 0 and var_5==True:
        print('Coding', a)
    elif a % 10 == 0 and var_10==True:
        print('Coding Dojo', a)
    else:
        print(a)
###########  contar con estilo dojo while
#a=1
#while a <= 100:
#    var_5=(str(a).endswith("5"))
#    var_10=(str(a).endswith("0"))    
#    if a % 5 ==0 and var_5==True:
#        print('Coding',a)
#    elif a % 10 ==0 and var_10==True:
#        print('Coding Dojo',a)
#    else:
#        print(a)
#    a +=1


 ###########  Whoa. es un gran idiota
#var=0
#for a in range (0,500000,1):
#    if a % 2 != 0:
#        var=var+a
#        print(a)
#print(var)
###########  Whoa. es un gran idiota while
#acum=0
#var=0
#while var < 500000:
#    if var % 2 != 0:
#        print(var)
#        acum=acum+var
#    var += 1    
#print(acum)
         

###########  Cuenta regresiva 4 en 4
#for a in range (2018,1,-4):
#    print(a)
###########  Cuenta regresiva 4 en 4 while
#var=2018
#var1=1
#while var >= var1:
#    print(var)
#    var = var - 4
#    if var1 < 0:
#        break
#var1 +=1    
    #test pm

###########  Contador Flexible
#lowNum=2
#highNum=9
#mult=3
#for a in range(lowNum,highNum + 1):
#    if a % mult==0:
#        lowNum +=1
#        print(a)
###########  Contador Flexible while
#while lowNum <= highNum:
#    if lowNum % mult==0:
#        print(lowNum)
#    lowNum +=1
