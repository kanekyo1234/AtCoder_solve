

#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    cin >> a;
    vector<int> b(a);
    int ans=0;
    for(int i=0;i<a;i++){
        cin >> b[i];
        ans+=b[i];
    }
    int b_count=count(b.begin(),b.end(),0);
    a-=b_count;
    if (ans%a==0){
        cout << ans/a << endl;
    }else{
        cout << ans/a +1<< endl;
    }
    return 0;
}