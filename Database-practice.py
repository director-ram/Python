import sqlite3

class StudentDatabase:
    def __init__(self,db_name = "school.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.CreateTable()
    #Creating table if it doesnt exists
    def CreateTable(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER,
                            grade REAL
                            )
    """)
        self.connection.commit()
    
    #adding students to table
    def add_student(self, name, age, grade):
        self.cursor.execute("""INSERT INTO students(name, age, grade)
                            VALUES(?,?,?)""",(name,age,grade))
        self.connection.commit()
        print(f"{name} added to database!")

    #display all students from table
    def show_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    #get top scorers    
    def top_students(self, min_grade=80):
        self.cursor.execute("""SELECT name, grade FROM students
                            WHERE grade >= ?
                            ORDER BY grade DESC""",(min_grade,))
        print("Database created!")
        return self.cursor.fetchall()

    #close the db connection
    def close(self):
        self.connection.close()

db = StudentDatabase()

db.add_student('Nateesha',21,99)
db.add_student('Sameer',21,47)
db.add_student('Madhu',22,85)

print("\n ALL STUDENTS: ")
for student in db.show_all_students():
    print(student)

print("\n TOP students: ")
for name, grade in db.top_students():
    print(f"{name}: {grade}%")

db.close()