#include <bits/stdc++.h>
using namespace std;
int main() {
    int a,b,c;
    cin >> a >> b >> c;
    vector <int> s{a,b,c};
    int a5,a7=0;
    for (int i=0;i<3;i++){
        if (s[i]==5){
            a5+=1;
        }
        if (s[i]==7){
            a7+=1;
        }
    }
        if (a5==2 && a7==1){
            cout << "YES"<< endl;
        }else{
            cout << "NO" << endl;
        }
    
    return 0;
}