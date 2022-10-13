#INPUT AN YEAR AND FIND WHETHER IT IS A LEAP YEAR OR NOT

year=int(input("ENTER A YEAR: "))

if year%400==0:
    print("ENTERED YEAR IS A LEAP YEAR")
elif year%100==0 and year%400!=0:
   print("ENTERED YEAR IS NOT A LEAP YEAR")
elif year%4==0:
    print("ENTERED YEAR IS A LEAP YEAR")  
else:
    print("ENTERED YEAR IS NOT A LEAP YEAR")    