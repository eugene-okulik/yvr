import datetime

# Преобразуйте эту дату в питоновский формат:
date = "Jan 15, 2023 - 12:05:33"
py_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')

# 1. Распечатайте полное название месяца из этой даты
print(py_date.strftime('%B'))

# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
print(py_date.strftime('%d.%m.%Y, %H:%M'))
