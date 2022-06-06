// versão mais complexa do converter
// ela pode tomar como argumento dias, horas, minutos como argumento

let dias = 1
let horas = 0
let minutos = 0


function converter(argument){
     horas = dias * 24;
     minutos = argument * 60;
     segundos = minutos * 60;
    //  console.log("equivale a " + horas + " horas");
    //  console.log("equivale a " + minutos + " minutos");
    //  console.log("equivale a " + segundos + " segundos");
}

if(dias > 0);{
    console.log("equivale a " + converter(dias) + " horas");}
if (horas > 0 );{
    console.log("equivale a " + converter(horas) + " minutos");}
if(minutos > 0 );{
    console.log("equivale a " + converter(minutos) + " segundos");}