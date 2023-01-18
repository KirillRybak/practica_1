from random import random
N = int(input("Введите кол-во строк и столбцов: "))
a = []
x = 0
for i in range(N):
    z = []
    for j in range(N):
        n = int(random() * 100) - 50
        z.append(n)
        print("%4d" % n, end='')
        if n < 0:
            x += 1
    print()
    a.append(z)




print("___________")
print("Отрицательных чисел под главной диагональю: ", x )





