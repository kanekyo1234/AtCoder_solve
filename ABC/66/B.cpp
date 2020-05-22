#include <bits/stdc++.h>
using namespace std;

int main() {
    string s,s1,s2;
    cin >> s;
    for(int i=s.length()-2;i>=2;i-=2){
        s1=s.substr(0,i/2);
        s2=s.substr(i/2,i/2); //i/2番目からi/2個分r取り出し
        if(s1==s2){
            cout << i << endl;
            break;
        }
    }
    return 0;
}
