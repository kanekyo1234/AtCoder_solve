function main(input){
    tx=input.split(' ')
    t=parseInt(tx[0],10)
    x=parseInt(tx[1],10)
    console.log(t/x)

}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));