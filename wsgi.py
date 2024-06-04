from flask import Flask, jsonify
from game_test.game import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    return jsonify({'roll':dice.roll()})
