'''age = int(input("Enter Your Age : "))
if age >= 24 :
    print("You are Not Elligible for Exam")
else:
    print("Sure! You can Appear for The Exam")
'''
#-----------------------------------------------------------------
'''
userName = input("Enter The User Name : ")
if userName == "akshat_0017" :
    password = input(" Enter Your Password : ")
    if password == "py123" :
        print("Congrats You Have Logged IN")
    else:
        print("Wrong Password")
else:
    print("Wrong Username Try Again Idiot")
'''

#-----------------------------------------------------------------


username = input("Enter the username please : ")
passw = input("Enter the Password : ")
if(username == "akshat112" and passw == "candoit12"):
    print("LOGGED IN SUCCESSFULLY")
elif(username != "akshat112" and passw == "candoit12"):
     print("Wrong Username please check")
elif(username == "akshat112" and passw != "candoit12"):
     print("Wrong password please check")
elif(username != "akshat112" and passw != "candoit12"):
     print("Wrong password and username please check")
else:
    print("wrong")

