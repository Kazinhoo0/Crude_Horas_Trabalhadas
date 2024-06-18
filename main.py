
<<<<<<< HEAD
from flask import Flask, render_template, redirect, request, flash
import mysql.connector
=======
from flask import Flask, render_template, redirect, request, flash, url_for
import sqlite3 as sql
>>>>>>> ce75b48b3b075efa691fca64da898ed93e1e2aa9

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kaue182023'


<<<<<<< HEAD
#se o usuário não acessar nenhuma página específica, ira ser direcionado para o index.html
=======
>>>>>>> ce75b48b3b075efa691fca64da898ed93e1e2aa9
@app.route('/')

def home() :
    return render_template('pagina_ptbr/index.html')

<<<<<<< HEAD

@app.route('/verprojetos')

def verprojetos () :
    return render_template('viewproj.html')



@app.route('/novoprojeto')
def novoprojeto () :
    return render_template('novoprojeto.html')



@app.route('/cadastrar' , methods= ['POST'])
def criarconta() :
    
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    
    conect_DB = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "",
        database = "usuários"
    )
    if conect_DB.is_connected():
        print("Banco de dados conectado com sucesso")
        
        cursor = conect_DB.cursor()
        cursor.execute(f"INSERT INTO usuarios (nome,senha) VALUES ('{nome}', '{senha}')")
    if conect_DB.is_connected():
        cursor.close()
        conect_DB.close()    
  
          
    return render_template("criarnovaconta.html")
    
        



# @app.route('/verprojetos')
# def verprojetos() :
#     return render_template("viewproj.html")



@app.route('/login', methods = ['POST'])
def login():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    conect_DB = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "",
        database = "usuários"
    )
    cont = 0
    if conect_DB.is_connected():
        print("Banco de dados conectado com sucesso")
        
        
        cursor = conect_DB.cursor()
        cursor.execute('select * from usuarios')
        usuariosDB = cursor.fetchall()
        # comando ="""INSERT INTO usuários_cadastrados (nome, senha) VALUES ()"""
        
        # cursor.execute(comando)
        
        for usuario in usuariosDB:
            
            cont += 1
            
            usuarioNome = str(usuario[0])
            usuariosenha = str(usuario[2])
            
            
            if nome == "adm" and senha == "000123" :
                return redirect('/criarconta')
            
            if usuarioNome == nome and usuariosenha == senha:
                return render_template('novoprojeto.html')

            if cont >= len(usuariosDB):
                flash('Usuario Inválido')
                return redirect("/")
    else :
        return redirect("/")
=======
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
>>>>>>> ce75b48b3b075efa691fca64da898ed93e1e2aa9




<<<<<<< HEAD
if __name__ in "__main__" :
=======
if __name__ == "__main__" :
>>>>>>> ce75b48b3b075efa691fca64da898ed93e1e2aa9
    app.run(debug = True)  