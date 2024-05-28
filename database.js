
function connect() {
    const mysql = require('mysql2')
    const connection = mysql.createConnection({
        host: "localhost",
        user: "root",
        password: "",
        database: "horastrabalhadas"

    })
    console.log("conectado com sucesso")
    return connection
}


connect();


function novo_proj() {
    connect()
    const novoproj = { nome:'calculadora' , data:'2024-05-28' , valorhora: 50 , descricao: 'seila' }
    connection.query('INSERT INTO projetos (nome, data, valorhora, descricao) VALUES (?,?,?,?)',
    [novoproj.nome, novoproj.data, novoproj.valorhora, novoproj.descricao], 
    (err, results) => {
        if (err) {
            console.error('Erro ao executar consulta:', err);
            return;
        }
        console.log('Registros da tabela "usuarios":', results.insertId);
    });

 }
 
