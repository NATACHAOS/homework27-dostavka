print("Расчёт стоимости доставки")
price = 50
price_for_10 = 200
weight = int(input("Напишите вес посылки: "))
if weight <= 2:
    print('Стоимость составляет:', price, 'рублей')
if weight in range(3, 11):
    price_dop = 0
    for i in range(len(weight)):
        price_dop += 20
    print('Стоимость составляет:', price + (i), 'рублей')
    print(price_dop)
if weight > 11:
    print('Стоимость составляет:', price_for_10, 'рублей')
