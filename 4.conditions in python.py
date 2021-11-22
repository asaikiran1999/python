  # if clause
x= int(input("enter the marks"))
if x>=90:
    print('a grade')
elif x>=50:
    print('B GRADE')
elif  x<50:
    print("fail")


 # for loop
x=['sai kiran',6.5,34]
for i in x:
    print(i)


#While loop
x=int(input('enter number'))
print()
print('tables')
i=1
while i<=10:
    t=x*i
    print(t)
    i+=1
  
   #break continue  and  pass

 # break
av = 10
n = int(input('enter no of candies you want'))
for i in range(n):
      if i >= av :
         break
      print("candies")
print("bye")


# continue
n= int(input("enter the number"))
for i in range(n+1):
    if (i == 5):
        continue
    print(i)

# pattern printing
 
 # print '####
          ####
          ####
          ####'



for i in range(4):
    print("")
    for j in range(4):
        print("#",end="")  
#how to print ####
              ###
              ##
              #      
for i in range(1,4):
    print("")
    for j in range(i,5):
        print("#",end="")  

#how to print #
              ##
              ###
              ####

for i in range(1,5):
    print("")
    for j in range(i):
        print("#", end="")
 #how to print #### doubt
                ###
                 ##
                  #
 '''Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
******* '''                 
def histogram(lists):
    for i in lists:
         stringn = ''
         n = i
         while(n>0):
            stringn += '*'
            n=n-1
         print(stringn)
    print('\n')

histogram([1,4,4,2])










  


  