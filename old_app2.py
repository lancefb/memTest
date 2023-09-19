from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'state' not in session:
            session['state'] = 'numbers'
            session['jokes'] = ['Joke 1', 'Joke 2']  # Replace with your actual jokes
            session['random_numbers'] = [random.randint(100, 999) for _ in range(3)]

        if session['state'] == 'numbers':
            session['state'] = 'joke1'
        elif session['state'] == 'joke1':
            session['state'] = 'joke2'
        elif session['state'] == 'joke2':
            session['state'] = 'numbers'
        
        response_data = {'state': session['state']}
        if session['state'] == 'numbers':
            response_data['random_numbers'] = session['random_numbers']
        else:
            response_data['joke'] = session['jokes'][0] if session['state'] == 'joke1' else session['jokes'][1]

        return jsonify(response_data)
    
    session.clear()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
