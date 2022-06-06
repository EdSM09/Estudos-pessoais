// versão mais complexa do converter
// ela pode tomar como argumento dias, horas, minutos como argumento

let dias = 5;
let horas = 2;
let minutos = 3;


function converterDias(argument){
     let horas = argument * 24;
     let minutos = horas * 60;
     let segundos = minutos * 60;
     console.log("Equivalem a: "+ horas + " horas, " + minutos + " minutos, e "+ segundos + " segundos.")
}    
function converterHoras(argument){
    let minutos = argument * 60;
    let segundos = minutos * 60;
    console.log("Equivalem a: " + minutos + " minutos e " + segundos + " segundos.")
}
function converterMinutos(argument){
    let segundos = argument * 60;
    console.log("Equivalem a: "+segundos + " segundos.");
}

console.log(" ")
console.log("Conversão dos dias: ")
if(dias > 0);{
    converterDias(dias)
}

console.log(" ")
console.log("Conversão das horas:")
if(horas > 0);{
    converterHoras(horas)
}
console.log(" ")
console.log("Conversão dos minutos")
if(minutos > 0);{
    converterMinutos(minutos)
}


