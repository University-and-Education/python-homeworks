def homework_first():
    list_for_return = []
    input_data = input('Введите значение: ')
    while len(input_data) != 0:
        list_for_return.append(input_data)
        input_data = input('Введите значение: ')
    return list_for_return


def homework_second(number):
    if number > 12 or number < 1:
        print("Введено некорректное значение")
    elif number <= 2 or number == 12:
        print('Зима')
    elif 2 < number <= 5:
        print('Весна')
    elif 5 < number <= 8:
        print('Лето')
    elif 8 < number <= 11:
        print('Осень')


def homework_third(n):
    if n < 1:
        print("Введено некорректное значение")
        exit(0)

    fib1 = fib2 = 1

    print(fib1, fib2, end=' ')

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


def homework_fourth():
    list_for_input = []
    value_with_count = dict()
    input_for_list = input('Введите значение: ')
    while len(input_for_list) > 0:
        list_for_input.append(input_for_list)
        input_for_list = input('Введите значение: ')
    for i in list_for_input:
        key_exists = i in value_with_count
        if not key_exists:
            new_data = {i: 1}
            value_with_count.update(new_data)
        else:
            new_data = {i: value_with_count.get(i) + 1}
            value_with_count.update(new_data)
    print(value_with_count)


def homework_fifth(n):
    print(sum(n) / len(n))


def homework_sixth(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def homework_seventh(n):
    long_word = max(n, key=len)
    often_word = the_most_often_word(n)
    print(long_word + ' ' + often_word)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def str_to_int(number):
    if is_int(number):
        return int(number)
    else:
        print("Введено некорректное значение")
        exit(0)


def the_most_often_word(lst):
    elems = {}
    e, em = None, 0
    for i in lst:
        elems[i] = t = elems.get(i, 0) + 1
        if t > em:
            e, em = i, t
        return e

# Задание 1
# print(homework_first())

# Задание 2
# homework_second(str_to_int(input('Введите значение: ')))

# Задание 3
# homework_third(str_to_int(input('Введите значение: ')))

# Задание 4
# homework_fourth()

# Задание 5
# list_for_input = []
# input_for_list = input('Введите значение: ')
# while len(input_for_list) > 0:
#     number = str_to_int(input_for_list)
#     list_for_input.append(number)
#     input_for_list = input('Введите значение: ')
# homework_fifth(list_for_input)

# Задание 6
# print(homework_sixth(str_to_int(input('Введите значение: '))))

# Задание 7
# list_for_input = []
# input_for_list = input('Введите значение: ')
# while len(input_for_list) > 0:
#     list_for_input.append(input_for_list)
#     input_for_list = input('Введите значение: ')
# homework_seventh(list_for_input)
