n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов:"))
listA = []
for i in range(n):
    listB = []
    for j in range(m):
        a = int(input())
        listB.append(a)
    listA.append(listB)
for i in listA:
    print(i)
