# 1. TASK: print "Hola, mundo"
print( "Hola, mundo" )
# 2. print "Hola Noelle!" con el nombre de una variable
name = "Jorge"
print( "Hola,", name )	# con una coma
print( "Hola,"+ name )	# con un +
# 3. print "Hola 42!" con el número en una variable
name = 42
print(  "Hola,", name,"!" )	# con una coma
print(  "Hola," + str(name),"!" )	# con un +	-- ¡esta nos debería arrojar un error!
# 4. print "Amo comer sushi y pizza." con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "Amo comer {} y {}".format(fave_food1,fave_food2) ) # with .format()
print( f"Amo comer {fave_food1} y {fave_food2}" ) # with an f string

x=100
if x > 50:
    print('Mayor a 50 -> ',x)
elif x > 55:
    print('Mayor a 50 (elif) -> ',x)
else:
    print('Menor a 50 -> ',x)

for x in range(0,10,2):
    print(x)
for x in range(5,1,-3):
    print(x)




mi_list=['abc',123,'hik']

for i in range(0,len(mi_list)):
    print(i,mi_list[i])

for v in mi_list:
    print(v)

mi_dict={'name':'Jorge','lenguaje':'Python'}

for k in mi_dict:
    print(k)        # Solo muestra las key del diccionario

for x in mi_dict:
    print(mi_dict[x])

for key in mi_dict.keys(): # Otra forma de iterar y obtener las key
    print(key)

for val in mi_dict.values(): # Otra forma de iterar y obtener los valores
    print(val)

for key,val in mi_dict.items(): # Otra forma de iterar y obtener las key y valores
    print(key,"=",val)


for count in range(0,5):
    print("looping -", count)
#################### Ambos ciclos (for y while hacen lo mismo)
count=0
while count < 5:
    print('looping -',count)
    count += 1

# ejemplo de while con else
y=3
while y > 0:
    print(y)
    y=y-1
else:
    print('fin del ciclo')    

# ejemplo de ciclo for con break
palabra='domingo'

for x in palabra:
    if x=='g':
        break
    print(x)    

# ejemplo de ciclo for con sentencia continue
for x in palabra:
    if x=='i':
        continue
    print(x)

# ejemplo de ciclo while con sentencia break

y=4
while y > 0:
    print(y)
    y=y-1
    if y == -1:
        break
else:
        print('fin del ciclo')    