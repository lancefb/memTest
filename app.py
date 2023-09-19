from flask import Flask, render_template, request, session
import requests
import random  

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def generate_random_numbers():
    # A function to generate 3 random numbers between 100 and 999
    return [random.randint(100, 999) for _ in range(3)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'random_numbers' not in session:
        session['random_numbers'] = generate_random_numbers()
    
    if request.method == 'POST':
        action = request.form.get('action')
        joke = request.form.get('joke')
        if action == 'JOKES':
            joke = get_joke()
        elif action == 'NUMBERS':
            session['random_numbers'] = generate_random_numbers()
        return render_template('index.html', joke=joke, random_numbers=session['random_numbers'], is_welcome_page=False)
    else:
        welcome_message = "Hover here to get numbers.<br>"
        return render_template('index.html', joke=welcome_message, random_numbers=session['random_numbers'], is_welcome_page=True)

def get_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return data['joke']

if __name__ == "__main__":
    app.run(debug=True)
