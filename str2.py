#input a string and check whether it ends with a vowel or not
s=str(input())
#this program will be done in two methods

#method 1

if s.endswith("a") or s.endswith("e") or s.endswith("i") or s.endswith("o") or s.endswith("u"):
    print("ends with vowel")
else:
    print("does not end with vowel")

#method 2
l=s[-1]

if l=="a" or l=="e" or l=="i" or l=="o" or l=="u": #this is a much less time-consuming method
    print("ends with vowel")
else:
    print("does not end with vowel")    