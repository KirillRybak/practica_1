from abc import abstractmethod
class Animal:
    def __init__(self):
        pass
    def ves(self,x):
        pass
    def speed(self,x):
        pass
    def Coloring(self,x):
        pass

class Kat(Animal):
    def __init__(self,animal = "Кот"):
        self.animal = animal
    def ver(self,x):
        print(self.animal + " имеет вес " + str(x) + ' kg')
    def speed(self,x):
        print("Скорость: " + str(x))
    def Coloring(self,x):
        print('Раскраска: ' + str(x))
kat = Kat()
kat.Coloring('black')
kat.speed(48)
kat.ver(7.5)
