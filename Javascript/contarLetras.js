// Função que conta todos caracteres alfabeticos
function contarLetras(argument){
    
    if(argument === string){
        argument = argument.toLowerCase();
        let contador = 0
        for(var i = 0; i < argument.length; i++){
            if( argument[i].isAlpha()){
                contador+= 1;
            }
        }
    }

}



texto = "oi"
console.log(contarLetras(texto))
