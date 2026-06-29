# JSON
#converting python to json
import time
import json
import datetime
student = {
    'name': 'Sameer',
    'age': 22,
    'grade': 8.9
}

json_string = json.dumps(student) #converts dictionary to json
#print(json_string)

#write to a file
print("saving....")
with open("student.json", "w") as file:
    json.dump(student, file) #IMP note: dump without 's', not dumps
time.sleep(1)
print("file saved!")
# read from file
print("loading file....")
with open("student.json", "r") as file:
    student_data = json.load(file)
time.sleep(0.5)
print("file loaded!")
print(student_data['name'])
time.sleep(1)
# or another example to convert from json-string
Json_string = '{"name":"Narendra", "age": 21, "grade": 10.0}'
data = json.loads(Json_string) # note: loads with 's'
print(data['name'])

# multiple dictionaries example
students = [
    {
        'name': 'Hemasai',
        'age': 21,
        'grade': 7.1,
        'dept': 'CSE'
    },
    {
        "name": "Dhoni",
        "age": 21,
        "grade": 8.5,
        "dept": "CSE"
    },
    {
        "name": "Nateesha",
        "age": 21,
        "grade": 9.1,
        "dept": "CSE"
    },
    {
        "name": "Neeraj",
        "age": 21,
        "grade": 9.5,
        "dept": "CSE"
    }
]

# saving into a file
with open("students.json", "w") as file:
    json.dump(students, file, indent=2) # indent=2 makes it readable

# open the json file and read the data
with open("students.json", "r") as file:
    json_students = json.load(file)

#displat students data
print("students from cse: ")
for student in json_students:
    print(f"{student['name']} - Grade: {student['grade']} from {student['dept']}")

# display top scorers
high_grades = [s for s in json_students if s['grade'] >= 8.0]
print(f"TOP students: {[s['name'] for s in high_grades]}")

#real example
#saving into a file
def save_profile(username, email, role):
    profile = {
        "name": username,
        "email": email,
        "role": role,
        "created": datetime.date.today().isoformat() # converts date to string
    }
    with open(f"{username}_profile.json", "w") as file:
        json.dump(profile, file, indent=2)

    print(f"profile of {username} was saved!!")
#reading from a file
def show_profile(username):
    try:
        with open(f"{username}_profile.json", "r") as file:
            profile = json.load(file)
        return profile
    except FileNotFoundError:
        print(f"{username}_profile not found!!")
        return None

#user input
username = input("Enter your username: ")
email = input("\nEnter your mail: ")
role = input("\nEnter your role: ")
with open(f"{username}_profile.json") as file:
    saved = json.load(file)

if saved is not None:
    profile = show_profile(username)
    if profile is not None:
        print("Details loaded...")
        print(f"Name: {profile['name']}\nEmail: {profile['email']}\nRole: {profile['role']}\nCreated on: {profile['created']}")
    else:
        print("No profile to display.")
else:
    save_profile(username,email,role)
    #ask user to show profile or not
    view_profile = input("Enter 'yes' to view profile, 'No' for exit: ")
    if view_profile == "yes" or view_profile == "y":
        profile = show_profile(username)
        if profile is not None:
            print("Details loaded...")
            print(f"Name: {profile['name']}\nEmail: {profile['email']}\nRole: {profile['role']}\nCreated on: {profile['created']}")
        else:
            print("No profile to display.")
    else:
        print("")