from flask import Flask, url_for

app = Flask(__name__)

utenti_db: dict[int,str] = {
    100: 'Alessio',
    101: 'Rebecca',
    102: 'Edoardo',
    103: 'Rachele'
}

post_db: dict[int, str] = {
    1: 'Io sono Alessio',
    2: 'Io sono Rebecca, La giusta',
    3: 'Io sono Edoardo, aka Lo Stronzo Colossale',
    4: 'Io sono Rachele'
}

@app.route('/about')
def welcome():
    return "<h1>Benventuri nella nostra app</h1>" \
    "<div>In questa app trovi gli utenti</div>"

@app.route("/users/<string: nome>")
def get_user(nome: str):
    return f"<h3>Benvenuto {nome}!</h3>"

@app.route("/square/<int: n>")
def square(n: int):
    square = n**2
    return f"<h3>Il quadrato di {n} è {square}</h3>"

@app.route("/sum/<int: a>/<int: b>")
def summ(a, b):
    somma = sum(a,b)
    return f"<h3>La somma di {a} e {b} è {somma}</h3>"

@app.route("/")
def directions():
    return f"<h1>Benvenuti Cojoni!!</h1>" \
    f'<div><a href = "{url_for("welcome")}>About Us</a></div>"' \
    f'<div><a href = "{url_for("list_users")}">Lista Utenti</a></div>'

@app.route("/users")
def list_users():

    html_output:str = "<h1>Questo è l'elenco degli utenti</h1>"
    html_output += '<ul>'

    for id_user, name_user in utenti_db.items():
        html_output += f'<li><a href={url_for('get_user',name = name_user)}>{name_user}</a></li>'

    html_output += '</ul>'

    return html_output


@app.route("/post")
def list_posts():

    html_output: str = "<h1>Questo l'elenco dei post</h1>"
    html_output += "<ul>"

    for id_post, post in post_db.items():
        html_output += f"<li>{post}</li>"

    html_output += "</ul>"

    return html_output

def find_post(id: int):
    if id in post_db:    
        post = post_db.get(id)
        return f"<div>{post}</div>"
    
