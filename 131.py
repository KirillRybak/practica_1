
class Objects:
    def __init__(self,Obj1,Obj2,Obj3,Obj4,Obj5):
        self.Obj1 = str(Obj1)
        self.Obj2 = str(Obj2)
        self.Obj3 = str(Obj3)
        self.Obj4 = str(Obj4)
        self.Obj5 = str(Obj5)
    def object(self):
        print("Объект 1: " + self.Obj1 + "\n" + "Объект 2: " + self.Obj2 + "\n" + "Объект 3: " + self.Obj3 + "\n" + "Объект 4: " + self.Obj4 + "\n" + "Объект 5: " + self.Obj5)

Proj = Objects("Kirill",22,3.45,True,None)
Proj.object()