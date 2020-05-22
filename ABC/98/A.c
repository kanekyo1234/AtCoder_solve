#include <stdio.h>

int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    int ans=a+b;
    if (ans<a-b){
        ans=a-b;
    }
    if(ans<a*b){
        ans=a*b;
    }
    printf("%d",ans);
    return 0;
}