tot=int(input("NUMBER OF CLASSES HELD: "))
pre= int(input("NUMBER OF CLASSES ATTENDED: "))
att= (pre/tot)*100

if att>=75:
    print("you are eligible to sit for the examination")
else:
    print("you are not eligible to sit for the examination")     
