class animal:
    def __init__(self,animal):
        self.animal = animal

    def leo(self):
        print("Привет, я " + self.animal)
    def _spe(self,speed):
        print("Могу разогнаться до " + str(speed) + " км/ч")
    def _Weight(self,x = 7.5):
        print("Мой вес " + str(x) + " кг")


class lep(animal):
    def __init__(self,animal = "Кошка"):
        super().__init__(animal)


    def leo(self):
        print("(Изменено) Привет, я " + self.animal)
    def _spe(self,speed = 48):
        print("Могу разогнаться до " + str(speed) + " км/ч")
    def color(self,col = "чёрная"):
        print("Имеет расскраску: " + col)

    def bob(self):
        print ("Всё работает")

    def lov(self):
        print("Мне нравиться ", self.animal)
obj1 = lep()
obj1.leo()
obj1._spe()
obj2 = animal("Панда")
obj2.leo()


