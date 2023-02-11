class animal:
    def __init__(self,animal):
        self.animal = animal

    def _leo(self):
        print("Привет, я " + self.animal)
    def _spe(self,speed):
        print("Могу разогнаться до " + str(speed) + " км/ч")
animal1 = animal("Леопард")
animal1._leo()

obj1 = animal("loo")





