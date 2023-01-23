from random import randint

n = int(input("n="))

sets = [None]

for i in range(1, n + 1):
    t = []
    for _ in range(10):
        t.append(randint(-10, 10))
    sets.append(set(t))

print("Исходные множества:")
for i in range(1, n + 1):
    print(i, ":", *sets[i])

res = sets[3]
i = 6
while i <= n:
    res = res & sets[i]
    i += 3
res = res - sets[1]
print("Результат:")
print(*res)


