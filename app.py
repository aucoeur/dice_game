from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

def roll_dice():
    result = randint(1,6)
    return result

@app.route('/')
def index():
    section = 'Greetings, human'
    return render_template('index.html',
        section=section)


@app.route('/dice')
def play_dice_game():
    name = request.args.get('name')
    die1 = roll_dice()
    die2 = roll_dice()
    
    if die1 == die2:
        return "You won! You rolled " + str(die1) + " and " + str(die2) + "."

    return render_template('dice.html',
        name=name,
        die1=die1,
        die2=die2)

if __name__ == '__main__':
    app.run(debug=True)