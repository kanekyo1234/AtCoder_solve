#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,a,b;
    cin >> x >> a >> b ;
    if (abs(x-a)>abs(x-b)){
        printf("B");
    }else{
        printf("A");
    }

    return 0;
}
