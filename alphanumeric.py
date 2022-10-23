#enter a string and check whether it is alphanumeric(has only alphabets and numbers)
#if it is alphanumeric replace the middle of the string with $
s=str(input())

if s.isalnum():
    print("IT IS ALPHANUMERIC")
    l=len(s)
    i=l-1
    m=round(i/2)
    print(s[0:m]+"$"+s[(m+1):i]+s[i]) #REPLACE FUNCTION IS NOT USED BECAUSE IT WILL CHANGE ALL THE SAME CHARACTERS(IF ANY) OF MIDDLE INDEX WITH $
else:
    print("IT IS NOT ALPHANUMERIC")

