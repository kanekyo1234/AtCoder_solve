
function main(input){
    abc=input.split(' ');
    abc=abc.sort();
    a=parseInt(abc[2],10)
    b=parseInt(abc[1],10)
    c=parseInt(abc[0],10)
    console.log(a*10+b+c)
    


}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));