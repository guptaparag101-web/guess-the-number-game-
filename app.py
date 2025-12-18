from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)
attempts = 0

print("INITIAL secret number:", secret_number)

@app.route("/", methods=["GET", "POST"])
def index():
    global secret_number, attempts
    message = ""

    if request.method == "POST":
        guess = request.form["guess"]
        print("Raw guess from form:", guess, type(guess))

        guess = int(guess)   # 🔴 VERY IMPORTANT
        print("Converted guess:", guess, type(guess))
        print("Current secret number:", secret_number)

        attempts += 1

        if guess < secret_number:
            message = "📉 Too Low"
        elif guess > secret_number:
            message = "📈 Too High"
        else:
            message = f"🎉 Correct! Attempts: {attempts}"
            secret_number = random.randint(1, 100)
            attempts = 0
            print("NEW secret number:", secret_number)

    return render_template("index.html", result=message)

if __name__ == "__main__":
    app.run(debug=True)
