// definir quantidade de horas 
let horas = 4;


// usar a variável horas para realizar as operações
function converter(argument){
    let minutos = argument * 60;
    let segundos = minutos * 60;
    console.log("equivale a " + minutos + " minutos");
    console.log("equivale a " + segundos + " segundos")
}   
// fazer a chamada da função
converter(horas)