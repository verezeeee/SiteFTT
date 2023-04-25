from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = '1234321'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)