import sqlite3 from 'sqlite3';
import {open} from 'sqlite';



async function Criareregistrarusuarios(usuario,senha) {
    const db = await open ({
        filename: './banco.db',
        driver: sqlite3.Database,

    });

    await db.run(
        'CREATE TABLE IF NOT EXISTS usuarios ( id INTEGER PRIMARY KEY, nome TXT)'
    );

    await db.run (
        'INSERT INTO usuarios (nome,senha) VALUES (?,?)' , [usuario,senha]
    )

}

Criareregistrarusuarios('josé','15144788adwad');





















// function connect() {
//     const mysql = require('mysql2')
//     const connection = mysql.createConnection({
//         host: "localhost",
//         user: "root",
//         password: "",
//         database: "horastrabalhadas"

//     })
//     console.log("conectado com sucesso")
//     return connection
// }





// function novo_proj() {
//     const connection = connect()
//     novoproj = capturarvalores()
//     const novoproj = { nome:'calculadora' , data:'2024-05-28' , valorhora: 50 , descricao: 'seila' }
//     connection.query('INSERT INTO projetos (nome, data, valorhora, descricao) VALUES (?,?,?,?)',
//     [novoproj.nome, novoproj.data, novoproj.valorhora, novoproj.descricao], 
//     (err, results) => {
//         if (err) {
//             console.error('Erro ao executar consulta:', err);
//             return;
//         }
//         console.log('Registros da tabela "usuarios":', results.insertId);
//     });

//  }
 
