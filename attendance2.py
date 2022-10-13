tot= int(input("ENTER TOTAL CLASSES HELD: "))
PRE=int(input("TOTAL DAYS ATTENDED: "))

att= (PRE/tot)*100

if att>=75:
    print("YOU ARE ELIGIBLE TO SIT FOR THE EXAM")

else:
    med=str(input(" do you have any medical cause(Y/N): "))
    if med == "Y" or med == "y" :
        print("you are eligible")
    else:
        print("you are not eligible")    
