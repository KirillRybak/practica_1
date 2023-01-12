try:
    f = 1
    i = 1
    n = int(input("Введите число, факториал которого найти: "))
    while i <= n:
        f *= i
        i += 1
    print(f)
except:
    print("Упс, что то пошло не так")





