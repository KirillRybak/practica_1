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
prim1.leo()
prim1.Weight(50)
prim1.spe(58)
prim1.color("оранжувую")
prim1.bob()
prim1.lov()
prim2 = lep("Пингвин")
prim2.bob()eo()