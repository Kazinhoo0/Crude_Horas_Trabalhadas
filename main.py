
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kaue182023'



@app.route('/')

def home() :
    return render_template('index.html')

@app.route('/criarconta')
def criarconta() :
    return render_template ("criarnovaconta.html")

@app.route('/verprojetos')
def verprojetos() :
    return render_template("viewproj.html")



@app.route('/login', methods = ['POST'])
def login () :

    nome = request.form.get('nome')
    senha = request.form.get('senha')
    
    if nome == 'kauã' and senha == '12345' :
        return render_template("novoprojeto.html")
    else :
        render_template('index.html')



    return redirect('/login')
    # render_template("novoprojeto.html")



if __name__ in "__main__" :
    app.run(debug = True)  