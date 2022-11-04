#input 4 integers and print those which are divisible by both 3 and 5

a=int(input("NUMBER 1: "))
b=int(input("NUMBER 2: "))
c=int(input("NUMBER 3: "))
d=int(input("NUMBER 4: "))

k=[a,b,c,d]

for i in k:
    if i%3==0 and i%5==0:
        print(i)