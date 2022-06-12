// Função que conta todos caracteres alfabeticos


let texto = "teste a"
  
function contarLetras(argument){
    let n = 0 // variável local que armazena o comprimento total da string
    let s = 0 // variável que armazena o número de espaços

    for(var i= 0; i < argument.length; i++) // para todo o comprimento do argumento
        if( typeof(argument) === 'string' ){ // se o argumento for uma string execute o seguinte
            n = argument.length // incrementar um valor a essa variável
            if (argument[i] === " "){ // dar consideração aos espaços
                s++ // incrementar ao valor 
        } 
        return n - s // devolver o valor total de caracteres dentro da string
    }
}
if (typeof(texto) === 'string'){
    console.log(contarLetras(texto))
}
// medida de controle
if(typeof(texto) !== 'string'){
    console.log("INSIRA UMA STRING")

}
