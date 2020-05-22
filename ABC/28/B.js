function main(input) {
    a=input
    A=a.split('A').length-1
    B=a.split('B').length-1
    C=a.split('C').length-1
    D=a.split('D').length-1
    E=a.split('E').length-1
    F=a.split('F').length-1

    console.log(A+" "+B+" "+C+" "+D+" "+E+" "+F)
    

}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));