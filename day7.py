# regular expressions
# find pattrens in text (regex)
#cheat sheet
# | Pattern | Meaning                   | Example Match      |
# | ------- | ------------------------- | ------------------ |
# | `\d`    | Digit                     | `5`, `8`, `0`      |
# | `\w`    | Letter, digit, underscore | `a`, `Z`, `_`, `7` |
# | `\w+`   | One or more word chars    | `hello123`         |
# | `\s`    | Whitespace                | space, tab         |
# | `\s+`   | One or more whitespaces   | `"   "`            |
# | `+`     | One or more occurrences   | `aaa`, `123`       |

import re
import time
import pyttsx3
text = "My email is testmail@gmail.com and my frnd email is hemasai@gmail.com"
#find pattren if it exists
# if re.search(r"@", text):
#     print("Email found!")

emails = re.findall(r"\w+@\w+\.\w+", text) #findall() returns a list
#"\w+" for one or more letters or _ or numbers, "@" means @, "\w+" is for gmail or yahoo or outlook, "\." used for dot(.), normal dot(.) means any character in regex thats why backslash dot used,"\w+" mathces com or org
#print(emails)

numbers = "I am hitiksha from 3 rd class"
num = re.findall(r"\d", numbers) #"\d" searches for numbers 0-9
#print(num)

words = re.findall(r"\w+",numbers) #as mentioned earlier w for letters, numbers & underscore, "+" for more
#print(words)

space = "Hello    World"
parts = re.split(r"\s+", space)
#print(parts)

#practice program
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern,email))

emails = []

if not emails:
    count = int(input("enter no.of emails: "))
    for _ in range(count):
        emails.append(input("enter email: "))

for email in emails:
    print(f"the {email}: {is_valid_email(email)}")
    time.sleep(2)
#for extracting phone numbers
mobile_num = " contact me 9391763277 or 918-248-6441"
phone = re.findall(r"\d{3}[-.]?\d{3}[-.]?\d{4}",mobile_num)
#print(phone)

#example of pyttsx3
talk = pyttsx3.init()
talk.say("hello user")
talk.runAndWait()
