
function main(input){
    d=input;
    var a=["Christmas","Christmas Eve","Christmas Eve Eve","Christmas Eve Eve Eve"];
    var b=[25,24,23,22]
    for (var i = 0;i<4;i++){
        if (d==b[i]){
            console.log(a[i])
        }
    }
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));