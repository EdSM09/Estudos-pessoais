// fizzbuzz é um desaffio básico que engloba varios conceitos da programação
// pseudocode:

// se o numero entre 1 e 100 for divisivel por 3 e 5
//      imprima fizzbuzz
// se o número for divisivel por 3
//      imprima fizz
// se o numero dor divisivel por 5 
//      imprima buzz
// se nenhuma delas for satisfeita 
//      imprima o número 

for(var i = 0; i < 101; i++){
    if( i % 3 === 0 && i % 5 === 0){
        console.log("FizzBuzz");
    }
    else if(i % 3 == 0){
        console.log("Buzz");
    }  
    else if(i % 5 === 0){
        console.log("Fizz")
    }
    else{
        console.log(i)
    }
}