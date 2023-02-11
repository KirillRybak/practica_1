from work_ import animal
class lep(animal):
    def __init__(self,animal):
        super().__init__(animal)

    def color(self,col):
        print("Имеет расскраску: " + col)

    def bob(self):
        print ("Всё работает")

    def lov(self):
        print("Мне нравиться ", self.animal)

prim1 = lep("Леопард")
prim1._leo()

prim1._spe(58)
prim1.color("оранжувую")
prim1.bob()
prim1.lov()
prim2 = animal("Пингвин")
prim2._leo()