#resturant PAY
bill = float(input("Please enter the bill : "))
x = (0.18 * bill) + (0.10 * bill)
y = (0.18 * bill) + (0.05 * bill)
z = (0.18 * bill) + (0.025 * bill)
w = (0.18 * bill) + (0.015 * bill)

if(100<bill<500):
    print("Your Bill Is : ", bill +x)
elif(500<bill<1000):
    print("Your Bill is : ", bill + y)
elif(1000<bill<2000):
    print("Your Bill is : ", bill + z)
elif(2000<bill<3000):
    print("your bill is : ",bill + w )
else:
    print("your bill is : ", bill)