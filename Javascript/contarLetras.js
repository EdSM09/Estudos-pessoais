// Função que conta todos caracteres alfabeticos
function contarLetras(argument){
    
    if(typeof argument === 'string'){
        argument = argument.toLowerCase();
        let contador = 0
        for(var i = 0; i < argument.length; i++){
            if(argument[i] == ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']){
                contador+= 1;
                return contador;
            }
        }
    }

}



texto = "oi"
console.log(contarLetras(texto))
