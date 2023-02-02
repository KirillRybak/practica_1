import math
def kru(r):
    p = math.pi
    S = p * r**2
    return S
def pry(a,b):
    S = a*b
    return S
def tre(a,h):
    S = (0.5 * a) * h
    return S
x= int(input("Введите площадь какой фигуры вы хотите найти (число): \n1)Круг\n2)Прямоугольник\n3)Треугольник\n| "))
if x==1:
    r = int(input("Введите радиус окружности : "))
    print(round(kru(r), 1))

elif x==2:
    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    print(round(pry(a,b), 1))
elif x==3:
    a = int(input("Введите длину основание треугольника: "))
    h = int(input("Введите высоту треугольника: "))
    print(tre(a,h))