number1 = int(input("Введите число: "))
number2 = 0
while number1 > 0:
    x = number1%10
    number1 = number1//10
    number2 = number2 * 10 + x
print(number2)




