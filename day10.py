# creating database
# sqlite3 is built in python
import sqlite3

#connect to a database file
connection = sqlite3.connect("students.db")

# Get a tool to work with database (cursor)
cursor = connection.cursor()

#create a table
cursor.execute("""
    CREATE TABLE students (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER,
               grade REAL
    )
""")

#save data
# connection.commit()

print("Table created")

# Inserting data into tables
# ADD one student
cursor.execute("""
    INSERT INTO students(name, age, grade)
               VALUES ('Hemasai', 22, 98)               
""")

# add multiple students
students = [
    ('Dhoni', 21, 78),
    ('Varun', 21, 88),
    ('Neeraj', 21, 99)                
]

cursor.executemany("""
    INSERT INTO students(name,age,grade)
                   Values(?,?,?)
""", students)

#connection.commit()
print(f"{cursor.rowcount} students added")

# getting all students data
cursor.execute("""SELECT * FROM students""")
all_students = cursor.fetchall()

# for student in all_students:
#     print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

# get specific details
cursor.execute("""
               SELECT name, grade FROM students 
               WHERE grade >= 80
               """)
high_grades = cursor.fetchall()

print("\n Top students: ")
for name, grade in high_grades:
    print(f"{name}: {grade}%")


#updating data
cursor.execute("""UPDATE students SET grade = 96 WHERE name = 'Dhoni'""")
connection.commit()
print(f"{cursor.rowcount} student(s) added")

cursor.execute("""SELECT * FROM students WHERE name = 'Dhoni'""")
print(cursor.fetchone()) # fetchone is used to get first result only

# deleting students from table
cursor.execute("""INSERT INTO students (name, age, grade)
               VALUES('Raj', 23, 68)
""")
#connection.commit()
print(f"{cursor.rowcount} student(s) added")

#delete a student
cursor.execute("""DELETE FROM students WHERE name = 'Raj'""")
connection.commit()
print(f"{cursor.rowcount} student(s) Deleted")

for student in all_students:
    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
connection.close()