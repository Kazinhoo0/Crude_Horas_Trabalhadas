import sqlite3 from 'sqlite3';
import {open} from 'sqlite';


  
  

  const sqlite = require('sqlite');
  const sqlite3 = require('sqlite3');
  const express = require('express');
  const app = express();
  
  app.use(express.json());
  
  app.post('/registrar', async (req, res) => {
      const nome = req.body.nome;
      const senha = req.body.senha;

      const db = await open ({
        filename: './banco.db',
       driver: sqlite3.Database,
       });
  
      await db.run(
          'CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, senha TEXT)'
      );
      await db.run(
          'INSERT INTO usuarios (nome, senha) VALUES (?, ?)', [nome, senha]
      );
  
      res.send('Usuário registrado com sucesso!!');
  });
  
  app.listen(3000, () => {
      console.log('Servidor rodando na porta 3000');
  });




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




