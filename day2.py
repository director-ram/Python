#string methods
text = "Hello World"
#replace
new_text = text.replace("World","MotherFucker")
print(new_text)
sentence = " I love Python"
#split & strip(for only right- rstip, for only left- lstrip)
message = sentence.strip().split()
#print(message)
for name in message:
    print(name)
filename = "photo.jpg"
#endswith & startswith
if filename.endswith(".jpg"):
    print(f"Your file {filename} is an image")
if sentence.find("Python") !=-1:
    print("Found Python")
else:
    print("Not Found")

#list methods
"""why does it is used, it is used with lists(AKA arrays)"""
fruits = ["apple", "banana", "orange"]
#pop (if you didnt specify position it removes last element or item)
removed = fruits.pop(1)
print(removed)
#append
fruits.append("mango")
#insert
fruits.insert(1, "banana")
for fruit in fruits:
    print(fruit)
#sort
numbers = [1,32,5,4,6,7,6,79,411,23]
numbers.sort()
print(numbers)
#reverse sort
numbers.sort(reverse=True)
print(numbers)
names = ["hemasai", "dhoni", "varun"]
names.sort()
names.reverse()
print(names)
#count
print(numbers.count(6))
#index
try:
    print(fruits.index("strawberry"))
except:
    print("not found")
#join
joints = ",".join(fruits)
print(joints)

#tuples
# tuples are immutable whereas lists are mutable
my_tuple = ("Hema","sai")
print(my_tuple)

#practice program
def add_student_grades(students):
    name = input("Enter the student name: ")
    grade = float(input("Enter grade(0-100): "))
    students.append({"name": name,"grade": grade})
    print(f"{name} added!")

def show_all_students(students):
    if not students:
        print("No students yet!")
        return
    print(f"\n ===ALL STUDENTS LIST===")
    for student in students:
        print(f"{student['name']}- Grade: {student['grade']}")

def find_top_students(students):
    if not students:
        print("No students Yet!!")
        return
    print("===Top Students===")
    top = max(students, key=lambda s: s['grade'])
    print(f"\n Name: {top['name']} with {top['grade']}%")
def get_avg_grade(students):
    if not students:
        print("No students yet!")
        return
    total = sum(student['grade'] for student in students)
    average = total/len(students)
    print(f"\n Average grade: {average:.2f}")

#file handeling
#writing
with open("students.txt","w") as file:
    file.write("name: Hemasai - grade: 98\n")
    file.write("name: Neeraj - grade: 96\n")
#reading
with open("students.txt", "r") as file:
    content = file.read()
    #print(content)
#line by line reading
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
#append to file without erasing exisiting data
with open("students.txt", "a") as file:
    file.write("name: Varun - grade: 92\n")
# practice program
def save_students_info(students, filename):
    if not students:
        print(f"No students to save into {filename}")
        return
    
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student['name']} - {student['grade']}\n")
    print(f"{filename} saved with {len(students)} students")
def load_students(filename):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    name, grade = line.strip().split("-")
                    students.append({"name": name, "grade": float(grade)})
        print(f"Loaded {len(students)} from {filename}")
        for student in students:
            print(f"name:{student['name']}- grade: {student['grade']}")
    except:
        print("file not found!")
    return students
def main():
    students = []
    filename = "students-data.txt"

    while True:
        print("\n Select a option from below:")
        print("1. Add student")
        print("2. show all students")
        print("3. show top student")
        print("4. show average grade")
        print("5. save students data")
        print("6. load saved data")
        print("7. Exit")

        choice = input("choose an option (1-5): ")

        if choice == "1":
            add_student_grades(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            find_top_students(students)
        elif choice == "4":
            get_avg_grade(students)
        elif choice == "5":
            save_students_info(students, filename)
        elif choice == "6":
            load_students(filename)
        elif choice == "7":
            print("\n Exiting....")
            break
        else:
            print("Invalid Choice!!")
main()