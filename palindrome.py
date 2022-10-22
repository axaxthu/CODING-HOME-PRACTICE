#enter a string and check whether its reverse is the same(palindrome string)
s=str(input())
rev=s[:-1]
rev1=rev+s[-1]

if rev1==s:
    print("PALINDROME")
else:
    print("NOT PALINDROME")    