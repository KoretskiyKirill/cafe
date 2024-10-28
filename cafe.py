name = input("введите имя: ")
menu = {
    "Кофе": 100,
    "Чай": 50,
    "Пирожок": 75,
    "Сэндвич": 150,
    "Сок": 120
}
print(menu)
eat = []
summa = 0
sht = []
stop = ''
while stop != 'нет':
    eat.append(input("введите блюдо: "))


    sht.append(int(input("введите кол-во: ")))
    stop = input('продолжить?: ')
def decor(func):
    pay = input("способ оплаты: ")
    print('=' * 12)
    print(f"Ваш чек господин {name}:")
    global summa
    global eat
    for i in range(len(eat)):
        if eat[i] == "Кофе":
            rub = 100
        elif eat[i] == "Чай":
            rub = 50
        elif eat[i] == "Пирожок":
            rub = 75
        elif eat[i] == "Сендвич":
            rub = 150
        elif eat[i] == "Сок":
            rub = 120

        print(f"{eat[i]} : {rub} руб {sht[i]}х")
        summa = summa + rub
    print(f"Итого к оплате: {summa} руб.")
    if pay == 'наличные':
        func()
    print('=' * 12)


@decor
def ceck():
    nall = int(input("введите сколько рублей"))

    print(f"Внесено: {nall} руб.")
    print(f"Сдача: {nall - summa} руб.")
