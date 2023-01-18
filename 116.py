from random import random
N = int(input("Введите кол-во строк и столбцов: "))
a = []
b = 0
for i in range(N):
    z = []
    for j in range(N):
        n = int(random() * 100) - 50
        z.append(n)
        print("%4d" % n, end='')
    print()
    a.append(z)
print()

for i in range(N):
    if a[i][i] > 0:
        b += 1
print()
print(b)





