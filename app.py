import hashlib
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Initial page load
    return render_template('index.html')


@app.route('/', methods=['POST'])
def hash():
    output = ""

    algorithm = request.form.get('hash_algorithm').lower()
    message = request.form.get('message')

    #Gets the appropiate function from hashlib through the algorithm selected in the html form and hashes the message given with it
    hash_func = getattr(hashlib, algorithm)
    m = hash_func
    message = m(message.encode()).hexdigest()

    if message:
        print(message)
        output = message

    # Output for fetch(), which will update the output textarea
    return output

# About route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)