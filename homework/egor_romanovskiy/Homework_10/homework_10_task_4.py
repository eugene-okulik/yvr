PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = [item.split() for item in PRICE_LIST.split('\n')]
my_dict = {key: int(value.rstrip('р')) for key, value in my_list}
