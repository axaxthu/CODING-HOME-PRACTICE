#input two integers and check whether they are same object or not(using is not operator)
a=int(input())
b=int(input())

boo=a is not b
print("{} is not {} = {}".format(a,b,boo))