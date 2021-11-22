################################################## list comprehension example 1 ############################################

#checking a char without using list comprehension

list = ['apple','mango','orange','sses','ra','rr']
newlist=[]
for x in list:
    if "a" in x:
        newlist.append(x)
print(newlist)

#checking a char using list comprehension

list = ['apple','mango','orange','sses','ra','rr']
newlist=[x for x in list if "a"in x ] #the line 'if "a" in x' = checks the a in x and appends x into newlist
print(newlist)

############################################### listcomp. example2 #####################################################

# basic syntax : newlist = [expression for item in iterable if condition == True]

list = ['apple','mango','orange','sses','ra','rr']
newlist=[x for x in list if x!='apple' ]
print(newlist)

################################################ listcomp. example 3 ###################################################


#list compression   
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
#Solve
arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != n]
#Output
print(arr)

############################################## listcomp. example 4 ##########################################################
newlist=[x for x in range(10) if x!=5]
print(newlist)





