## Command line prompts

# pwd - Where am I?
# ls - List Files 
# cd - Change directory
# cd .. - Moving backwards in folders
# touch main.py - Create main.py file 
# rm main.py - Delete main.py file 
# rm -rf Test - Remove Test folder



## Introducing to Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/bye')
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()



## Decorator functions

import time

# Decorator to measure execution time
def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# Print the current time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Run the functions
test_fast = fast_function()
test_slow = slow_function()