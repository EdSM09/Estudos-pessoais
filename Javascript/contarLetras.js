// Função que conta todos caracteres alfabeticos

texto = ["oi"]

function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
  }
  

function contarLetras(argument){
    for(var i = 0; i < argument.length; i++){
        if(isLetter(argument[i])){
            contador = contador + 1;
            return contador
            }
        }
}


