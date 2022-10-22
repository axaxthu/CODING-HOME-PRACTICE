#enter a binary value and print its octal value

bnum=input()
bnum=int(bnum,2) #2 is put here so as to make the default string into an integer with base 2 i.e,a binary number

o=oct(bnum)[2:]
print(o)
