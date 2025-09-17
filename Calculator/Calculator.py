    while True:
        n1=float(input("Enter first number:"))
        n2=float(input("Enter second number:"))
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Exponent")
        print("5.Division")
        print("6.Floor Division")
        print("7.Modulo")
        operation=int(input("Choose your operation(MUST BE NUMBER!!):"))

        if operation==1:
            print(f"Sum of your numbers is {n1+n2}")


        elif operation==2:
            print("1.Difference n1 to n2")
            print("2.Difference n2 to n1")
            difference=int(input("Choose which difference you want(MUST BE NUMBER!!):"))
            if difference==1:
                print(f"Difference of your numbers is {n1-n2}")
            elif difference==2:
                print(f"Difference of your numbers is {n2-n1}")
            else:
                print("ERROR")

        elif operation==3:
            print(f"Product of your numbers is {n1*n2}")

        elif operation==4:
            print("1.Exponent of n1")
            print("2.Exponent of n2")
            power=int(input("Choose power of which number you want(MUST BE NUMBER!!):"))
            powering_number=float(input("Choose to which power you want your number to be:"))
            if power==1:
                print(f"Power of your number is {n1**powering_number}")
            elif power==2:
                print(f"Power of your number is {n2**powering_number}")
            else:
                print("ERROR")

        elif operation==5:
            print("1.Quotient of n1 to n2")
            print("2.Quotient of n2 to n1")
            quotient=int(input("Choose which quotient you want(MUST BE NUMBER!!)"))
            if quotient==1:
                print(f"Quotient of your numbers is {n1/n2}")
            elif quotient==2:
                print(f"Quotient of your numbers is {n2/n1}")
            else:
                print("ERROR")

        elif operation==6:
            print("1.Floor Quotient of n1 to n2")
            print("2.Floor Quotient of n2 to n1")
            floor_quotient=int(input("Choose which floor quotient you want(MUST BE NUMBER!!)"))
            if floor_quotient==1:
                print(f"Floor Quotient of your numbers is {n1//n2}")
            elif floor_quotient==2:
                print(f"Floor Quotient of your numbers is {n2//n1}")
            else:
                print("ERROR")

        elif operation==7:
            print("1.Modulo of n1 to n2")
            print("2.Modulo of n2 to n1")
            modulo=int(input("Choose which modulo you want(MUST BE NUMBER!!)"))
            if modulo==1:
                print(f"Modulo of your numbers is {n1%n2}")
            elif modulo==2:
                print(f"Modulo of your numbers is {n2%n1}")
            else:
                print("ERROR")

        else:
            print("ERROR")

        continue_operation=input("Do you wish to try another operation? (yes/no):").lower()
        if continue_operation!="yes":
            print("Goodbye!")
            break
















    




















            

