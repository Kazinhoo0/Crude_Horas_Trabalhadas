// import express from 'express';
// import mysql from 'mysql';


// const app = express();
// const port = 8000;

// const con = mysql.createConnection({
//   host: 'localhost',
//   user: 'root',
//   password: "",
//   database: "usuários"
// });

// con.connect((err) => {
//   if (err) {
//     console.error('Erro ao conectar ao banco de dados:', err.stack);
//     return;
//   }
//   console.log('Conectado ao banco de dados.');
// });

// app.use(express.json());

// app.post('/registrar', (req, res) => {
//   const nome = req.body.nome;
//   const senha = req.body.senha;

//   con.query("INSERT INTO usuários_cadastrados (Nome,Senha) VALUES (?,?)", [nome, senha], (err, result) => {
//     if (err) {
//       console.error(err);
//       res.status(500).send("Erro ao inserir dados no banco de dados.");
//     } else {
//       res.send(result);
//     }
//   });
// });

// app.listen(port, () => {
//   console.log(`Servidor iniciado com sucesso na porta ${port}`);
// });


import express from 'express';
import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

const app = express();
const port = 8000;

// Conectar ao banco de dados SQLite
async function connectDB() {
  try {
    const db = await open({
      filename: './database.db',
      driver: sqlite3.Database
    });
    console.log('Conectado ao banco de dados SQLite.');
    return db;
  } catch (error) {
    console.error('Erro ao conectar ao banco de dados:', error);
  }
}

// Criar tabela se não existir
async function createTable() {
  try {
    const db = await connectDB();
    await db.exec(`
      CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        senha TEXT
      )
    `);
    console.log('Tabela criada com sucesso.');
  } catch (error) {
    console.error('Erro ao criar tabela:', error);
  }
}

// Middleware para analisar JSON
app.use(express.json());

// Rota para registrar usuário
app.post('/registrar', async (req, res) => {
  const { nome, senha } = req.body;

  try {
    const db = await connectDB();
    const result = await db.run('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', [nome, senha]);
    console.log('Usuário registrado com sucesso:', result.lastID);
    res.status(200).send('Usuário registrado com sucesso.');
  } catch (error) {
    console.error('Erro ao inserir dados no banco de dados:', error);
    res.status(500).send('Erro ao inserir dados no banco de dados.');
  }
});

// Iniciar o servidor
async function startServer() {
  await createTable();
  app.listen(port, () => {
    console.log(`Servidor iniciado com sucesso na porta ${port}`);
  });
}

startServer();



