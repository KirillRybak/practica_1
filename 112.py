
try:
    import statistics
    a = [int(i) for i in input("Заполните список (через пробел): ").split()]
    n = statistics.mean(a)
    for z in range(a[0], len(a), 1):
        if z<n:
            print(z, end=" | ")
except:
    print("Упс, что то пошло не так")
