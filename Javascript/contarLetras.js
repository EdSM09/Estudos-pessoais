// Função que conta todos caracteres alfabeticos

let texto = "oi"
function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
  }
  

function contarLetras(argument){
    let n = 0
    for(var i = 0; i < argument.length; i++){
        if(isLetter(argument[i])){
            n++
            return n
            }
        }
}

console.log(contarLetras(texto))

