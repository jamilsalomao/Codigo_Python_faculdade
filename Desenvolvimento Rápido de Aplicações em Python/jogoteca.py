from flask import Flask, render_template, request, redirect, url_for

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
@app.route("/")
def index() -> str:
    return render_template("lista.html", titulo="Jogos", jogos=lista)

@app.route("/novo")
def novo() -> str:
    return render_template("novo.html", titulo="Novo Jogo")

@app.route("/criar", methods=["POST"])
def criar() -> str:
    nome: str = request.form["nome"]
    categoria: str = request.form["categoria"]
    console: str = request.form["console"]
    
    jogo: Jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect(url_for('index'))

app.run(debug=True)
