name = input("Введите имя: ")
def fan(func):
    def winner(x):
        print("Вообще без понятия, как это делать")
        func(x)
        return func(x.upper())
    return winner
@fan
def hello(name):

    x = "Hello, " + name

    return print(x)
fan(hello(name))



