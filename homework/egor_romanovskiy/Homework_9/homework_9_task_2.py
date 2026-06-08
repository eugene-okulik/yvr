temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]
hot_days = list(filter(lambda temperature: temperature > 28, temperatures))
print(f'Самая высокая температура в жаркие дни: {max(hot_days)}')
print(f'Самая низкая температура в жаркие дни: {min(hot_days)}')
print(f'Средняя температура в жаркие дни: {round(sum(hot_days) / len(hot_days), 2)}')
