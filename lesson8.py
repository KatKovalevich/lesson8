# задача 1

class MyData:
    def __init__(self, date):
        self.date = date.split('-')
    @classmethod
    def date_to_int(cls, obj):
        return obj.date.split('-')

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Дата введена верно!'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

# задача 2

class Div_by_zero(Exception):
    def division_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> на ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")

# задача 3

class StopError(Exception):
    def __init__(self, my_list):
        self.my_list = my_list
        while True:
            try:
                my_list = input('Введите число в список:')
                for el in my_list:
                    if type(el) == str:
                        raise StopError("в списке присутствует элемент типа данных <<str>>: ")
            except StopError as err:
                print(err, el)

# задача 4,5,6

class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

        def income(self):
            try:
                name = input(f'Введите наименование: ')
                price = int(input(f'Введите цену за единицу: '))
                quantity = int(input(f'Введите количество: '))
                item = {'Модель устройства': name, 'Цена за единицу': price, 'Количество': quantity}
                self.items.update(item)
                print(self.items)
            except ValueError:
                print('Недопустимое значение!')

class Printer(OfficeEquipment):
        pass

class Scanner(OfficeEquipment):
        pass

class Xerox(OfficeEquipment):
        pass



# задача 7
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'