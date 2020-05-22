#include <bits/stdc++.h>
using namespace std;

int main() {
    int m,vv;
    cin >> m;
    if( m < 100){
        vv = 0;
    }
    if( m >= 100 && m <= 5000 ){
        vv = m*0.001*10;
    }
    if( m >= 6000 && m <= 30000 ){
        vv = m*0.001 + 50;
    }
    if( m >= 35000 && m <= 70000 ){
        vv = (m*0.001 - 30)/5 + 80;
    }
    if( m > 70000 ){
        vv = 89;
    }
    printf("%02d\n",vv);
    return 0;
}
