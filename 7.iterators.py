nums = [1,2,3]

# for num in nums :#1 # here nums is taken as num using iteration concept
#    print(num)
# print(dir(nums)) # it has the '__iter__' but has no __next__
# so
# print(next(nums))#gives an Type error: 'list' object is not a iterator

#i_nums = nums.__iter__() # or 'iter(nums)' can be used #converting list into a iterator
#dir(nums)#now it has' __next__'
#print(next(i_nums))
# if you repeat the out of element count it gives an error 'StopIteration'

#IN FOR LOOP HOW THE ITERATION IS HAPPENING IS
nums = [1,2,3]
i_nums=iter(nums)  # calling of iterator '__iter__'
while True :
    try:
        item = next(i_nums) # call of '__next__'
        print(item)
    except StopIteration: #out of range exception
        break
