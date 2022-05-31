// Defirnir uma variável como um array de dois valores
// Usar uma função para randomizar o resultado. Dessa forma existe uma probabilidade de 50% cada.
let semaforo = pickRandom( ["vermelho", "verde"]);
// Se o valor de semaforo for "verde" será exibida a mensagem "Você pode passar"
if(semaforo == "verde"){
    console.log('Você pode passar')
}
// Caso contrário, será exibida a mensagem "PARE"
else{
    console.log('PARE')
}

// Função pickRandom 
function pickRandom(argument) {
    if (typeof argument === 'number') {
      return Math.floor(Math.random() * Math.floor(argument)) + 1;
    }
    if (Array.isArray(argument)) {
      return argument[Math.floor(Math.random() * argument.length)];
    }
  }

    