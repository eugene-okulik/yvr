# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.
result_str = 'результат операции: 42'
start_index = result_str.index(': ') + 2
num = int(result_str[start_index:])
print(num + 10)

result_str = 'результат операции: 514'
start_index = result_str.index(': ') + 2
num = int(result_str[start_index:])
print(num + 10)

result_str = 'результат работы программы: 9'
start_index = result_str.index(': ') + 2
num = int(result_str[start_index:])
print(num + 10)
