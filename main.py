
from flask import Flask, render_template, redirect, request, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kaue182023'


#se o usuário não acessar nenhuma página específica, ira ser direcionado para o index.html
@app.route('/')

def home() :
    return render_template('index.html')


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




if __name__ in "__main__" :
    app.run(debug = True)  