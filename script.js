const express = require('express')
import mysql from 'mysql';

const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: "",
  database: "usuários"
});


const app = express();
const port = 8000



app.post('/registrar', (req, res) => {
  const nome = req.body.nome;
  const senha = req.body.senha;
  con.query("INSERT INTO usuários (nome,senha) VALUES (?,?)", [nome, senha], (err, result) => {
    if (err) {
      console.error(err)
      res.status(500).send("Erro ao inserir dados no banco de dados.");
    } else {
      res.send(result)
    }

  })
})

app.listen(port, () => {
  console.log("Servidor iniciado com sucesso!")
})





















//  async function Criareregistrarusuarios() {

//   //   let nome = document.getElementById('nome').value
//   //   let senha = document.getElementById('senha').value

//   const db = await open ({
//  filename: './banco.db',
// driver: sqlite3.Database,
// });

//   //   await db .run(
//   //       'CREATE TABLE IF NOT EXISTS usuarios ( id INTEGER PRIMARY KEY, nome TEXT)'
//   //   );
//   //    await db.run (
//   //        'INSERT INTO usuarios (nome,senha) VALUES (?,?)' , [nome , senha]
//   //   );

//   //   console.log('Usuário registrado com sucesso!!');
//   // }



















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




