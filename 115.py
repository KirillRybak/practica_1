n = int(input("Введите кол-во строк и столбцов: "))
m = int(input("Введите кол-во столбцов: "))
listA = []
for i in range(n):
    listB = []
    for j in range(m):
        a = int(input())
        listB.append(a)
    listA.append(listB)
for i in listA:
    print(i)
max_,k = listA[0][0],0
for q in range(len(listA)):
    if listA[q][k] > max_:
        max_ = listA[q][k]
    k += 1
print(max_)


