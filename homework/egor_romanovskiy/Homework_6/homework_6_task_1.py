# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
list_from_text = text.split(' ')
new_list = []
ending = 'ing'
for word in list_from_text:
    last_symbol = word[-1]
    if last_symbol not in ('.', ','):
        word = word + 'ing'
    else:
        word = word.replace(last_symbol, ending + last_symbol)
    new_list.append(word)
print(' '.join(new_list))
