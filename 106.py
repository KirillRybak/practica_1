print("Для выхода нажмите Y")
while True:
    data = input("Введите сумму для обмена: ")
    if data.lower()=="y":
        break
    money = int(data)
    if money < 0:
        print("Сумма должна быть положительной")
        continue
    cache = round(money/2.64)
    print("К выдаче", cache,"долларов")
print("Работа обменного пункта завершена")