from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)