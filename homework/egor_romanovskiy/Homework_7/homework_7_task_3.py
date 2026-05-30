def get_number_from_text(text):
    print(int(text.split(': ')[-1]) + 10)


program_output = 'результат операции: 42'
get_number_from_text(program_output)

program_output = 'результат операции: 54'
get_number_from_text(program_output)

program_output = 'результат работы программы: 209'
get_number_from_text(program_output)

program_output = 'результат: 2'
get_number_from_text(program_output)
