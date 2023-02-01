def num(n):
    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i

m = abs(int(input('Введите число: ')))
print('Количество разрядов:', num(m))