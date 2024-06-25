
from flask import Flask, render_template, redirect, request, flash , url_for , session
import mysql.connector
from mysql.connector import Error
from time import sleep

def dormir():
    return sleep(3.0)

app = Flask(__name__)
app.secret_key = 'Kaelsd20031811'


#se o usuário não acessar nenhuma página específica, ira ser direcionado para o index.html

@app.route('/indexhome')
def indexhome() :
    dormir()
    return render_template('pagina_ptbr/index.html')

@app.route('/')
def home() :
    dormir()
    return render_template('pagina_ptbr/index.html')

@app.route('/viewproj')
def viewproj() :
    if 'usuario_id' not in session :
        flash('Por favor, faça login para poder ver seus projetos.')
        return redirect(url_for('indexhome'))
    
    usuario_id = session['usuario_id']
    
    conect_DB = mysql.connector.connect(
        host="192.168.0.117",
        user = "teste_conexao",
        password = "123456",
        database = "usuários"
    )

    if conect_DB.is_connected():
        cursor = conect_DB.cursor()
        comando = ("SELECT id, nome FROM projetos WHERE usuario_id = %s")
        cursor.execute(comando, (usuario_id,))
        projetos = cursor.fetchall()
        
        cursor.close()
        conect_DB.close()
        dormir()
    
        return render_template('pagina_ptbr/viewproj.html', projetos = projetos)
    
    flash('Erro ao conectar com o banco de dados.')
    return redirect(url_for('indexhome'))




@app.route('/index', methods = ["POST", 'GET'])

def index () :
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
  
        if nome == 'adm' and senha == '123' :
            return render_template('pagina_ptbr/novoprojeto.html')
        

        conect_DB = mysql.connector.connect(
            host="192.168.0.117",
            user = "teste_conexao",
            password = "123456",
            database = "usuários"
        )
        if conect_DB.is_connected():
            print("Banco de dados conectado com sucesso")
            cursor = conect_DB.cursor()
            comando = ("select id from usuarios where nome = %s and senha = %s ")
            cursor.execute(comando, (nome,senha))
            usuario = cursor.fetchone()
            
            conect_DB.close()
            cursor.close()

            if usuario :
                session['usuario_id'] = usuario[0]
                flash('Login efetuado com sucesso!')
                dormir() 
                return render_template('pagina_ptbr/novoprojeto.html')

            if not usuario :
                flash("Nome de usuario ou senha incorretos!") 
                dormir()
                return redirect(url_for('indexhome'))
            
        dormir()
        return render_template('pagina_ptbr/index.html')
    else: 
        return render_template(url_for('indexhome'))
    
    
    
@app.route('/logoff' , methods = ['POST' , 'GET'])  

def logoff () :
    
    if 'usuario_id' in session :
        session.pop('usuario_id', None)
        flash('Sessão finalizada!')
    
    dormir()
    return redirect(url_for('indexhome'))




@app.route('/criarnovaconta' , methods= ['POST' , 'GET'])

