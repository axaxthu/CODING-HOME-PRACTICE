#Ask user to enter age, sex(M/F), marital status (Y/N) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"

age= int(input("ENTER YOUR AGE: "))
sex=str(input("ENTER YOUR SEX(M/F): "))
mar=str(input("ARE YOU MARRIED(Y/N): "))

if sex=='F' or sex=='f'and age<=60 and age>=20:
    print("YOU WILL WORK IN URBAN AREAS ONLY")
elif sex=='m' or sex=='M' :
    if age>=20 and age<40:
        print("YOU MAY WORK ANYWHERE ASSIGNED")   
    elif age>=40 and age<60:
        print("YOU WILL WORK IN URBAN AREAS ONLY")
    else:
        print("ERROR")
else:
    print("ERROR")      




