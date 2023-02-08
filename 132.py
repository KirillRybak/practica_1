class animal:
    def __init__(self,animal):
        self.animal = animal

    def leo(self):
        print("Привет, я " + self.animal)
    def spe(self,speed):
        print("могу разогнаться до " + str(speed) + " км/ч")
    def Weight(self,x):
        print("Мой вес " + str(x))


animal1 = animal("Леопард")
animal1.leo()
animal1.spe(99)
animal1.Weight(31)
