import time
#Error handling
try:
    #code that might cause an error
    name = input("enter your name: ")
    print(f"Hello {name}")

    age = int(input(f"{name} enter your age: "))
    print(f"your age is {age}")
except ValueError:
    #code that runs when an error occurs
    print("the Enter a number!!")
except:
    print("there is a error!")
#finally
file = None
try:
    file = open("students-data.txt", "r")
    content = file.read()
    print("file opened")
    time.sleep(2)
    print(f"\n{content}")
except FileNotFoundError:
    print("file doesn't exists")
finally:
    if file is not None:
        file.close()
        time.sleep(1)
        print("file closed")

#practice program
def integer_input(prompt):
    try:
        value = int(input(prompt))
        if value < 0 or value > 100:
            print("grade must be between 1-100")
        return value
    except ValueError:
        print("enter a valid number")
def add_student(students):
    try:
        name = input("enter your name: ")
        if not name.strip():
            print("name cannot be empty!")
            return
        
        grade = integer_input("Enter the student grade: ")
        students.append({"name":name,"grade": grade})
        print(f"{name} added successfully")
    except Exception as e:
        print(f"Error: {e}")
students = []
add_student(students)

# List comprehensions
numbers = [i for i in range(5)]
print(numbers)

squares = [i**2 for i in range(5)]
print(squares)

# with if condition
grades = [99,54,65,98,78,45,68,75,88,82,87,59,91,84]
high_grades = [g for g in grades if g>=80]
print(high_grades)

# with dictionaries
employees = [{"name": "suresh", "salary": 25000},
             {"name": "vivek", "salary": 22000},
             {"name": "neeraj", "salary": 30000}]
highest_salary = [e['salary'] for e in employees if e['salary'] > 25000]
print(highest_salary)

# neseted comprehension
grid = [[i*4 + j for j in range(4)] for i in range(4)]
print(grid)
# flating a matrix
matrix = [[0,1,2],[3,4,5],[6,7,8]]
flat = [num for row in matrix for num in row]
print(flat)
# decorator
def my_decorator(func):
    """decorator returns with a wrapper"""
    def wrapper():
        print("=" * 20)
        func()
        print("="*20)
    return wrapper
@my_decorator
def greet():
    print("hello world")
greet()

def time_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} starting....")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper
@time_decorator
def timer():
    time.sleep(4)
    print("function execution finished.")

timer()

def require_login(func):
    def wrapper(user):
        try:
            if user.get("is_loggedIn"):
                return func(user)
            else:
                print(f"\n{user.get('name')} not loggedIn!!")
                return None
        except Exception as e:
            print(f"Error: {e}")
    return wrapper
@require_login
def view_profile(user):
    print(f"\nWelcome {user['name']}")
    print(f"Email: {user['email']}")
user1 = {"name":"Hemasai","email":"khemasai413@gmail.com","is_loggedIn": True}
admin = {"name":"Admin","email":"admin@gmail.com","is_loggedIn": False}
user2 = {"name":"Dhoni","email":"correadhoni@gmail.com","is_loggedIn": True}
view_profile(user1)
view_profile(admin)
view_profile(user2)