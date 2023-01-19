s = input("Введите строку:")
c = []
for i in range(len(s)):
    if s[i] not in c:
        c += s[i]
c = tuple(c)
print(c)