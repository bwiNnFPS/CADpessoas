from flask import Flask, render_template, request, redirect
lista=[]

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('Home.html', Titulo='Bem vindo ao site de cadastro de pessoas')

@app.route('/pokemon')
def pokemon():
    return render_template('Pokemon.html', Banana='pessoas')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Banana='Sobre nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Banana='Cadastro de pessoas')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Banana='pessoas cadastrados', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    genero = request.form['genero']
    altura = request.form['altura']
    peso = request.form['peso']
    pokemon = [nome, genero, altura, peso]
    lista.append(pokemon)
    return  redirect ('/exibir')

if __name__ == '__main__':
    app.run()
