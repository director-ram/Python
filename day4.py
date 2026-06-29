#Modules & libraries
import random
import datetime
import math
import time
import my_function

print(random.randint(1, 20))

fruits = ["Apple","Banana","Custardapple"]
print(random.choice(fruits))
#we can use shuffle along with the random
cards = [1,2,3,4,5,6,7]
random.shuffle(cards)
print(cards)
#practice program
def roll_dice():
    return random.randint(1,6)
player1 = roll_dice()
player2 = roll_dice()

print(f"player 1 rolled: {player1}")
print(f"player 2 rolled: {player2}")

if player1 > player2:
    print("player 1 wins!")
elif player1 < player2:
    print("player 2 wins!")
else:
    print('its a tie')

# date modules
today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)

birthday = datetime.date(2004, 8, 14)
print(f"your birthday is on {birthday}")
#calculate diff b/w dates
age = today.year - birthday.year
print(f"You are {age} OLD")

#math module
print(math.sqrt(256)) # to get square root of the number
print(math.floor(6.7)) # to round down the value
print(math.ceil(6.2)) # to round up the value
print(math.pow(3,2)) # to get the power of a value
print(math.pi) # to get the PI value
print(abs(-24)) # to absolute a -ve value
def area_circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area
radius = 8
area_of_circle = area_circle(radius)
print(f"Area of circle with radius of {radius}: {area_of_circle:.2f}")

# time module
print("Starting...")
time.sleep(5) # it will wait for 5 sec
print("Done waiting...")
# using it in countdown
def countdown(seconds):
    while seconds > 0:
        print(f"countdown: {seconds}")
        time.sleep(1)
        seconds -=1
    print("Happy birthday!!")
countdown(10)

# using functions from another file
print(my_function.greet("hemasai"))