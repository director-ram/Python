#class in python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def is_passing(self):
        return self.grade >= 60
    def get_info(self):
        return f"{self.name} - {self.grade}"
    
#create student objects
hemasai = Student("Hemasai", 98)
varun = Student("Varun", 92)
dhoni = Student("Dhoni", 96)

#use objects
print(hemasai.get_info())
print(hemasai.is_passing())
# pratice program
class Students:
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade
        self.attendance = 0
    #to mark attendance
    def add_attendance(self):
        self.attendance += 1
    # to get full status of students
    def get_status(self):
        if self.grade >= 80:
            status = "Excellent"
        elif self.grade >=60:
            status = "Good"
        else:
            status = "Needs improvement"
        return f"{self.name}: {self.grade} ({status}) - Attendance: {self.attendance}"
#creating multiple student objects
Student_list = [Students("Hemasai", 98),
                Students("Nateesha", 98.1),
                Students("Varun", 96),
                Students("Dhoni", 89),
                Students("Neeraj", 98.5),
                Students("Madhu", 100.0)]
# marking attendance
Student_list[0].add_attendance()
Student_list[0].add_attendance()
Student_list[0].add_attendance()
Student_list[0].add_attendance()
Student_list[1].add_attendance()
Student_list[1].add_attendance()
Student_list[1].add_attendance()
Student_list[1].add_attendance()
Student_list[1].add_attendance()
Student_list[2].add_attendance()
Student_list[2].add_attendance()
Student_list[3].add_attendance()
Student_list[3].add_attendance()
Student_list[3].add_attendance()
Student_list[4].add_attendance()
Student_list[4].add_attendance()
Student_list[4].add_attendance()
Student_list[4].add_attendance()
Student_list[4].add_attendance()
Student_list[5].add_attendance()
Student_list[5].add_attendance()
Student_list[5].add_attendance()
Student_list[5].add_attendance()
Student_list[5].add_attendance()
Student_list[5].add_attendance()
Student_list[5].add_attendance()
#display students
for student in Student_list:
    print(student.get_status())
#working with CSV files
import csv
students = [{"name": "Hemasai", "grade": 99},
            {"name": "Dhoni", "grade": 94},
            {"name": "Neeraj", "grade": 95},
            {"name":"Varun","grade":62}]
print("\nStudents list from CSV file\n")
with open("students_info.csv", "w",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['name','grade'])
    writer.writeheader()
    writer.writerows(students)
with open("students_info.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} - {row['grade']}")