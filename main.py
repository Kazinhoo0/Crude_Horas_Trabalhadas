
from flask import Flask, render_template, redirect, request, flash, url_for
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kaue182023'


@app.route('/')

def home() :
    return render_template('pagina_ptbr/index.html')

@app.route('/index', methods = ["POST"])

def index () :
    conect = sql.connect ('form_db.db')
    conect.row_factory=sql.Row
    cursor = conect.cursor()
    cursor.execute("select * from usuarios")
    data = cursor.fetchall()
    
    return render_template('pagina_ptbr/index.html', datas= data)


@app.route('/criarnovaconta' , methods = ["POST","GET"])
def criarnovaconta() :


    if request.method == "POST":
        
        nome = request.form ['nome']
        senha = request.form ['senha']


        conect = sql.connect ('form_db.db')
        conect.row_factory=sql.Row
        cursor = conect.cursor()

        cursor.execute(f"INSERT INTO usuarios (nome,senha) VALUES (?,?)" , (nome,senha))
        conect.commit()
        flash("Usuario criado com sucesso!")
        cursor.close()
        conect.close()

        return redirect(url_for('index'))
    return render_template('pagina_ptbr/criarnovaconta.html')


@app.route('/modifyvalorhora')
def modifyvalorhora () :
    return render_template('pagina_ptbr/modifyvalorhora.html')

@app.route('/tothorasproj')

def tothorasproj () :
    return render_template('pagina_ptbr/tothorasproj.html')

@app.route('/viewproj')
def viewproj() :
    return render_template('pagina_ptbr/viewproj.html')

@app.route('/novoprojeto')

def novoprojeto () :
    return render_template('pagina_ptbr/novoprojeto.html')

@app.route('/historypag')
def historypag () :
    return render_template("pagina_ptbr/historypag.html")
#--------------------------------------               ROTAS DA PAGINA EM INGLES-------------------------------------------------------------------#


@app.route('/indexenglish', methods = ["POST"])

def indexenglish () :
    conect = sql.connect ('form_db.db')
    conect.row_factory=sql.Row
    cursor = conect.cursor()
    cursor.execute("select * from usuarios")
    data = cursor.fetchall()
    
    return render_template('pagina_eng/index_english.html', datas= data)


@app.route('/historypagenglish')
def historypagenglish () :
    return render_template("pagina_eng/historypag_english.html")

# @app.route('/modifyvalorhoraenglish')
# def modifyvalorhoraenglish () :
#      return render_template('pagina_eng/modifyvalorhora_english.html')

# @app.route('/tothorasprojenglish')

# def tothorasprojenglish () :
#      return render_template('pagina_eng/tothorasproj_english.html')

# @app.route('/viewprojenglish')
# def viewprojenglish () :
#     return render_template('pagina_eng/viewproj_english.html')

# @app.route('/novoprojetoenglish')

# def novoprojetoenglish () :
#     return render_template('pagina_eng/novoprojeto_english.html')




if __name__ == "__main__" :
    app.run(debug = True)  