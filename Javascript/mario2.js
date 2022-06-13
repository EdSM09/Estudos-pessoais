let altura = 10

function imprimirPiramide(altura){
    for(var i = 0; i < altura; i++){
        for(var j = 1; j <= altura; j++ ){
            console.log(" ");
        }
        for(var j = 1; j <= altura - 1; j++){
            console.log("#")
        }
    }
}