import functions
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    cotacao = functions.principal()
    dolar = cotacao[0]
    euro = cotacao[1]
    bitcoin = cotacao[2]
    bitcoin = (f"{bitcoin:.3f},00")
    return render_template('home.html', dolar=dolar, euro=euro, bitcoin=bitcoin)

if __name__ == '__main__':
    app.run(debug=True)











