// Função que conta todos caracteres alfabeticos

let texto = " a d v"
  

// função está contando letras e espços
function contarLetras(argument){
    let n = 0
    console.log(typeof(argument))

    if( typeof(argument) === 'string' ){
        n = argument.length
        return n
    }

}

let comp = contarLetras(texto)

console.log(comp)

