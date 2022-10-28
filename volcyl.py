#calculate and print volume of a cylinder
r=float(input("ENTER RADIUS OF THE CYLINDER: "))
h=float(input("ENTER HEIGHT OF THE CYLINDER: "))
P=3.141

vol=P*(r**2)*h   #volume of a cylinder= pi*r(square)*h
print("VOLUME OF THE CYLINDER IS {:.2f}".format(vol))