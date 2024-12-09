#This programme only built for quadrilateral shape field area measurement.
#Different quadrilaterals are divided into diffearent functions.
print("     {Find the area of your quadrilateral field}-")
def chos():
    print("There are five types of quadrilateral shaped field that you can chose.")
    list=[]
    qa="square"
    qb="rectangle"
    qc="rhombus"
    qd="parellelogram"
    qe="trapezium"
    list.append(qa)
    list.append(qb)
    list.append(qc)
    list.append(qd)
    list.append(qe)
    print(list)
    return list 
chos()  
def square():
    a=str(input("Do you wanna calculate(A) of a square field?(yes/no): "))
    if(a.lower() != "yes"):
        quit()
    else:
        s=float(input("Enter the side length of your square field: "))
        #Area of the square= (s)^2 or (s)**2
        area=s**2
        print("Area of your square field is:",area)
        return area
square()
def rectangle():
    b=str(input("Do you wanna calaculate(A) of rectangular field?(yes/no): "))
    if(b.lower() != "yes"):
        quit()
    else:
        len=float(input("Enter the length of the side of your rectangular field: "))
        bth=float(input("Enter the length of the width of your rectangular field: "))
        #Area of raectangle= 2(l + b) or 2*(l + b)
        area=2*(len + bth)
        print("Area of your square field is",area)
        return area
rectangle()
def rhombus():
    c=str(input("Do you wanna calculate(A) of rhombus shaped field?(yes/no): "))
    if(c.lower() != "yes"):
        quit()
    else:
        #Calculation of area through parallelogram method-
        base=float(input("Emter the length of the base of your rhombus shaped field: "))
        height=float(input("Enter the height(length of perpendicular) of your rhombus shaped field: "))
        #Area of rhombus= base * height or 1/2*product of diagonals
        area=base * height
        print("Area of your rhombus shaped field is",area)
        return area
rhombus()
def parellelogram():
    d=str(input("Do you wanna calculate(A) of parellelogram shaped field?(yes/no): "))
    if(d.lower() != "yes"):
        quit()
    else:
        base=float(input("Enter the base-length of your parellelogarm shaped field: "))
        height=float(input("Enter the height(perpendicular length) of your parellelogram shaped field: "))
        #Area of parellelogram=base * height
        area=base * height
        print("Area of your parellelogram shaped field is:",area)
        return area 
parellelogram()
def trapezium():
    e=str(input("Do you wnanna calculate(A) of a trapezium shaped field?(yes/no): "))
    if(e.lower() != "yes"):
        quit()
    else:
        p1=float(input("Enter the length of the first parellel side of your tarpezium shaped field: "))
        p2=float(input("Enter the length of the second parellel side of your tarpezium shaped field: "))
        height=float(input("Enter the height of the field: "))
        #Area of trapezium= 1/2*(sum of the parellel sides)*height
        def sum():
            a=p1+p2
            return a
        sum()
        area=1/2 * sum() * height
        print("Area of your parellelogram shaped field is:",area)
        return area
trapezium()
