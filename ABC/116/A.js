
function main(input){
    abc=input.split(' ');
    //console.log(abc)
    ab=parseInt(abc[0],10)
    bc=parseInt(abc[1],10)
    console.log(ab*bc/2)
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));