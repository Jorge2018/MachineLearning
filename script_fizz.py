for a in range (1,21,1):    
    if a % 5 == 0  and a % 3 == 0:
        print('FizzBuzz')
    elif a % 5 == 0 :
        print('Buzz')   
    elif a % 3 == 0 : 
        print('Fizz')
    else:
        print(a)