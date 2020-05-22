function main(input){
    ab=input.split(' ')
    a=parseInt(ab[0],10)
    b=parseInt(ab[1],10)
    if (b%a==0){
        console.log(a+b)

    }else{
        console.log(b-a)

    }


}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));