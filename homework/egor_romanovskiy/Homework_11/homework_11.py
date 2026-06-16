class Book:
    material = 'бумага'
    has_text = True
    is_booked = False

    def __init__(self, title, author, pages, ISBN):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN

    def get_info(self):
        if self.is_booked:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}, '
                  f'зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}')

    def set_is_booked(self, booked):
        self.is_booked = booked


class SchoolBook(Book):
    has_hometask = True

    def __init__(self, title, author, pages, ISBN, subject, class_num):
        super().__init__(title, author, pages, ISBN)
        self.subject = subject
        self.class_num = class_num

    def get_school_book_info(self):
        if self.is_booked:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                  f'класс: {self.class_num}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                  f'класс: {self.class_num}')


book_1 = Book('Эхо забытых снов', 'Анна Ветрова', 342, '978-5-16-123456-7')
book_1.set_is_booked(True)
book_1.get_info()

book_2 = Book('Границы бесконечности', 'Дэн Симмонс', 612, '978-1-56619-789-0')
book_2.set_is_booked(False)
book_2.get_info()

book_3 = Book('Чайный дом на окраине', 'Харуки Мураками', 288, '978-4-06-543210-8')
book_3.set_is_booked(False)
book_3.get_info()

book_4 = Book('Механика гнева', 'Алексей Пехов', 480, '978-5-17-987654-3')
book_4.set_is_booked(False)
book_4.get_info()

book_5 = Book('Тишина между строк', 'Джоан Роулинг', 527, '978-0-316-00123-4')
book_5.set_is_booked(False)
book_5.get_info()

class_book_1 = SchoolBook('История Средних веков', 'Василий Пупкин', 120, '978-0-316-00123-5', 'История', '9')
class_book_1.set_is_booked(True)
class_book_1.get_school_book_info()

class_book_2 = SchoolBook('Геометрия', 'Александр Иванов', 100, '978-0-316-00123-6', 'history', '11')
class_book_2.set_is_booked(False)
class_book_2.get_school_book_info()
