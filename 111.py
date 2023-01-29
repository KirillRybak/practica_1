try:
    a = [int(i) for i in input("Заполните список (через пробел): ").split()]
    s = 0
    for i in range(len(a)):
        if a[i] % 2 == 0 and a[i] > 0:
            s += a[i]
    print(s)
except:
    print("оп")
