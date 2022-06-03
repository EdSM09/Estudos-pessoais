// A declaração do...while cria um laço que executa uma declaração até que o teste da condição for falsa (false). A condição é avaliada depois que o bloco de código é executado, resultando que uma declaração seja executada pelo menos uma vez.
// exemplo:

// var resultado = doWhile([1,2,3,4,5,6,7,8,9,10]);
// console.log(resultado)





// function doWhile(argument){
//     let i = 0;
//     do{
//         console.log(argument[i] + argument[i + 1]);
//         i++;
//     }
//     while( i < argument.length)
// }

let num = [1,2,3,4,5,6,7,8,9,10];
var soma = 0;
i = 0;

do {
    soma  = num[i] + num[i + 1]
    i += 1;
    console.log(soma);
} while(i < num.length - 1)