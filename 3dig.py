#input a three digit number and print each of its digits(in reverse order)and also divide the number by 2(without any decimal)
n=int(input("INPUT A THREE DIGIT NUMBER: "))
l=n%10
m=(n//10)%10
f=n//100
print(l)
print(m)
print(f)
half=n//2
print(half)