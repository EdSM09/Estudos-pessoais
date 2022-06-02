// um loop servem para encurtar tarefas repetitivas 
// basicamente, se inicia um loop com um contador, uma condição de saida, e um interador
// exempplo:

// definir uma variavel com um array
let num = [0,1,2,3,4,5,6,7,8,9,10];

//inicializar um loop onde i = 0 e menor que o comprimento do array menos 1

for(var i = 0; i < num.length - 1; i++) {
    //printar a soma dos numeros em pares
    console.log(num[i] + num[i + 1]);
}




