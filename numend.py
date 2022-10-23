#input a string and check whether it ends with a numeric value

s=str(input())
l=s[-1]

if l.isdigit():
    print("True")
else:
    print("false")    