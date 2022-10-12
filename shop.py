#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

q= int(input("ENTER QUANTITY"))
dis=0
totalcost=0
if(q*100>1000) :
    dis=.10*q*100
    totalcost= q*100 - dis
else:
    totalcost = q*100
print("TOTAL COST IS =",totalcost)    