def criarnovaconta() :
    if request.method == 'POST':
        nome = request.form.get ('nome')
        senha = request.form.get ('senha')
        
        if not nome or not senha:
            flash('O campo Usuário e senha são obrigatorios')
            dormir()
            return render_template('pagina_ptbr/criarnovaconta.html')
        
        if len(senha) < 8 :
            flash('Sua senha precisa ter mais que 8 caracteres,porfavor tente novamente.')
            dormir()
            return redirect(url_for('criarnovaconta') )
            
            
        
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso")
                cursor = conect_DB.cursor()
                comando = ("INSERT INTO usuarios (nome,senha) VALUES (%s,%s)")
                cursor.execute(comando, (nome , senha))
                conect_DB.commit()
                dormir()
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
    
    if 'usuario_id' not in session:
        flash('Por favor, faça login ou crie uma conta, para acessar essa página')
        print('Usuário não cadastrado')
        return redirect(url_for('indexhome'))     
    
    
    
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        novovalor = request.form.get('novovalor')

        
        if not nomeprojeto or not novovalor :
            flash('Os campos nome do projeto e novo valor são obrigatorios!. Por favor, tente novamente.')
            return render_template('pagina_ptbr/modifyvalorhora.html')
 
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("UPDATE usuários.projetos SET valorhora = (%s) WHERE  nome = (%s)")
                cursor.execute(comando, (novovalor,nomeprojeto))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                dormir()
                return redirect(url_for('modifyvalorhora'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    dormir() 
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
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("UPDATE projetos SET valorhora = valorhora + (%s) WHERE nome = (%s)")
                cursor.execute(comando, (novahora,nomeprojeto))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                dormir()
                return redirect(url_for('tothorasproj'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    dormir()  
    return render_template('pagina_ptbr/tothorasproj.html')
    
    
    


@app.route('/novoprojeto', methods = ['POST' , 'GET'])
def novoprojeto() :
    
    if 'usuario_id' not in session:
        flash('Por favor, faça login para criar um projeto.')
        return redirect(url_for('indexhome'))
    
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        data = request.form.get ('data')
        valorhora = request.form.get('valorhora')
        descricao = request.form.get('descricao')
        usuario_id = session['usuario_id']
        
        
        
        if not nomeprojeto or not data or not valorhora :
            flash('Os campos nome, data e valor/hora são obrigatórios. Por favor, tente novamente.')
            return render_template('pagina_ptbr/novoprojeto.html')
        
        if len(descricao) > 200 :
            flash('Numero máximo de 200 caracteres ultrapassado. Por favor, insira novamente .')
            return redirect(url_for('novoprojeto') )
            
            
        
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando ="""INSERT INTO projetos (nome,data,valorhora,descricao,usuario_id) VALUES (%s , %s , %s , %s , %s)"""
                cursor.execute(comando, (nomeprojeto,data,valorhora,descricao, usuario_id))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                dormir()
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


@app.route('/indexhomeenglish')
def indexhomeenglish() :
    dormir()
    return render_template('pagina_eng/index_english.html')


@app.route('/indexenglish', methods = ["POST"])

def indexenglish() :


    conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
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
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        novahora = request.form.get('horastrab')

        
        if not nomeprojeto or not nomeprojeto or not novahora :
            flash('Tem algo de errado ai.-. Os campos nome e horas precisam estar preechidos. Por favor, tente novamente..')
            return render_template('pagina_ptbr/tothorasproj.html')
 
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("UPDATE projetos SET valorhora = valorhora + (%s) WHERE nome = (%s)")
                cursor.execute(comando, (novahora,nomeprojeto))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                dormir()
                return redirect(url_for('tothorasproj'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    dormir()  
    return render_template("pagina_eng/historypag_english.html")

@app.route('/modifyvalorhoraenglish')
def modifyvalorhoraenglish() :
       
       
    if 'usuario_id' not in session:
        flash('Por favor, faça login ou crie uma conta, para acessar essa página')
        print('Usuário não cadastrado')
        return redirect(url_for('indexhome'))     
    
    
    
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nomeprojeto')
        novovalor = request.form.get('novovalor')

        
        if not nomeprojeto or not novovalor :
            flash('Os campos nome do projeto e novo valor são obrigatorios!. Por favor, tente novamente.')
            return render_template('pagina_ptbr/modifyvalorhora.html')
 
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando = ("UPDATE usuários.projetos SET valorhora = (%s) WHERE  nome = (%s)")
                cursor.execute(comando, (novovalor,nomeprojeto))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                dormir()
                return redirect(url_for('modifyvalorhora'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    dormir() 
    return render_template('pagina_eng/modifyvalorhora_english.html')

@app.route('/tothorasprojenglish')

def tothorasprojenglish() :
      
    if 'usuario_id' not in session:
        flash('Please create a account or login a account existing')
        print('UserNotfound')
        return redirect(url_for('indexhomeenglish'))
    
    if 'usuario_id' in session:

        nomeprojeto = request.form.get = ('nomeprojeto')
        novovalor = request.form.get = ('novovalor')
    
    try:
        conect_DB = mysql.connector.connect(
            host="192.168.0.117",
            user = "teste_conexao",
            password = "123456",
            database = "usuários"
        )
        if conect_DB.is_connected():
            print("Banco de dados conectado com sucesso!")
            cursor = conect_DB.cursor()
            comando = ("UPDATE projetos SET valorhora = valorhora + (%s) WHERE nome = (%s)")
            cursor.execute(comando, (novovalor,nomeprojeto))
            conect_DB.commit()
            flash('Projeto registrado com sucesso!')
            dormir()
            return redirect(url_for('modifyvalorhora'))
    except Error as e:
        print(f'Erro {e} ao se conectar com banco de dados!')
        flash(f'Erro {e} , por favor tente novamente mais tarde')
    
    
    finally:
        if conect_DB and conect_DB.is_connected :
            cursor.close()
            conect_DB.close()




    dormir()  
    return render_template('pagina_eng/tothorasproj_english.html')

@app.route('/viewprojenglish')
def viewprojenglish() :
     
    if 'usuario_id' not in session :
        flash('Por favor, faça login para poder ver seus projetos.')
        return redirect(url_for('indexhome'))
    
    usuario_id = session['usuario_id']
    
    conect_DB = mysql.connector.connect(
        host="192.168.0.117",
        user = "teste_conexao",
        password = "123456",
        database = "usuários"
    )

    if conect_DB.is_connected():
        cursor = conect_DB.cursor()
        comando = ("SELECT id, nome FROM projetos WHERE usuario_id = %s")
        cursor.execute(comando, (usuario_id,))
        projetos = cursor.fetchall()
        
        cursor.close()
        conect_DB.close()
        dormir()
    
        return render_template('pagina_ptbr/viewproj.html', projetos = projetos)
    
    flash('Erro ao conectar com o banco de dados.')
    return redirect(url_for('indexhome'))

@app.route('/novoprojetoenglish')

def novoprojetoenglish() :
    
    if 'usuario_id' not in session:
        flash('Por favor, faça login para criar um projeto.')
        return redirect(url_for('indexhome'))
    
    
    if request.method == 'POST':
        nomeprojeto = request.form.get ('nameproject')
        data = request.form.get ('data')
        valorhora = request.form.get('valorhora')
        descricao = request.form.get('descricao')
        usuario_id = session['usuario_id']
        
        
        
        if not nomeprojeto or not data or not valorhora :
            flash('Os campos nome, data e valor/hora são obrigatórios. Por favor, tente novamente.')
            return render_template('pagina_ptbr/novoprojeto.html')
        
        if len(descricao) > 200 :
            flash('Numero máximo de 200 caracteres ultrapassado. Por favor, insira novamente .')
            return redirect(url_for('novoprojeto') )
            
            
        
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso!")
                cursor = conect_DB.cursor()
                comando ="""INSERT INTO projetos (nome,data,valorhora,descricao,usuario_id) VALUES (%s , %s , %s , %s , %s)"""
                cursor.execute(comando, (nomeprojeto,data,valorhora,descricao, usuario_id))
                conect_DB.commit()
                flash('Projeto registrado com sucesso!')
                dormir()
                return redirect(url_for('novoprojeto'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    dormir()
    return render_template('pagina_eng/novoprojeto_english.html')


@app.route('/criarnovacontaenglish')

def criarnovacontaenglish () :
    
    if request.method == 'POST':
        nome = request.form.get ('nome')
        senha = request.form.get ('senha')
        
        if not nome or not senha:
            flash('O campo Usuário e senha são obrigatorios')
            dormir()
            return render_template('pagina_ptbr/criarnovaconta.html')
        
        if len(senha) < 8 :
            flash('Sua senha precisa ter mais que 8 caracteres,porfavor tente novamente.')
            dormir()
            return redirect(url_for('criarnovaconta') )
            
            
        
        try:
            conect_DB = mysql.connector.connect(
                host="192.168.0.117",
                user = "teste_conexao",
                password = "123456",
                database = "usuários"
            )
            if conect_DB.is_connected():
                print("Banco de dados conectado com sucesso")
                cursor = conect_DB.cursor()
                comando = ("INSERT INTO usuarios (nome,senha) VALUES (%s,%s)")
                cursor.execute(comando, (nome , senha))
                conect_DB.commit()
                dormir()
                flash('Conta criada com sucesso!')
                return redirect(url_for('home'))
                
        except Error as e :
            print(f'Erro ao conectar ou operar no banco de dados: {e}')
            flash('Erro ao criar conta. Por favor, tente novamente. ')        
        
        finally:   
            if conect_DB and conect_DB.is_connected():
                cursor.close()
                conect_DB.close()
    
    dormir()
    return render_template('pagina_eng/criarnovaconta_english.html')




if __name__ == "__main__" :
    app.run(debug=True)  



