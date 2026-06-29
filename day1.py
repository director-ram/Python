# To print the string
print("hello")
# variables
first_name = "Hema" #strings
last_name = "Sai"
age = 22 #integers
fee = 40000.99 #float
print(f"Hello {first_name + last_name} & {age} years old and your fee is {fee}")
#conditionals(if,else)
if age>=18:
    print("you can enter the club")
else:
    print("sorry, you are not old engouh!")
#comparision operators
# age == 22      # "Is age exactly 22?" → True
# age != 25      # "Is age NOT 25?" → True
# age > 18       # "Is age greater than 18?" → True
# age < 25       # "Is age less than 25?" → True
# age >= 22      # "Is age greater or equal to 22?" → True
# age <= 22      # "Is age less or equal to 22?" → True

#Loops-
#forloop
for i in range(5):
    print("*"*i)
#looping through lists
bikes = ["pulsar ns220", "ktm", "RX100", "hero honda", "tvs radieon", "royal enfield", "avanger indure", "harley davidson"]
for bike in bikes:
    print(bike)
bikes.append("BMW")
print(bikes)
#while loop
count = 0
while count<5:
    print(f"Count: {count}")
    count = count +1
#loop break
for i in range(10):
    if i == 5:
        break
    print(i)
#practice program
students = ["Hemasai", "Nateesha", "Dhoni", "Varun"]
fee_due = ["paid", "paid", "unpaid", "paid"]
for i in range(len(students)):
    student = students[i]
    fee_status = fee_due[i]
    if fee_status == "paid":
        print(f"{student} has paid the fee.")
    else:
        print(f"{student} has not paid the fee!!")
#Functions
def greet(name):
    print(f"Hello, {name}")

greet("hemasai")
greet("nateesha")
#functions with parameters and return values
def calculate_price(price, discount_percent):
    discount = price * (discount_percent/100) #this calculates discount
    final_price = price - discount # this gives final price after discount
    return final_price #this returns a value

price = 50000
discount_percent = 5
product_price = calculate_price(price, discount_percent)
print(f"the item price is {price} and final price after {discount_percent}% discount is: {product_price}")
#dictionaries
student= {
    "name" : "hemasai",
    "age" : 22,
    "fee" : 40000,
    "city" : "gudivada"
}
print(f"{student['name']} your fee is {student['fee']}")
student["fee_status"] = "paid"
print(student)
del student["city"]
#looping through dictionaries
for key in student:
    print(f"{key}:{student[key]}")
#input methods
user_name = input("Enter your name: ")
password = input("Enter new password:")
print("opening login page....")
new_password = input("enter your password: ")
while new_password != password:
    print("try again!!")
    new_password = input("enter your password: ")
    if new_password == password:
        break
print(f"Hello {user_name}")
# or you can try using functions
def login():
    name=input("enter your name: ")
    print(f"you entered: {name}")
    logged_in = input("Enter yes or no:")
    print(f"You entered:{logged_in}")
    if logged_in.lower() == "yes":
        print(f"{name} welcome your logged in.")
    else:
        print(f"{name} please login!!")

login()
#practice program
def get_student_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    department = input("Enter your dept: ")
    fee = float(input("Enter your fee: "))

    return { "name":name, "age":age, "dept":department, "fee":fee}
def check_elgibility(student):
    if student['age'] >= 18:
        return True
    return False
def process_student():
    students = []
    num_of_students = int(input("Enter no.of students: "))
    for i in range(num_of_students):
        print(f"\n ---Student{i+1}---")
        student = get_student_info()
        students.append(student)
    print(f"\n ===Student Report===")
    for student in students:
        status= "eligible" if check_elgibility(student) else "not eligible"
        print(f"\n name: {student['name']}, age: {student['age']}, fee: {student['fee']}, status: {status}")
process_student()