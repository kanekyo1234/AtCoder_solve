#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,a;
    int count=0;
    cin >> n >> a;
    count+=n%500;
    //cout << count <<" "<< a << endl;
    if (count<=a){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
