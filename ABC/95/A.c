#include<stdio.h>

int main(){
    char c[10];
    int all=700;
    scanf("%s",c);
	for (int i = 0; i < 3; i++){
        if (c[i] == 'o'){
			all += 100;
        }
	}
	printf("%d", all);
 
    return 0;
}
 
