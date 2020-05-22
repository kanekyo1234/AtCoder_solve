#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    string s;
    cin >> a >> b;
    cin >> s;
    bool flag=true;

    for(int i=0;i<a;i++){
        if(s[i]=='-'){
            flag=false;
        }
    }
    //cout << flag << endl;

    if (s[a]!='-'){
        flag=false;
    }
    //cout << flag << endl;

    for(int i=a+1;i<b+a+1;i++){
        if(s[i]=='-'){
            flag=false;
        }
    }
    //cout << flag << endl;
    if (flag==true){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
