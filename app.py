from flask import Flask, render_template


app = Flask('meu app')

post = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segundo post",
        "texto": "Outro teste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = post #Moc das postagens
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/novo')
def novo():
    return '<h1> Nova página </h1>'