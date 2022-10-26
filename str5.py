#enter 2 strings and check if their first and last values are equal
#enter a number n
#if they are equal, find the square root of n
#else find cube root of n
s1=str(input())
s2=str(input())
n=int(input())
f1=s1[0]
l1=s2[-1]
f2=s2[0]
l2=s2[-1]

if f1==l1 and f2==l2:
    sq=n**0.5
    print("THEY ARE EQUAL")
    print("square root of n is",sq)
else:
    cb=n**(1/3)
    print("THEY ARE NOT EQUAL")
    print("cube root of n",cb)    