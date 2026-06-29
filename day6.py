#generator
def counter(n):
    i = 1
    while i<=n:
        yield i # give one number at a time
        i+=1
#n = int(input("Enter a number to print: "))
#for num in counter(n):
#    print(num)

num_list = [i for i in range(100)]
#print(num_list)

#generator creates numbers one at a time (saves memory)
def num_gen():
    for i in range(100):
        yield i
num_generator = num_gen()
#print(num_generator)

def fibonacci(n):
    a, b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

#for fib in fibonacci(10):
 #   print(fib, end=" ")

squares_gen = (i*i for i in range(10))
# for square in squares_gen:
#     print(square)
#print(square for square in squares_gen)

#map()
numbers = [i for i in range(6)]
#double each item using map
doubled = list(map(lambda x: x *2, numbers))
#print(doubled)
#comprehension version
doubled_comp = [x * 2 for x in numbers]
#print(doubled_comp)

#filter
integers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
evens = [x for x in integers if x % 2 == 0] # comprehension version
evens = list(filter(lambda x: x % 2 == 0, integers)) # with filter method and anonimus function
print(evens)

#reduce
from functools import reduce
fee = [{"name": "hemasai", "Fee":45000, "grade":80},
       {"name": "Neeraj", "Fee":45000, "grade":98},
       {"name": "madhu", "Fee":40000, "grade":68},
       {"name":"abhi ram", "Fee":25000, "grade":78},
       {"name": "dhoni", "Fee":20000, "grade":54}]
all_students_fee = reduce(lambda x,y: x + y['Fee'],fee,0)
print(all_students_fee)
#practice program
passing = filter(lambda g: g['grade']>=80, fee) # filter the passed students
names = map(lambda n: n['name'],passing) # get the names of passed students
result = ", ".join(names) # joining names with ","
print(result) # print the names of the students