# differnent types of functions
def printn() :
    print('life')
printn()

def add(a,b) :    #return one value
     c = a+b
     return c
print(add(1,20))

def add_sub(a,b):        # return 2 vqlues
    c=a+b
    d=a-b
    return c,d
print(add_sub(7,4))
result1,result2=add_sub(7,4)
print(result1)
print(result2)

 # passing variables as list
def add(*b):
     c=0
     for i in b :
         c+=i
     return c
print(add(1,2,6,8))

#Keyworded Variable Length Arguments
def printn(a,**b):
    print(a)
    for i,j in b.items():
        print(i,j)
    print(b)

printn('sai',age =1,score =3.4)


# CREATING FACTORIAL FUNCTION USING FOR LOOP
def fact(n):
    f=1
    for i in range(1,n+1):
        f=i*f
    return f

a=4
print(fact(a))

# CREATING FACTORIAL FUNCTION USING recursion
def fact(n):
 if n==0 :
    return 1
 return n*fact(n-1)

a=4
print(fact(a))

#using short functions lambda
#defining a short function lambda
f = lambda a,b:a+b
print(f(1,2))

#defining a short function lambda for filters,map,reduce fuctions
from functools import*
nums = [1,2,3,4,5,6]
evens = list(filter(lambda n : n%2==0, nums)) #filter eleminates with condition 
doubles = list(map(lambda a : a*2, evens)) #map use make changes to list element
sum =  reduce(lambda a,b :a+b ,evens ) #reduce use completely reduce a list into asinge variable
print(evens,doubles,sum)
  
  #decorators is not much useful




















