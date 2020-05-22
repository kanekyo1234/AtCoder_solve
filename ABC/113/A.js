
function main(input){
    abc=input.split(' ');
    a=parseInt(abc[0],10)
    b=parseInt(abc[1],10)
    console.log(a+b/2) 

}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));