#enter a 8 letter string and form a new word with its first two and last two words
s=str(input("ENTER AN 8 LETTER STRING: "))
f=s[0:2]
l=s[6:]
print("new word is:",f+l)