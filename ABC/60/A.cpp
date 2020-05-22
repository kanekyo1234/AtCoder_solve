#include <bits/stdc++.h>
using namespace std;

int main() {
    string a,b,c;
    cin >> a >> b >> c;
    if(a[a.length()-1]==b[0] && c[0]==b[b.length()-1]){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    return 0;
}