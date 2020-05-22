#include <bits/stdc++.h>
using namespace std;

int main() {
    string a;
    cin >> a ;
    vector <int> s(26);
    
    for(int i=0;i<a.length();i++){
        s[a[i]-'a']+=1;
    }
    bool jugh=true;
    for (int i=0;i<26;i++){
        if (s[i]%2!=0){
            jugh=false ;
        }
    }
    if (jugh){
        cout << "Yes" ;
    }else{
        cout << "No";
    }
    return 0;
}