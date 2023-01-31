from random import randint

n = int(input("Введите минимальное значение: "))
m = int(input("Введите максимальное значение: "))
def hello(n,m):


    x =[randint(n,m) for i in range(15)]

    print(x)
hello(n,m)
