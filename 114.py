from random import randint
N = 15
a = [randint(-150,150) for j in range(N)]
p = len(a)
print(a)
b = int(input("Введите нижний порог: "))
c = int(input("Введите верхний порог: "))
i=0
while i < len(a):
    if b < a[i] < c:
        del a[i]
    else:
        i+=1
while p>len(a):
    a.append(0)
print(a)