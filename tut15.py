# a = 15
# b = 20
# print(a+b)

# ----------------------------------------------------------------------------------------------------------------
# Exercize 3

num = 18

print("Welcome to The game \n")
print("\n Guess The correct number for which you have 10 trials")
i = 1

while(i <= 10):
    print("Enter the", [i], "number \n")
    x = int(input())
    if (x > num):
        print("Enter The Smaller Number \n")
    elif (x < num):
        print("Enter The Grater Number \n")
    elif (x == num):
        print("You Got it. GAME ENDS \n")
        break  

    i = i+1
if(x != 18):
    print("YOU LOST GAME END")

