let altura = 3

function imprimirPiramide(argument){
    for(var i = 0; i < argument; i++){
        for(var j = 1; j <= argument; j++ ){
            console.log(" ");
        }
        for(var j = 1; j <= argument ; j++){
            console.log("#")
        }
    }
}

imprimirPiramide(altura)