import datetime
import os


current_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(current_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(file):
    with open(file, 'r', encoding='utf-8') as test_file:
        for data_line in test_file.readlines():
            yield data_line


for line in read_file(file_path):
    data = line.rsplit(' -')[0]
    if data[0] == '1':
        date_1 = datetime.datetime.strptime(data[3:], "%Y-%m-%d %H:%M:%S.%f")
        print(date_1 + datetime.timedelta(weeks=1))
    elif data[0] == '2':
        date_2 = datetime.datetime.strptime(data[3:], "%Y-%m-%d %H:%M:%S.%f")
        print(date_2.strftime('%A'))
    else:
        date_3 = datetime.datetime.strptime(data[3:], "%Y-%m-%d %H:%M:%S.%f")
        current_datetime = datetime.datetime.now()
        print((current_datetime - date_3).days)
