from random import randint

n = int(input("Введите минимальное значение: "))
m = int(input("Введите максимальное значение: "))
def hello(n,m):

    b = int(input("Введите кол-во значений в массиве: "))
    x =[randint(n,m) for i in range(b)]
    print(x)
hello(n,m)
