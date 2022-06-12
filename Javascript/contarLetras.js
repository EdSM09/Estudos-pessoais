// Função que conta todos caracteres alfabeticos


let texto = "éôÃ"
  

// função está contando letras e espaços 
// tentando remmover os espaços
function contarLetras(argument){
    let n = 0
    let s = 0
    console.log(typeof(argument))
    for(var i= 0; i < argument.length; i++)
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

