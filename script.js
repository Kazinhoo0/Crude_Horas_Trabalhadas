// função para mudar a cor de fundo do site
function mudarcor() {

   var checkbox = document.getElementById('wallpaperbox');

   if (checkbox.checked = true) {
      document.getElementById('wallpaperbox').style.backgroundColor = '#ffffff'
   } else {
      document.getElementById('wallpaperbox').style.backgroundColor = '#252525'
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




