def read_user_input():
    first_num = int(input('Введите первое целое число: '))
    second_num = int(input('Введите второе целое число: '))
    return first_num, second_num


def decorator(func):
    def wrapper(n1, n2):
        if n1 < 0 or n2 < 0:
            operation = '*'
        elif n1 == n2:
            operation = '+'
        elif n1 > n2:
            operation = '-'
        else:
            operation = '/'
        return func(n1, n2, operation)

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


num1, num2 = read_user_input()
print(calc(num1, num2))
