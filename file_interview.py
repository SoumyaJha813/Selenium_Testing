#read and write into a file
with open("test.txt","w") as f:
    f.write("Hello World")

try:
    with open("test1.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e: #execution will come here only if error is there in try block
    print(e)
finally:
    print("cleanup db connection, clean up resources")

'''
data = []
dict = {"name": "Alice", "age": 30}
data.append(dict)
list_dict = [
    {
    "name": "Alice",
    "age": 30
    },
    {
        "name": "Bob",
        "age": 40
    },
    {
        "name": "Carter",
        "age": 50
    }]

print(list_dict[0]["name"])

'''
import asyncio

"""
A lambda function in python is a small, anonymous function that can have mulitple arguments but only one expression.
It is written in a single line.
It is used where a short function is needed temporarily.
Don't use lambda if the function is complex-use def instead.
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b

add = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b

summ1 = lambda c,t: c+t
print(f"Sum lambda function : {summ1(5, 9)}")

numbers = [1,2,3,4,5]

squared_numbers = map(lambda x : x*2, numbers)
print(list(squared_numbers))

even_numbers = filter(lambda x : x%2 == 0, numbers)
print(list(even_numbers))
num = [4,1,7,3]
print(sorted(num))
#Synchronous Execution
import time
def task(name):
    print(f"Starting {name}")
    time.sleep(2) #block
    print(f"Finished {name}")

task("Soumya")
task("Riya")

#Asynchronous Execution
import time
async def task(name, delay):
    print(f"Starting task {name}")
    await asyncio.sleep(delay) #block
    print(f"Finished task {name} after {delay}")

async def main():
    await asyncio.gather(task("Xaden", 2), task("Violet", 1)) #Run tasks simultaneously

asyncio.run(main())




