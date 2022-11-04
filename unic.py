#input an alphabet and print its unicode value
#after add 2 to the unicode and print its corresponding character

al=str(input("INPUT AN ALPHABET: "))

print(ord(al)) #using ord function unicode value of a character can be printed
un=ord(al)
un+=2
print(chr(un)) #using chr function character corresponding to a unicode value can be printed

