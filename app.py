from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        joke = get_joke()
        return render_template('index.html', joke=joke)
    else:
        joke = get_joke()
        return render_template('index.html', joke=joke)

def get_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    return data['joke']

if __name__ == "__main__":
    app.run(debug=True)

