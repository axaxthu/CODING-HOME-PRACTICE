#input a number add it with 0.5 and then print the value in 3 decimal and 4 decimal places
n=int(input())
n+=0.5
print("{:.3f}".format(n))
print("{:.4f}".format(n))