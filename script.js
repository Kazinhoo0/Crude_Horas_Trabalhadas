// Esta função, esta implementada no objeto button
//com o objetivo de mudar a cor do site para branco, e consequêntimente preto novamente.
function mudarcor(cordefundo, backimage, divproj, buttonback, buttoncolor, inputwhitecolor, whitelogin) {

  let checkbox = document.getElementById("checkbox");
  let div = document.getElementById("wallpaperbox");
  let divpadproj = document.getElementById("wallpaperpadproj");
  let buttonwhite = document.getElementsByClassName("buttonwhite");
  let inputwhite = document.getElementById("inputwhite")
  let loginwhite = document.getElementById('loginwhite')



  if (checkbox.checked) {
     div.style.backgroundColor = cordefundo;
     div.style.backgroundImage = backimage;
     divpadproj.style.backgroundColor = divproj;
     inputwhite.style.backgroundColor = inputwhitecolor
     loginwhite.style.backgroundColor = whitelogin

     if (buttonwhite.length > 0) {
        for (i = 0; i < buttonwhite.length; i++) {
           buttonwhite[i].style.backgroundColor = buttonback;
           buttonwhite[i].style.color = buttoncolor;
        }
     }
  } else {
     div.style.backgroundColor = '#313131';
     div.style.backgroundImage = 'radial-gradient(#f7f7f744 2px, transparent 0)'
     divpadproj.style.backgroundColor = '#171717'
     inputwhite.style.backgroundColor = '#161616'
     for (i = 0; i < buttonwhite.length; i++) {
        buttonwhite[i].style.backgroundColor = '#272525';
        buttonwhite[i].style.color = '#fff3f3';
     }

  }


}

function mudarcorpopup () {
  let corpopup = document.getElementById('popupid')

 corpopup.style.backgroundColor = "#b4c2c7"
}

function mudarcorpopupleave() {
  let corpopup = document.getElementById('popupid')

   corpopup.style.backgroundColor = "#ffffff"
}


// função para mudar a cor de fundo dos botões do site, quando o usario colocar o cursor em cima.
function mouseenter(backcolor, buttoncolor) {
  let botãocriarconta = document.getElementById('buttoncriarconta');
  let botãovoltarparaomenu = document.getElementById('botãovoltarparaomenu')


     botãovoltarparaomenu.style.backgroundColor = backcolor;
     botãovoltarparaomenu.style.Color = buttoncolor;
     botãocriarconta.style.backgroundColor = backcolor;
     botãocriarconta.style.color = buttoncolor;

}

function mouseenter2 (backcolor,buttoncolor) {
  let botãojatenhoconta = document.getElementById('buttonjatenhoconta');


  botãojatenhoconta.style.backgroundColor = backcolor;
  botãojatenhoconta.style.color = buttoncolor;
}



// função para mudar a cor de fundo dos botões do site, quando o usario tirar o mouse do mesmo.
function mouseleave(backcolor, buttoncolor) {
  let botãocriarconta = document.getElementById('buttoncriarconta');
  let botãojatenhoconta = document.getElementById("buttonjatenhoconta");


     botãocriarconta.style.backgroundColor = backcolor;
     botãocriarconta.style.color = buttoncolor;
     botãojatenhoconta.style.background = backcolor;
     botãojatenhoconta.style.color = buttoncolor;

}

function mouseleave2(backcolor, buttoncolor) {
  let botãojatenhoconta = document.getElementById("buttonjatenhoconta");
     
     botãojatenhoconta.style.background = backcolor;
     botãojatenhoconta.style.color = buttoncolor;

}


// abri o pop do portifólio
function abrirpop_porti(){ 
  var portifólio 

     portifólio = window.open("https://kaualopesmonteiro.netlify.app/");

  }
//abri o pop do github
function abrirpop_github () {
  var github 
  
  github = window.open("https://github.com/Kazinhoo0");
}
//abri o pop do linkedin
function abrirpop_linkd () {
  var linkedin

 linkedin = window.open("https://www.linkedin.com/in/kau%C3%A3-lopes-monteiro-330048214/","width = 1000px ")
}


function fecharPopUps(){

  portifólio.close()
  github.close()
  linkedin.close()


}



// function capturarvalores() {
//   const nomeproj = document.getElementById('nome').value;
//   const valorhoraproj = parseFloat(document.getElementById('valorhora').value);
//   const descricaoproj = document.getElementById('descricao').value;
//   const dataproj = document.getElementById('data').value

//   const novoproj = {
//      nome: nomeproj,
//      data: dataproj,
//      descricao: descricaoproj,
//      valorhora: valorhoraproj
//   };

//   return novoproj;




document.addEventListener('DOMContentLoaded', function() {
  const registrationForm = document.getElementById('registrationForm');
  if (registrationForm) {
    registrationForm.addEventListener('submit', function (event) {
      event.preventDefault(); 

      const nome = document.getElementById('nome').value;
      const senha = document.getElementById('senha').value;

      fetch('http://127.0.0.1:8085/registrar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nome: nome, senha: senha }),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao registrar usuário');
        }
        return response.json();
      })
      .then(data => {
        console.log('Success:', data);
        // Exibir mensagem de sucesso ou redirecionar o usuário
      })
      .catch((error) => {
        console.error('Error:', error);
        // Exibir mensagem de erro
      });
    });
  } else {
    console.error('Elemento com id "registrationForm" não encontrado.');
  }
});


























