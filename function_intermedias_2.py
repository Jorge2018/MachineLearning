x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

##################################
#print(x)
#x[1][0]=15
#print(x)
##################################
#print(students[0])
#students[0]['last_name']='Bryant'
#print(students)
#################################
#print(sports_directory['soccer'])
#sports_directory['soccer'][0]='Andres'
#print(sports_directory)
##################################
#print(z)
#z[0]['y']=30
#print(z)
##################################

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    largo=len(students)
    indice=students.index(students[0]) 
    while largo > indice:
        print('first_name -', students[indice]['first_name'] + ',' + ' last_name -',students[indice]['last_name'] )
        indice += 1
#iterateDictionary(students)
##########################################################

def iterateDictionary2(key_name,lista):
    largo=len(students)
    indice=lista.index(lista[0])
    while largo > indice:
        print(lista[indice][key_name])
        indice +=1
#iterateDictionary2('first_name',students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(dicc):
    contador_a=len(dojo['locations'])
    contador_b=len(dojo['instructors'])
    indice=0
    indice_b=0
    print(str(contador_a) + ' Locations')
    while contador_a > indice:
        print(dojo['locations'][indice])
        indice += 1
    print('')
    print(str(contador_b) + ' Instructors')
    while contador_b > indice_b:
        print(dojo['instructors'][indice_b])
        indice_b += 1
        

printinfo(dojo)

