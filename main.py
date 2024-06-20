
from flask import Flask, render_template, redirect, request, flash , url_for
import mysql.connector
from mysql.connector import Error
from time import sleep



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kaue182023'


#se o usuário não acessar nenhuma página específica, ira ser direcionado para o index.html

@app.route('/indexhome')
def indexhome() :
    return render_template('pagina_ptbr/index.html')

@app.route('/indexhomeenglish')
def indexhomeenglish() :
    return render_template('pagina_eng/index_english.html')

@app.route('/')
def home() :
    return render_template('pagina_ptbr/index.html')

@app.route('/verprojetos')
def verprojetos() :
    return render_template('pagina_ptbr/viewproj.html')



@app.route('/index', methods = ["POST", 'GET'])

def index () :
    nome = request.form.get('nome')
    senha = request.form.get('senha')
  
    if nome == 'adm' and senha == 'Kaua1987231' :
        return render_template('pagina_ptbr/novoprojeto.html')
    

    conect_DB = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "",
        database = "usuários"
    )
    if conect_DB.is_connected():
        print("Banco de dados conectado com sucesso")
        cursor = conect_DB.cursor()
        comando = ("select * from usuarios where nome = %s and senha = %s ")
        cursor.execute(comando, (nome,senha))
        usuario = cursor.fetchone()
        
        conect_DB.close()
        cursor.close()

        if usuario :
            sleep(4.0)
            flash('Login efetuado com sucesso!') 
            return render_template('pagina_ptbr/novoprojeto.html')

        if not usuario :
            flash("Nome de usuario ou senha incorretos!") 
            return redirect(url_for('indexhome'))
        

    return render_template('pagina_ptbr/index.html')



@app.route('/criarnovaconta' , methods= ['POST' , 'GET'])

def criarnovaconta() :
    if request.method == 'POST':
        nome = request.form.get ('nome')
        senha = request.form.get ('senha')
        
        if not nome and not senha:
            flash('O campo Usuário e senha são obrigatorios')
            return render_template('pagina_ptbr/criarnovaconta.html')
        
        if len(senha) < 8 :
            flash('Sua senha precisa ter mais que 8 caracteres,porfavor tente novamente.')
            return redirect(url_for('criarnovaconta') )
            
            
        
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
                conect_DB.commit()
                flash('Conta criada com sucesso!')
                return redirect(url_for('home'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
                
        
        
    return render_template('pagina_ptbr/criarnovaconta.html')  
  

@app.route('/modifyvalorhora', methods = ["POST" , "GET"])
def modifyvalorhora() :
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        novovalor = request.form.get('novovalor')

        
        if not nomeprojeto or not nomeprojeto or not novovalor :
            flash('Os campos nome do projeto e novo valor são obrigatorios!. Por favor, tente novamente.')
            return render_template('pagina_ptbr/modifyvalorhora.html')
 
        try:
            conect_DB = mysql.connector.connect(
                host="localhost",
                user = "root",
                password = "",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("UPDATE usuários.projetos SET valorhora = (%s) WHERE  nome = (%s)")
                cursor.execute(comando, (novovalor,nomeprojeto))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                return redirect(url_for('modifyvalorhora'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
        
    return render_template('pagina_ptbr/modifyvalorhora.html')

@app.route('/tothorasproj' , methods = ['POST' , 'GET'])

def tothorasproj() :
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        novahora = request.form.get('horastrab')

        
        if not nomeprojeto or not nomeprojeto or not novahora :
            flash('Tem algo de errado ai.-. Os campos nome e horas precisam estar preechidos. Por favor, tente novamente..')
            return render_template('pagina_ptbr/tothorasproj.html')
 
        try:
            conect_DB = mysql.connector.connect(
                host="localhost",
                user = "root",
                password = "",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("UPDATE projetos SET valorhora = valorhora + (%s) WHERE nome = (%s)")
                cursor.execute(comando, (novahora,nomeprojeto))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                return redirect(url_for('tothorasproj'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
        
    return render_template('pagina_ptbr/tothorasproj.html')
    
    
    

@app.route('/viewproj')
def viewproj() :
    return render_template('pagina_ptbr/viewproj.html')

@app.route('/novoprojeto', methods = ['POST' , 'GET'])
def novoprojeto() :
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        data = request.form.get ('data')
        valorhora = request.form.get('valorhora')
        descricao = request.form.get('descricao')
        
        
        
        if not nomeprojeto or not data or not valorhora :
            flash('Os campos nome, data e valor/hora são obrigatórios. Por favor, tente novamente.')
            return render_template('pagina_ptbr/novoprojeto.html')
        
        if len(descricao) > 200 :
            flash('Numero máximo de 200 caracteres ultrapassado. Por favor, insira novamente .')
            return redirect(url_for('novoprojeto') )
            
            
        
        try:
            conect_DB = mysql.connector.connect(
                host="localhost",
                user = "root",
                password = "",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("INSERT INTO projetos (nome,data,valorhora,descrição) VALUES (%s,%s,%s,%s)")
                cursor.execute(comando, (nomeprojeto,data,valorhora,descricao))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                return redirect(url_for('novoprojeto'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    
    return render_template('pagina_ptbr/novoprojeto.html')

@app.route('/historypag')
def historypag() :
    return render_template("pagina_ptbr/historypag.html")
#--------------------------------------               ROTAS DA PAGINA EM INGLES-------------------------------------------------------------------#


@app.route('/indexenglish', methods = ["POST"])

def indexenglish() :


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


    return render_template('pagina_eng/index_english.html')


@app.route('/historypagenglish')
def historypagenglish() :
    return render_template("pagina_eng/historypag_english.html")

@app.route('/modifyvalorhoraenglish')
def modifyvalorhoraenglish() :
      return render_template('pagina_eng/modifyvalorhora_english.html')

@app.route('/tothorasprojenglish')

def tothorasprojenglish() :
      return render_template('pagina_eng/tothorasproj_english.html')

@app.route('/viewprojenglish')
def viewprojenglish() :
     return render_template('pagina_eng/viewproj_english.html')

@app.route('/novoprojetoenglish')

def novoprojetoenglish() :
    return render_template('pagina_eng/novoprojeto_english.html')


@app.route('/criarnovacontaenglish')

def criarnovacontaenglish () :
    return render_template('pagina_eng/criarnovaconta_english.html')




if __name__ == "__main__" :
    app.run(debug = True)  