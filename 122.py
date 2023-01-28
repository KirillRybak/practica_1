f = open("example.txt","w")
f.writelines(["Wesley Hubbard ","4\n"])
f.writelines(["Brian Franklin ","1\n"])
f.writelines(["Anthony Hensley ","2\n"])
f.writelines(["Leslie Miles ","5\n"])
f.writelines(["Brice Flynn ","5"])
f.close()
with open("example.txt",'r') as f:
    x = 0
    for i in f:
        i = i.split()
        for j in i:
            if j.isdigit()==True:
                x += int(j)
                if int(j)<3:
                    print(list(i))
    print(x/5)



