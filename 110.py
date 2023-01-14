min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))
x = 0

for i in range(min+1, max):
    x += i
print(x)
