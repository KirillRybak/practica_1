try:
    a = [int(i) for i in input("Заполните список (через пробел): ").split()]
    x = min(a)
    print(x, end=" | ")
    a.remove(x)
    c = min(a)
    print(c)
    a.remove(c)
except:
    print("Упс, что то пошло не так")