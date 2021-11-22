# data types
# int 
# float #compex boolean
#string
s = "data science"
print(s[1:2])#a
print(s[-1:-2])#prints nothing and prints no error
print(s[-1:0])#prints nothing and prints no error
print(s[0])#prints d
print(s[3])#prints a
print(s[-3])#prints n
print(s[0:-1])#prints data scienc
print(s[-3:-1])#prints nc    

#"str()" function which convert integer into string 

      def printn(n):
     full_str=""
     for i in range(1,n+1):
        full_str += str(i)          # 'str(i)'
     return full_str
a= printn(5)
print(a) # if we give 5 it prints 12345

    
#Update Strings    
var1 = 'Hello World!'
print('Hello')
print ("Updated String :- ", var1 + 'Python')
print ("Updated String :- ", var1[:6] + 'Python');
print("hello \nworld") # \n used to get new line

#functions in string 
string = "data science"
print(string.capitalize())
string.center(50)
len(string.center(50))# doesn't prints anything
print(string.center(50))
substring="a"
print(string.count(substring))#counts the substring
print(string.count(substring,3,6))#counts the substring from index 3 to 6
string="t123"
print(string.isalnum())#combination of numbers and alphabets
print(string.isalpha())#only alphabets
print(string.isdigit())# only digits
print(string.upper())# changes to upper case
print(string.lower())# lower to lower case
string = "here is the most precious the diamond"
print(string.replace("the" , "sai"))
print(string.replace("the" , "sai",1))
print(string.split())
#print(string.split("",1))

#list
nums = [25 , 839,33,2,8,1]
print(nums)
print(nums[0])
print(nums[2:4])
print(nums[2:])
print(nums[:4])
values = ['sai',2,3,4 "kiran"]
print(values)
print(values[2:])
mix=[['sai','kiran','help'],[1,2,34,44]]
#print(mix[0][3])
#print(mix[1][2])
mil=[value,mix]
print(mil)
del mil
nums.exdend(29,12,14,34)
print(nums)
nums.sort()
print(nums)#list is mutable

#tuples

tup=(1,3,4,5,6)
print(tup[1])
print(tup.count(4))#should take an argument
tup2=(3,5,7,8,'kiran')
tup3=tup2+tup2
print(tup3)

#sets

s={ 1,2,2,4,2,3,5,5,3,6}
print(s)
 
 #dictionay

dic={1:'sai',2:'kiran',3:'r'}
print(dic[3])
#print(dic[4]) error 
dic2={ 'sai':'kiran','e':'d','er':'oik'}
print(dic2['sai'])
data = dict(zip(dic,dic2))  #1st keys: 2nd values
print(data)
print(data.keys())
print(data.values()) 


# arrays 
from array import*
vals = array('i',(9,0,3,6,1))
print(vals)
print(vals.buffer_info()) #addreas and size of a array
print(vals.typecode) #type of array
#printing of array
for i in range(2):
    print(vals[i])
    
for i in vals:
    print(i)
    
i=0
while i<len(vals):
    print(vals[i])
    i+=1


#introducing values into an empty array
# storing double of that array into another array
from array import *
vals = array('i',[])

n=int(input('enter the length of array'))
for i in range(n):
    x=int(input("enter the value of array"))
    vals.append(x)

newarr = array(vals.typecode,(a*2 for a in vals))
for i in newarr:
    print(i,end=".")


