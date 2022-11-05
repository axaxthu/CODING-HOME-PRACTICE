#enter a 4 digit number and if the last digit of the number is an even number
#replace the last digit with "e"
#otherwise print the number itself as the output

n=int(input("ENTER A 4 DIGIT NUMBER: "))
l=n%10
num=n//10
if l%2==0:
    print("{}e".format(num))    
else:
    print(n)    