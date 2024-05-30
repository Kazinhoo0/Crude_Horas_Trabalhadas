// função para mudar a cor de fundo do site
function mudarcor(cordefundo) {

   let boxcheck = document.getElementById('wallpaperbox');
   
   if (boxcheck.checked) {

      document.getElementById('wallpaperbox').style.backgroundColor = cordefundo
   } else {
      document.getElementById('wallpaperbox').style.backgroundColor = '#313131'
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




