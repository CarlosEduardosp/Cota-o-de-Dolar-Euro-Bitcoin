import functions
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

lista_valores = []


@app.route('/', methods=['GET','POST'])
def home():

    cotacao = functions.principal()
    dolar = cotacao[0]
    euro = cotacao[1]
    bitcoin = cotacao[2]
    bitcoin = (f"{bitcoin:.3f}.00")

    return render_template('home.html', dolar=dolar, euro=euro, bitcoin=bitcoin, lista_valores=lista_valores)



@app.route('/calculo', methods=["GET", "POST"])
def calculo():

    if request.method == 'POST':
        valor_conversao = request.form.get('valor')
        moedas = functions.converter(valor_conversao)
        lista_valores.clear()
        if moedas:
            lista_valores.append(moedas[0])
            lista_valores.append(moedas[1])
            lista_valores.append(moedas[2])
            lista_valores.append(moedas[3])


        return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)










