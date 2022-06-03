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
    // para i menor que 101 sera executado

    // se o numero i for tanto divisivel por 5 e 3
    if( i % 3 === 0 && i % 5 === 0){
        console.log("FizzBuzz");  // imprima FizzBuzz
    }
    
    // se o número i for divisível por 3
    else if(i % 3 == 0){
        console.log("Buzz");  // imprima Buzz
    }  

    // se o número i for divisível por 
    else if(i % 5 === 0){
        console.log("Fizz");  //imprima Fizz
    }
    else{
        console.log(i);  //imprima o número i
    }
}