
function main(input){
    input=input.split(' ');
    x=parseInt(input[0],10)
    if (x==3 ||x==5 || x==7){
        console.log("YES")
    }else{
        console.log("NO")
    }


}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
function main(input){
    abc=input.split(' ');
    abc=abc.sort();
    a='';
    a+=abc[2];
    a+=abc[1];
    a=parseInt(a,10);
    b=parseInt(abc[0],10);
    console.log(a+b);
    


}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));
