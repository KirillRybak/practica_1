from random import randint

def hello(n,m):
    n = int(input("Введите минимальное значение: "))
    m = int(input("Введите максимальное значение: "))
    b = int(input("Введите кол-во значений в массиве: "))
    x =[randint(n,m) for i in range(b)]
    print(x)
hello(-10,10)



