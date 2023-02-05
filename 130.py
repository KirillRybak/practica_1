def fan(func):
    def winner():
        print("Вообще без понятия, как это делать")
        func()
    return winner
@fan
def hello():
    name = input("Введите имя: ")
    x = "Hello, " + name
    x1 = x.upper()
    return print(x,x1)

fan(hello)

