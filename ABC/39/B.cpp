#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;
    cin >> x ;
    //cout << x ;
    for (int i=1;i<1001;i++){
        if (pow(i,4)==x){
            cout << i;
            break;
        }
    }
    return 0;
}