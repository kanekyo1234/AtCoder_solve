#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n; 
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin >> a.at(i);
    }   
    int ans=-1;
    bool flag=true;
    while(flag){
        for (int i=0;i<n;i++){
            if (a[i]%2==1){
                flag=false;
            }else{
                a[i]/=2;
            }
        }
        ans+=1;
    }
    cout << ans << endl;
    return 0;
}
