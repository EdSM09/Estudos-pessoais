// Função que conta todos caracteres alfabeticos


let texto = "asasas"
  
function contarLetras(argument){
    let n = 0 // variável local que armazena o comprimento total da string
    let s = 0 // variável que armazena o número de espaços

    for(var i= 0; i < argument.length; i++) // para todo o comprimento do argumento
        if( typeof(argument) === 'string' ){
            n = argument.length
            if (argument[i] === " "){
                s = s + 1

        }
        return n - s
    }

}

let comp = contarLetras(texto)

console.log(comp)

