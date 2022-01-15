def homework_first(input_data):
    list_for_return = []
    for i in input_data:
        if i.strip():
            list_for_return.append(i)
        else:
            return list_for_return
    return list_for_return


def homework_second(number):
    if number > 12 or number < 1:
        return ValueError
    elif number <= 2 or number == 12:
        return 'Зима'
    elif 2 < number <= 5:
        return 'Весна'
    elif 5 < number <= 8:
        return 'Лето'
    elif 8 < number <= 11:
        return 'Осень'


def homework_third(n):
    if n < 1:
        return ValueError

    fib1 = fib2 = 1

    value = str(fib1) + ' ' + str(fib2)

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        value += ' ' + str(fib2)
    return value


def homework_fourth(input_for_list):
    list_for_input = []
    value_with_count = dict()

    for i in input_for_list:
        if i:
            list_for_input.append(i)

    for i in list_for_input:
        key_exists = i in value_with_count
        if not key_exists:
            new_data = {i: 1}
            value_with_count.update(new_data)
        else:
            new_data = {i: value_with_count.get(i) + 1}
            value_with_count.update(new_data)
    return value_with_count


def homework_fifth(n):
    return sum(n) / len(n)


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
    return [long_word, often_word]


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
