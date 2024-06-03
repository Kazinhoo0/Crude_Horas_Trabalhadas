// função para mudar a cor de fundo do site
function mudarcor(cordefundo,backimage,divproj,buttonback,buttoncolor,inputwhitecolor,whitelogin) {

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
         inputwhite.style.backgroundColor= inputwhitecolor
         loginwhite.style.backgroundColor = whitelogin

            if ( buttonwhite.length > 0) {
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



function capturarvalores () {
   const nomeproj = document.getElementById('nome').value;
   const valorhoraproj = parseFloat(document.getElementById('valorhora').value);
   const descricaoproj = document.getElementById('descricao').value;
   const dataproj = document.getElementById('data').value

   const novoproj = {
      nome: nomeproj,
      data: dataproj,
      descricao: descricaoproj,
      valorhora: valorhoraproj
   };

   return novoproj;
}




