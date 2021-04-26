                    # Faulty Calculaator

# print("KINDLY ENTER THE OPERATOR FROM  +, -, *, /")
print("Enter 1 for add, 2 for substract, 3 for multiply, 4 for divide")
x = int(input())
if x == 1:
    print("Enter The value of First Number")
    y = int(input())
    print("Enter The Second Value")
    z = int(input())
    if y==56 and z == 9:
        print("Answer is 77")
    else:
        print("Sum  is ",(y+z))
elif x == 2:
    print("Enter The value of First Number")
    y = int(input())
    print("Enter The Second Value")
    z = int(input())
    print("The difference is",(y-z))
elif x == 3:
    print("Enter The value of First Number")
    y = int(input())
    print("Enter The Second Value")
    z = int(input())
    if y == 45 and z == 3:
        print("Answer is 555")
    else:
        print("Product is",(y*z))
elif x == 4:
    print("Enter The value of First Number")
    y = int(input())
    print("Enter The Second Value")
    z = int(input())
    if y == 56 and z == 6:
        print("Answer is 4")
    else:
        print("Quotient is",(y/z))
else:
    print("You have not entered a valid Operator. Please Check")