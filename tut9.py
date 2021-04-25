                    # Faulty Calculaator

print("KINDLY ENTER THE OPERATOR FROM  +, -, *, /")
operator = int(input)
print("Enter The First Number")
firstNumber = int(input)
print("Enter Second Number")
secondNumber = int(input)

answer = firstNumber operator secondNumber

if answer == 45 * 3:
    answer =555
    print(answer)
elif answer == 56 + 9:
    answer = 77
    print(answer)
elif answer == 56 / 6:
    answer = 4
    print(answer)
else:
    print(answer)