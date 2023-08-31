from flask import Flask

app = Flask('meu app')

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/novo')
def novo():
    return '<h1> Nova página </h1>'