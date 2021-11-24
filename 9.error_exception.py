#exception handling
a=3
b=90
try:

    print("open a resource")
    print(a/b)
    i = int(input("enter a number"))
    print(i)
except ZeroDivisionError as e:
    print("1:",e)
except ValueError as e:
    print("2:",e)
except Exception as e:
    print("3:",e)

finally:
    print("close the resource")

#assertions
#example 1
try:
    num = int(input("enter the number"))
    assert num%2==0 #raises the assertion error
    print("the number is even")
except AssertionError:#catches the assertion error
    print("Please enter even number")

#example 2
#here even one of the assertion statement is wrong it calls assertion exception 
try:
    num = int(input("enter the number"))
    assert num%2==0
    print("the number is even")
    assert num<20
    print("the given number is greater than 20")
except AssertionError:
    print("Please enter even number")

