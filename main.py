# # Домашнее задание по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='URBAN', c=True):
    print(a, b, c)
# Вызовы функции с различным количеством аргументов
print_params()  # вызов без аргументов
print_params(10)  # только один аргумент
print_params(10, 'Vitali')  # два аргумента
print_params(10, 'Python', False)  # три аргумента

# Проверка вызовов с именованными аргументами
print_params(b=25)
print_params(c=[1, 2, 3])

#Создадим список и словарь, а затем передадим их в функцию с помощью распаковки.

# Создание списка и словаря
values_list = [42, 'example', False]
values_dict = {'a': 3.14, 'b': 'hello', 'c': False}

# Распаковка списка и словаря в функцию
print_params(*values_list)
print_params(**values_dict)


