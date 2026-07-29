import csv
import dotenv
import mysql.connector as mysql
import os


dotenv.load_dotenv(override=True)
db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

query = '''
SELECT s.name,
    s.second_name,
    g.title AS 'group_title',
    b.title AS 'book_title',
    m.value AS 'mark_value',
    l.title AS 'lesson_title',
    subj.title AS 'subject_title'
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
WHERE s.name = %s
    AND s.second_name = %s
    AND g.title = %s
    AND b.title = %s
    AND m.value = %s
    AND l.title = %s
    AND subj.title = %s
'''

with open('C:/Users/egor.romanovskiy/JOB/Automation/okulik/yvr/homework/eugene_okulik/Lesson_16/hw_data/data.csv', 'r'
          ) as file:
    for line in csv.DictReader(file):
        values = (line['name'], line['second_name'], line['group_title'], line['book_title'], line['mark_value'],
                  line['lesson_title'], line['subject_title'])
        cursor.execute(query, values)
        if len(cursor.fetchall()) == 0:
            print(line)

cursor.close()
