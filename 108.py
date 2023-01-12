try:
    i = 1
    f =1
    n = int(input("Введите число, факториал которого найти:  "))
    while i<=n:
        f = f*i
        i = i+1
    print(f)
except:
    print("Упс, что то пошло не так")

