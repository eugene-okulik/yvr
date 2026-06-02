import sys


def generate_fibonachi_row(limit=10):
    num_1 = 0
    num_2 = 1
    count = 0
    while count < limit:
        yield num_1
        num_2 += num_1
        num_1 = num_2 - num_1
        count += 1


def get_number_by_position_from_fibonachi(position):
    count = 1
    for number in generate_fibonachi_row(position):
        if count == position:
            print(number)
            break
        count += 1


sys.set_int_max_str_digits(50000)

get_number_by_position_from_fibonachi(5)
get_number_by_position_from_fibonachi(200)
get_number_by_position_from_fibonachi(1000)
get_number_by_position_from_fibonachi(100000)
