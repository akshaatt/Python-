h_feet = int(input("Enter Feets in your Height : "))
h_inch =  int(input("Enter Inches in your height : "))
h_meter = (h_feet * 0.30) + (h_inch * 0.0252)
wght = int(input("Enter Your Weight in Kgs : "))
bmi = (wght/(h_meter)*(h_meter))
if(bmi < 15):
    print("You Are Damn Underweight")
elif(bmi < 16):
    print("You Are Very Under Wwight")
elif(bmi < 18.5):
    print("Underweight")
elif(bmi < 23):
    print("U Are Fit")
elif(bmi > 23):
    print("U are an Elephant")

