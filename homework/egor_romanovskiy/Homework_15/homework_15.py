import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создайте студента (student)
query = '''
INSERT INTO students (name, second_name, group_id)
VALUES (%s, %s, %s)'''
values = ('Firstname', 'Lastname', None)
cursor.execute(query, values)
student_id = cursor.lastrowid
db.commit()

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
query = '''
INSERT INTO books (title, taken_by_student_id)
VALUES(%s, %s)'''
values = [
    ('my_book_1', student_id),
    ('my_book_2', student_id)
]
cursor.executemany(query, values)
db.commit()

# Создайте группу (group) и определите своего студента туда
query = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
'''
values = ('Group102', '2024-09-01', '2025-06-30')
cursor.execute(query, values)
group_id = cursor.lastrowid
db.commit()

query = '''
UPDATE students
SET group_id = %s
WHERE id = %s
'''
values = (group_id, student_id)
cursor.execute(query, values)
db.commit()

# Создайте несколько учебных предметов (subjects)
query = '''
INSERT INTO subjects (title)
VALUES (%s);
'''
values = [('Subject5',), ('Subject6',)]
subject_ids = []
for item in values:
    cursor.execute(query, item)
    subject_ids.append(cursor.lastrowid)
db.commit()

# Создайте по два занятия для каждого предмета (lessons)
query = '''
INSERT INTO lessons
(title, subject_id)
VALUES (%s, %s)
'''
values = [('lesson9', subject_ids[0]),
          ('lesson10', subject_ids[0]),
          ('lesson11', subject_ids[1]),
          ('lesson12', subject_ids[1])]
lesson_ids = []
for value in values:
    cursor.execute(query, value)
    lesson_ids.append(cursor.lastrowid)
db.commit()

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query = '''
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)
'''
values = [(5, lesson_ids[0], student_id),
          (4, lesson_ids[1], student_id),
          (8, lesson_ids[2], student_id),
          (7, lesson_ids[3], student_id)]
cursor.executemany(query, values)
db.commit()

# Все оценки студента
query = '''
SELECT *
FROM marks m
WHERE m.student_id = %s;
'''
cursor.execute(query, (student_id,))
print(cursor.fetchall())

# Все книги, которые находятся у студента
query = '''
SELECT *
FROM books b
WHERE b.taken_by_student_id = %s;
'''
cursor.execute(query, (student_id,))
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
query = '''
SELECT g.title AS 'group',
    b.title AS 'book',
    m.value AS 'mark',
    l.title AS 'lesson',
    subj.title AS 'subject'
FROM students s
    JOIN `groups` g
        ON g.id = s.group_id
    JOIN books b
        ON b.taken_by_student_id = s.id
    JOIN marks m
        ON m.student_id = s.id
    JOIN lessons l
        ON l.id = m.lesson_id
    JOIN subjects subj
        ON subj.id = l.subject_id
WHERE s.id = %s;
'''
cursor.execute(query, (student_id,))
print(cursor.fetchall())

db.close()
