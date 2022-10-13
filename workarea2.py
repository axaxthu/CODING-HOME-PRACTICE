#ANOTHER METHOD TO DO WORK AREA

age= int(input("ENTER YOUR AGE: "))
sex=str(input("ENTER YOUR SEX(M/F): "))
mar=str(input("ARE YOU MARRIED(Y/N): "))

if sex=='M' and age<40 and age>=20:
    print("YOU MAY WORK ANYWHERE")
elif sex=='M' and age>=40 and age<=60:
    print("YOU MAY WORK IN URBAN AREAS ONLY")
elif sex=='F' and age>=20 and age<=60:
    print("YOU MAY WORK IN URBAN AREAS ONLY")
else:
    print("ERROR")       