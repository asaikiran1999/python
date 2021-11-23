
ex_list = [1,2,3,4] #taking a list
def get_square(lst):#creating a generator method
    for num in lst:
        yield num**2 # yield converts into a iteration concept

result = get_square(ex_list)#forms a iteration object

print(result)
#three ways of expressing iteration objects of generator function
#1.converting genorators into list
result = get_square(ex_list)
print(list(result))
#2. by calling through for loop
result = get_square(ex_list)
for i in result:
    print(i)
#3. by calling through using next
result = get_square(ex_list)
print(next(result))

#gnerator expression
#some what same as list compression
result=(x**2 for x in range(4))
print(result)
print(next(result))
