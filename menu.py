def N():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    #return a,b
while True:
    print ("Main menu\n\
        1. Add\n\
            2. Subtract\n\
                3. Multiply\n\
                    4. Exit")
    option=int(input("Enter your option"))
    if option==1:
        N()
        print ("Sum is", a+b)
    elif option==2:
        N()
        print("Difference is", a-b)
    elif option==4:
        print("Thank you")
        break