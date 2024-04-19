print("Расчёт стоимости доставки")
price = 50
price_for_10 = 200
weight = int(input("Напишите вес посылки в кг и нажмите Enter: "))
if weight <= 2:
    print('Стоимость составляет:', price, 'рублей')
if 2 < weight <= 10:
    price = 50 + 20 * (weight - 2)
    print('Стоимость составляет:', round(price, 2), 'рублей')
if weight > 10:
    print('Стоимость составляет:', price_for_10, 'рублей')
