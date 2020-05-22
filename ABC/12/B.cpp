

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[3];
    a[0]=n/3600;
    n=n%3600;
    a[1]=n/60;
    n=n%60;
    a[2]=n;
    for(int i=0; i<3;i++){
        if(a[i]>=10){
            cout << a[i];
        }else{
            cout << "0" << a[i] ;
        }
        if(i != 2){
            cout << ":";
        }
    }
    return 0;
}
