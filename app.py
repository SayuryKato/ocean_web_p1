from flask import Flask, render_template, request, session, flash, redirect, url_for


app = Flask('meu app')
app.config['SECRET_KEY'] = 'pudim'

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
    entradas = post[::-1] #Moc das postagens
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username'] == "admin" and request.form['password'] == "admin":
            session['logado'] = True
            flash("Login efetuado com sucesso!")
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"        
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado')
    flash('logout efetuado com sucesso!')
    return redirect(url_for('exibir_entradas'))

@app.route('/inserir', methods=['POST'])
def inserir_entrada():
    if session['logado']:
        novo_post ={ 
            'titulo': request.form['titulo'],
            'texto': request.form['texto']
        }
        post.append(novo_post)
        flash("Post criado com sucesso!")
    return redirect(url_for('exibir_entradas'))

@app.route('/posts')
# @app.route('/novo')
# def novo():
#     return '<h1> Nova página </h1>'