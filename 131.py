
class Objects:
    def __init__(self,Obj1,Obj2):
        self.Obj1 = str(Obj1)
        self.Obj2 = str(Obj2)

    def object(self):
        print("Имя: " + self.Obj1 + "\n" + "Возраст: " + self.Obj2 + "\n")

Proj1 = Objects("Kirill",22)
Proj2 = Objects("Василий",43)
Proj3 = Objects("Никита",18)
Proj4 = Objects("Ника", 20)
Proj5 = Objects("Яна", 27)
Proj5.object()
Proj4.object()
Proj3.object()
Proj2.object()
Proj1.object()


