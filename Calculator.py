num1=float(input("Enter a number of choice:"))
num2=float(input("Enter a number of choice:"))
operation=input("Enter the sign of operation:")

if operation=="+":
    print("Answer=",num1+num2)
    print("Addition performed.")
elif operation=="-":
    print("Answer=",num1-num2)
    print("Subtraction performed.")
elif operation=="*":
    print("Answer=",num1*num2)
    print("Multiplication performed.")
elif operation=="/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Answer=",num1/num2)
        print("Division performed.")
elif operation=="%":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Answer=",num1%num2)
        print("Modulus performed.")
elif operation=="//":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Answer=",num1//num2)
        print("Floor Division performed.")
elif operation=="**":
    print("Answer=",num1**num2)
    print("Exponentiation performed.")
else:
    print("Invalid input")
    print("Please try again.")

input("Press enter to exit...")