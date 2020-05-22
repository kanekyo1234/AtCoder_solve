#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    int ba=0;
    cin >>a;
    int n=a;
    while (n!=0) {
        ba+=n%10;
        n/=10;
    }
    if(a%ba==0){
        cout << "Yes" <<endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}
