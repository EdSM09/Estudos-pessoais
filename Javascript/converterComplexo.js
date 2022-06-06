// versão mais complexa do converter


// definir os valores a serem transformados
let dias = 5;
let horas = 2;
let minutos = 3;


// função para converter dias para horas, minutos e segundos
function converterDias(argument){
     let horas = argument * 24;
     let minutos = horas * 60;
     let segundos = minutos * 60;
     console.log("Equivalem a: "+ horas + " horas, " + minutos + " minutos, e "+ segundos + " segundos.")
}    

// função para converter horas em minutos e segundos
function converterHoras(argument){
    let minutos = argument * 60;
    let segundos = minutos * 60;
    console.log("Equivalem a: " + minutos + " minutos e " + segundos + " segundos.")
}

// função para converter minutos em segundos
function converterMinutos(argument){
    let segundos = argument * 60;
    console.log("Equivalem a: "+segundos + " segundos.");
}


// condições para execultar as funções

if(dias > 0);{
    console.log(" ")
    console.log("Conversão dos dias: ")
    converterDias(dias)
}

if(horas > 0);{
    console.log(" ")
    console.log("Conversão das horas:")
    converterHoras(horas)
}
if(minutos > 0);{
    console.log(" ")
    console.log("Conversão dos minutos")
    converterMinutos(minutos)
}


