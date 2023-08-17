
# Introduction
print("Equation 2nd degree!!!")

# Variables affectation
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))


# Procedures
if a==0 and b==0 and c==0:
    print("Infinity")
elif a==0 and b==0:
    print("Impossible")
elif a==0:
    solution=-c/b
    print("The solution is ",solution)
else:
    Delta=b**2 - 4*a*c
    if Delta == 0:
        solution=-b/(2*a)
        print("We have a double solution ",solution)
    elif Delta>0:
        solution1=(-b-Delta**(1/2))/(2*a)
        solution2=(-b+Delta**(1/2))/(2*a)
        print("We have two solutions\nx1=",solution1,"\nx2=",solution2)
    else:
        print("No solution in IR")
