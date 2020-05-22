#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,c;
    string b;
    cin >> a>>b>>c;
    //cout <<a << c;
    if (b=="+"){
        cout << a+c;
    }else{
        cout << a-c;
    }

    return 0;
}