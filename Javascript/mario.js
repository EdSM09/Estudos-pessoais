// imprimir uma piramide igual ao do mario
// uma adaptação de um problem set do Curso CS50

// pegar uma int para definir a altura da piramide
let altura = 5

// fazer uma função imprimirPiramide
// repetir pela colunas e linhas 

function imprimirPiramide(argument){
    for (var i = 1; i <= argument; i++) {
        var row = '';
    
        for (var j = 1; j <= i; j++) {
          row += '*';
        }
    
        console.log(row);
      }
    }

imprimirPiramide(altura)
