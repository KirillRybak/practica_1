nfile = input("Заголовок ")
f = open(nfile,"w",encoding='utf-8')
i = 0
while True:
    n = input()
    m = n.split()
    if n == "":
        break
    i += 1
    f.write(n+"\n")
    print("Символы: ",len(n))
    print("Слова: ",len(m))


print("Кол-во строк", i)
f.close()





