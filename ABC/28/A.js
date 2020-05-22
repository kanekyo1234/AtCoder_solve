function main(input) {
    a=input.split(' ')
    if (a==100){
        console.log("Perfect")
    }else if(90<=a){
        console.log("Great")
    }else if(60<=a){
        console.log("Good")
    }else{
        console.log("Bad")
    }
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));