class Flower:
    def __init__(self, name, price, length, color, quantity, lifetime):
        self.name = name
        self.price = price
        self.length = length
        self.color = color
        self.quantity = quantity
        self.lifetime = lifetime

    def get_info(self):
        print(f'Название: {self.name}, цена: {self.price} руб, длина: {self.length} см, цвет: {self.color}, '
              f'количество: {self.quantity} шт, время жизни: {self.lifetime} дней')

    def set_price(self, price):
        self.price = price

    def reduce_quantity_by(self, number):
        self.quantity = self.quantity - number


class Rose(Flower):
    def __init__(self, name, price, length, color, quantity, lifetime, has_thorns, variety):
        super().__init__(name, price, length, color, quantity, lifetime)
        self.has_thorns = has_thorns
        self.variety = variety

    def get_info(self):
        thorns = 'да' if self.has_thorns else 'нет'
        super().get_info()
        print(f'Шипы: {thorns}, сорт: {self.variety}')


class Tulip(Flower):
    def __init__(self, name, price, length, color, quantity, lifetime, texture, has_fringe):
        super().__init__(name, price, length, color, quantity, lifetime)
        self.texture = texture
        self.has_fringe = has_fringe

    def get_info(self):
        fringe = 'да' if self.has_fringe else 'нет'
        super().get_info()
        print(f'Текстура: {self.texture}, бахрома: {fringe}')


class Lily(Flower):
    def __init__(self, name, price, length, color, quantity, lifetime, number_of_petals):
        super().__init__(name, price, length, color, quantity, lifetime)
        self.number_of_petals = number_of_petals

    def get_info(self):
        super().get_info()
        print(f'Количество лепестков: {self.number_of_petals}')


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_info(self):
        for flower in self.flowers:
            flower.get_info()

    def calculate_price(self):
        price = 0
        for flower in self.flowers:
            price += flower.price
        return price

    def avg_lifetime(self):
        count = 0
        lifetime = 0
        for flower in self.flowers:
            count += 1
            lifetime += flower.lifetime
        return lifetime / count

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.lifetime)

    def sort_by_length(self):
        self.flowers.sort(key=lambda flower: flower.length)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def find_flower_by_color(self, color):
        for flower in self.flowers:
            if flower.color == color:
                print(flower.name)


red_rose = Rose('Красная Кристина', 30, 80, 'Бордовый', 50, 10,
                True, 'Кусторвая')
juliet = Rose('Джульетта', 15, 80, 'Персиковый', 50, 10,
                          True, 'Кусторвая')
peach_tulip = Tulip('Пионовидный', 5, 45, 'Розовый', 123, 6,
                          'Гладкий', False)
stargazer = Lily('Stargazer', 15, 30, 'Белый', 20, 20, 3)
lollipop = Lily('Lollipop', 15, 30, 'Розовый', 20, 20, 3)


red_rose.get_info()
juliet.get_info()
peach_tulip.get_info()
stargazer.get_info()
lollipop.get_info()

birthday_bouquet = Bouquet([red_rose, juliet, stargazer])
