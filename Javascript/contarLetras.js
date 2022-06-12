// Função que conta todos caracteres alfabeticos

let texto = ["oi eu sou o goku"]
function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
  }
  

  // A função está devolvendo um número  porém não o número certo

function contarLetras(argument){
    let n = 0
    if( typeof(argument) === 'string' )
        for(var i = 0; i < argument.length; i++){
            if(isLetter(argument[i])){
                n++
                return n
                }
            }
}

console.log(contarLetras(texto))

