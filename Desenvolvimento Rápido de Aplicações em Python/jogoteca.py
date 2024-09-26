from flask import Flask, render_template, request, redirect, url_for, session, flash

class Jogo:
    def __init__(self, nome: str, categoria: str, console: str):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1: Jogo = Jogo("God of War", "Ação", "PS4")
jogo2: Jogo = Jogo("Skyrim", "RPG", "PS4")
jogo3: Jogo = Jogo("Fifa 21", "Esportes", "PS4")
    
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'estacio'


@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista)

@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')

@app.route("/criar", methods=["POST"])
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', 
                           titulo='Login', 
                           proxima = proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'admin' == request.form['usuario'] and 'admin' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ': Login realizado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Não logado, tente novamente')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso')
    return redirect(url_for('index'))

app.run(debug=True)