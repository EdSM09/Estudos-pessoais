// uma função pode ser declarada com function verboSubstantivo(argumento) {}
// exemplo a função pickRandom nesse repositório
//exemplo:
// função que toma como argumento numbers em um array e retorna o ressultado das operações aplicadas neles

// definições dos valores dos argumendos dos operandos 
let valorSoma = soma([4, 5]);
let valorSubtração = subtração([45, 562])
let valorMultiplicação = multiplicação([2, 75])
let valorDivisão = divisão([45, 15])
let valorExponenciação= exponenciação([10, 2])

// print dos valores dos resultados das operações 
console.log(valorSoma);
console.log(valorSubtração);
console.log(valorMultiplicação);
console.log(valorDivisão);


// função soma
function soma(argument ){
    return argument[0] + argument[1];
}
// função subtração
function subtração(argument) {
    return argument[0] - argument[1];
}

// função de multiplicação 
function multiplicação(argument) {
    return argument[0]*argument[1];
}

// função de divisão
function divisão(argument) {
    return argument[0]/argument[1];
}

// funções de exponenciação 
function exponenciação(argument) {
    return argument[0] ** argument[1];
}

    
