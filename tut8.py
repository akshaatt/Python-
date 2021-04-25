#    # IF else statement

# var1 = "Akshat"
# var2 = "Riya"

# var3 = input()

# if var3 == "Akshat":
#     print("He IS A GOOD BOY")

# else: 
#     print("maa chuda na bhai")

# var1 = 56
# var2 = 6

# var3 = int(input())

# if var3>var2:
#     print("Entered value is grater than 6")
    
# else:
#      print("SUCK MY")

print("Please Enter the Age = ")
age = int(input())

if age < 3:
    print("Please Grow Up")
elif 3 < age < 18:
    print("Sorry You cannot Drive")
elif 18 < age < 88:
    print("Surely You Can drive" )
elif age == 18:
    print("We cant decide please come up rto office")
elif age == 3:
    print("Try One year later")
else:
    print("You are too old to drive SORRY")