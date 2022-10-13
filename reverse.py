#ENTER A FOUR DIGIT NUMBER AND PRINT ITS REVERSE AS NEW NUMBER
num= int(input("ENTER A FOUR DIGIT NUMBER: "))

firstnum= num//1000 #OR firstnum=int(num/1000)
rem= num%1000
secnum= rem//100
rem2=rem%100
thinum=rem2//10
rem3=rem2%10

newnum= (rem3*1000)+(thinum*100)+(secnum*10)+(firstnum)
print("REVERSE OF THE NUMBER IS: ", newnum)
