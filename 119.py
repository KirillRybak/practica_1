n = int(input("Введите кол-во множеств: "))
i = 3
x = []
while i<n:
    i += 1
    m = {"пусто"}
    if i%3==0 and m:
        m = str(i)+str({"пусто"})
        print(m)
