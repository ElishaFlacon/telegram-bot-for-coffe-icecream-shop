from data import *


# Получаем цену заказа, который Создается
# ТУТ ТАКОЕ ГОВНИЩЕ, ФУ СМЕРДИТ, зато работает XD
def get_order_price(num_order):
    try:
        max_rw_products = PRODUCTS_SHEET.max_row
        max_rw_orders = ORDERS_SHEET.max_row
        check_additions = 0
        order_price = 0
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
                # Пробел в сплите, после ; нужен, просто необходим, наверно))
                # [:-1] нужен, зачем? а потому что в конце массива появлялась пустая строка
                # через иф не убиралась, так что вырежем так))
                for j in ORDERS_SHEET[f'G{i+1}'].value.split('; ')[:-1]:
                    for l in range(max_rw_products):
                        # Тут проверка на продукт и вкус
                        if j.lower().find(str(PRODUCTS_SHEET[f'A{l+1}'].value)) == 0:
                            a = PRODUCTS_SHEET[f'B{l+1}'].value
                            order_price += float(a)
                        # А тут проверка на посыпку и топинг
                        # >=5 потому что да
                        # А вообще функция финд находит кол-во символов до указанного символа
                        # И соответственно возвращает их
                        # А до + который является началом для посыпок достаточно далеко, а топинг еще дальше
                        # Но минимально лучше оставить 5
                        elif j.lower().find(str(PRODUCTS_SHEET[f'A{l+1}'].value)) >= 5:
                            for i in j.lower().split():
                                if i.find('+') >= 0:
                                    # Проверка нужна, потому что первая посыпка бесплатная
                                    if check_additions == 1:
                                        # Тут мне было в падлу нормально делать поиск по +
                                        #  Плюс у нас это топинг, вот
                                        #  Так что столбец у нас, такой, константа
                                        # Ну и там ниже так же
                                        b = PRODUCTS_SHEET[f'B{2}'].value
                                        order_price += float(b)
                                    check_additions = 1
                                # Топинг хоть и бесплатный, но а вдруг... все бывает))
                                elif i.find('=') >= 0:
                                    b = PRODUCTS_SHEET[f'B{3}'].value
                                    order_price += float(b)
        return float(order_price)
    except Exception as e:
        print(f'price Строка №47 - {e}')


# Загружаем цену в БД
def load_order_price(price, num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Создается':
                ORDERS_SHEET[f'D{i+1}'] = float(price)
        save_data()
    except Exception as e:
        print(f'price Строка №59 - {e}')


# Получаем способ оплаты
def get_payment_method(num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
                if str(ORDERS_SHEET[f'E{i+1}'].value) == 'КАРТА':
                    return True
                elif str(ORDERS_SHEET[f'E{i+1}'].value) == 'НАЛИЧНЫЕ':
                    return False
    except Exception as e:
        print(f'price Строка №73 - {e}')


# Получаем способ оплаты в виде текста
def get_payment_method_with_text(num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
                if str(ORDERS_SHEET[f'E{i+1}'].value) == 'КАРТА':
                    return 'Карта'
                elif str(ORDERS_SHEET[f'E{i+1}'].value) == 'НАЛИЧНЫЕ':
                    return 'Наличные'
    except Exception as e:
        print(f'price Строка №87 - {e}')


# Загружаем способ оплаты в БД
def load_payment_method(card, num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Создается':
                if bool(card) == True:
                    ORDERS_SHEET[f'E{i+1}'] = "КАРТА"
                elif bool(card) == False:
                    ORDERS_SHEET[f'E{i+1}'] = "НАЛИЧНЫЕ"
        save_data()
    except Exception as e:
        print(f'price Строка №102 - {e}')


# Тут лучше бы сделать еще одну функцию и получать цену из БД, а не расчитывать ее заново, через первую функцию
# Но это же сделано для небольшого кол-во пользователей, там даже по максимуму брать 20 продавцов 5 админов
# Так что система не ляжет, у меня вообще один из первых вк ботов имел тайм.слип, он там картинку с погодой прогружал
# (библиотека была без всяких авейтов ваших), вопросы?
