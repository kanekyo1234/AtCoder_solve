
function main(input){
    d=input.split('');
    //console.log(d)
    a='';
    for (var i=0;i<3;i++){
        a+=10-d[i];
    }
    console.log(a);


}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));