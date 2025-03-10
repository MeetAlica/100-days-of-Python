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
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
    "<p>This is a paragraph</p>" \
    "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGUxY3JsaXRtdnR5ZjU3bTBndTFoeHcxdnhvNnZuc2kzcm8xeXo5bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lJNoBCvQYp7nq/giphy.gif'>"

@app.route('/bye')
def say_bye():
    return "Bye!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hi, {name}! Your number is: {number}"

if __name__ == "__main__":
    app.run(debug=True)



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



## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(func):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Ali")
new_user.is_logged_in = True
create_blog_post(new_user)