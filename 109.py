try:
    a = int(input("Введите число, кратное которому хотите найти числа до 10000 "))
    for i in range(10000):
        if i%a==0:
            print(i)
except:
    print("Упс, что то пошло не так")