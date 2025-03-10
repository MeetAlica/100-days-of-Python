from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9!</h1>"\
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1>Too high, try again!</h1>"\
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzE3NWdram5wcXFpdDI1ZW5scDJvbzJ0M2Q5b2xvZ2QxMDdtbWE5aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/EJsTKyvaYzvm8/giphy.gif'>"
    elif guess < random_number:
        return "<h1>Too low, try again!</h1>"\
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGJmMzluMndnd2lsd28yeHcyOWM1NGRsanYyZ29sa3cxdWljZTc2biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3OhXBaoR1tVPW/giphy.gif'>"
    else:
        return "<h1>You found me!</h1>"\
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3BhYjBzZW8yajlzNHUxNDFyeTFpNWsyN3lpbjk3aW52eGUxNmxjZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Z4B75dyOkCr5SrsNP1/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)