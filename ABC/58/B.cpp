#include <bits/stdc++.h>
using namespace std;

int main() {
    string a,b;
    cin >> a >> b ;
    if (a.length()>b.length()){
        for (int i=0;i<b.length();i++){
            cout << a[i] << b[i];
        }
        cout << a[a.length()-1] <<endl;
    }else{
        for (int i=0;i<b.length();i++){
            cout << a[i] << b[i];
        }
    }
    return 0;
}