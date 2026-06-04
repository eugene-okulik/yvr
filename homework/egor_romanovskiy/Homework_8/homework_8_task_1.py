import random

salary = int(input('Введите свою зарплату в долларах: '))
bonus = bool(random.randint(0, 1))


def get_amount_of_salary_with_bonus(user_salary, apply_bonus):
    if apply_bonus:
        bonus_rate = 1 + random.random()
    else:
        bonus_rate = 1
    return f"{user_salary}, {apply_bonus} - '${int(user_salary * bonus_rate)}'"


print(get_amount_of_salary_with_bonus(salary, bonus))
