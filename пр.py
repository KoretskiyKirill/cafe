name = input("введите имя")
menu = {
    "Кофе": 100,
    "Чай": 50,
    "Пирожок": 75,
    "Сэндвич": 150,
    "Сок": 120
}
print(menu)
summa = 0
def decor(fuc):
    eat = ''
    print('=' * 12)
    print(f"Ваш чек господин {name}:")
    global summa
    while eat != 'стоп':
        eat = input("введите блюдо")
        if eat == "Кофе":
            rub = 100
        elif eat == "Чай":
            rub = 50
        elif eat == "Пирожок":
            rub = 75
        elif eat == "Сендвич":
            rub = 150
        elif eat == "Сок":
            rub = 120
        sht = int(input("введите кол-во"))
        print(f"{eat} : {rub} руб {sht}х")
        summa = summa + rub
    pay = input("способ оплаты")
    if pay == 'наличными':
        fuc()
    print('=' * 12)


@decor
def ceck():
    nall = int(input("введите сколько рублей"))
    print(f"Итого к оплате: {summa} руб.")
    print(f"Внесено: {nall} руб.")
    print(f"Сдача: {nall - summa} руб.")
