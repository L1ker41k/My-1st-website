from flask import Flask
from flask import redirect
from random import randint
from random import choice

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/home">home</a><br><a href="/random_number">random</a>'

@app.route("/home")
def home():
    return '<h1>Welcome to home!</h1><a href="/">back</a>'

@app.route("/random_number")
def random():
    return f'<h1>Your random  number is {randint(100, 999)}</h1><a href="/">back</a><br><a href="/random_number">reroll</a>'

@app.route('/random_fact')
def random_fact():
    facts = ['Атомов в песчинке больше, чем песчинок на Земле!', 'До 2006 года в Солнечной системе было 9 планет!', "У осьминога 3 сердца и 9 мозгов!", "Радиус наблюдаемой вселенной состовляет 46,5 млрд световых лет! Это примерно 435 секстиллионов км или 435*10^21!"]
    return f'<h1>Your random fact: {choice(facts)}</h1><a href="/">back</a><br><a href="/random_fact">reroll</a>'

@app.route('/secret')
def secret():
    return redirect('https://youtu.be/j-iheFkstFQ?si=BPeHcgdw_a1ipyD3')
app.run(debug=True)