
from flask import Flask, render_template, redirect, request, flash , url_for
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kaue182023'


#se o usuário não acessar nenhuma página específica, ira ser direcionado para o index.html
@app.route('/')
def home() :
    return render_template('pagina_ptbr/index.html')

@app.route('/verprojetos')
def verprojetos () :
    return render_template('viewproj.html')



@app.route('/novoprojeto')
def novoprojeto () :
    return render_template('novoprojeto.html')


@app.route('/index', methods = ['POST'])
def index():

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











@app.route('/criarnovaconta' , methods= ['POST' , 'GET'])

def criarconta() :
    if request.method == 'POST':
        nome = request.form.get ('nome')
        senha = request.form.get ('senha')
        
        if not nome and not senha:
            flash('O campo Usuário e senha são obrigatorios')
            return render_template('pagina_ptbr/criarnovaconta.html')
   
        
        try:
            conect_DB = mysql.connector.connect(
                host="localhost",
                user = "root",
                password = "",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso")
                cursor = conect_DB.cursor()
                comando = ("INSERT INTO usuarios (nome,senha) VALUES (%s,%s)")
                cursor.execute(comando, (nome , senha))
                flash('Conta criada com sucesso!')
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
        return redirect(url_for('home'))
            
        
        
    return render_template('pagina_ptbr/criarnovaconta.html')   
  
        


# @app.route('/verprojetos')
# def verprojetos() :
#     return render_template("viewproj.html")


# @app.route('/index', methods = ["POST"])

# def index () :
#     conect = sql.connect ('form_db.db')
#     conect.row_factory=sql.Row
#     cursor = conect.cursor()
#     cursor.execute("select * from usuarios")
#     data = cursor.fetchall()
    
#     return render_template('pagina_ptbr/index.html', datas= data)


# @app.route('/criarnovaconta' , methods = ["POST","GET"])
# def criarnovaconta() :


#     if request.method == "POST":
        
#         nome = request.form ['nome']
#         senha = request.form ['senha']


#         conect = sql.connect ('form_db.db')
#         conect.row_factory=sql.Row
#         cursor = conect.cursor()

#         cursor.execute(f"INSERT INTO usuarios (nome,senha) VALUES (?,?)" , (nome,senha))
#         conect.commit()
#         flash("Usuario criado com sucesso!")
#         cursor.close()
#         conect.close()

#         return redirect(url_for('index'))
#     return render_template('pagina_ptbr/criarnovaconta.html')


@app.route('/modifyvalorhora')
def modifyvalorhora () :
    return render_template('pagina_ptbr/modifyvalorhora.html')

@app.route('/tothorasproj')

def tothorasproj () :
    return render_template('pagina_ptbr/tothorasproj.html')

@app.route('/viewproj')
def viewproj() :
    return render_template('pagina_ptbr/viewproj.html')

# @app.route('/novoprojeto')

def novoprojeto () :
    return render_template('pagina_ptbr/novoprojeto.html')

@app.route('/historypag')
def historypag () :
    return render_template("pagina_ptbr/historypag.html")
#--------------------------------------               ROTAS DA PAGINA EM INGLES-------------------------------------------------------------------#


@app.route('/indexenglish', methods = ["POST"])

def indexenglish () :
    conect_DB = mysql.connector.connect(
                host="localhost",
                user = "root",
                password = "",
                database = "usuários"
            )
    if conect_DB.is_connected():
        print("Banco de dados conectado com sucesso")
        cursor = conect_DB.cursor()
        cursor = conect_DB.cursor()
        cursor.execute("select * from usuarios")
        data = cursor.fetchall()
    
    return render_template('pagina_eng/index_english.html', datas= data)


@app.route('/historypagenglish')
def historypagenglish () :
    return render_template("pagina_eng/historypag_english.html")

@app.route('/modifyvalorhoraenglish')
def modifyvalorhoraenglish () :
      return render_template('pagina_eng/modifyvalorhora_english.html')

@app.route('/tothorasprojenglish')

def tothorasprojenglish () :
      return render_template('pagina_eng/tothorasproj_english.html')

@app.route('/viewprojenglish')
def viewprojenglish () :
     return render_template('pagina_eng/viewproj_english.html')

@app.route('/novoprojetoenglish')

def novoprojetoenglish () :
     return render_template('pagina_eng/novoprojeto_english.html')




if __name__ == "__main__" :
    app.run(debug = True)  