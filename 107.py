n1 = 1
n2 = 2

n = int(input("Введите число элементов ряда Фибоначчи: "))
print(n1 , n2 , end=" ")
while n > 2:
    n1, n2 = n2, n1 + n2
    n -= 1
    print(n2, end=" ")