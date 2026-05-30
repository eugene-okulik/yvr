def compare_user_input_with_number(user_input, num):
    while user_input != num:
        user_input = int(input("Попробуйте снова: "))
    print('Поздравляю! Вы угадали!')


input_number = int(input('Угадайте цифру от 0 до 9: '))
stored_number = 4
compare_user_input_with_number(input_number, stored_number)
