#OOPS
#Inheritance
class Person:
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Hello, im {self.name} & {self.age} years old')

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age) # calling parent constructor
        self.grade = grade
    def get_marks(self):
        print(f"{self.name} got {self.grade}%")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def teacher_info(self):
        print(f"{self.name} teachs '{self.subject}' ")

student = Student("hemasai", 22, 89)
teacher = Teacher("Nagesh Babu", 45, "React.js")
student.introduce()
teacher.introduce()
student.get_marks()
teacher.teacher_info()

#polymorphism
import time
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        time.sleep(1)
        print("Woof!")
        time.sleep(1)
class Cat(Animal):
    def sound(self):
        print("Meoow!")
        time.sleep(1)
class Cow(Animal):
    def sound(self):
        print("Moo!")
animals = [Dog(),Cat(),Cow()]
for animal in animals:
    animal.sound()

#Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # '__' means private
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}₹ successfully")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}₹ has been withdrawn successfully!")
        else:
            print("Invalid Amount!!")
username = input("Enter your name: ")
deposit = float(input("Enter deposit amount: "))
withdraw = float(input("Enter withdraw amount: "))
account = BankAccount(username, 0)
print(f"Balance: {account.get_balance()}₹")
account.deposit(deposit)
account.withdraw(withdraw)
print(f"Available Balance: {account.get_balance()}₹")

# API - Application Program Interface
# Common request types-
# GET - give me data
# POST - sending data
# PUT - update this data
# DELETE - Remove this data
# requests.get() - send request to the website
# response - recivied from website
# status_code - did it work?(200 means yes, 404 means not found)

# example program
import requests
# url of weather api
url = "https://api.weatherapi.com/v1/current.json"
# parameters
params = {
    "key": "8268ee7479184768be9153927261906", # your api key
    "q": "Gudivada", #City name
    "aqi": "yes" # Air quality index
}

# make request
response = requests.get(url, params=params)

#check the response status
if response.status_code == 200:
    data = response.json() # converting it to python dictionaries
    #extract data
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    city = data['location']['name']
    state = data['location']['region']
    country = data['location']['country']
    wind_dir = data['current']['wind_dir']
    wind_speed = data['current']['wind_kph']

    #output the data
    print(f"City: {city}, \nState: {state}, \nCountry: {country}")
    print(f"Temparature: {temp} °C")
    print(f"Condition: {condition}")
    print(f"Wind Speed: {wind_speed}kmph\nWind Direction: {wind_dir}")
else:
    print(f"Error: {response.status_code}")

#POST method
url = "https://httpbin.org/post"

# data to send
data = {
    'name': 'hemasai',
    'age': 22,
    'email': 'testamail@gmail.com',
    'password': 'testpassword'
}

# post request to send data
response = requests.post(url, json=data)

print(response.status_code)
#print(response.json()) # to see what server received