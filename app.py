from flask import Flask, render_template, request
import requests
import random  # Step 1: Import the random module

app = Flask(__name__)

def generate_random_numbers():
    # Step 2: Create a function to generate 3 random numbers between 100 and 999
    return [random.randint(100, 999) for _ in range(3)]

@app.route('/', methods=['GET', 'POST'])
def index():
    random_numbers = generate_random_numbers()  # Step 3: Generate random numbers when page is loaded
    if request.method == 'POST':
        joke = get_joke()
        return render_template('index.html', joke=joke, random_numbers=random_numbers)
    else:
        joke = get_joke()
        return render_template('index.html', joke=joke, random_numbers=random_numbers)  # Pass random numbers to the template

def get_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return data['joke']

if __name__ == "__main__":
    app.run(debug=True)

