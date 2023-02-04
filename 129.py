def summ(n, s=0):
    if not n:
        return s
    else:
        s += n % 10
        n //= 10
        return summ(n, s)
n = int(input("Введите число: "))
print(summ(n))
