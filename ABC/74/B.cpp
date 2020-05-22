#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,k;
    cin >> n >> k ;
    vector<int> x(n);
    for (int i=0;i<n;i++){
        cin >>x.at(i);
    }
    int ans = 0;
    for(int i=0;i<n;i++){
    int tmp = min(x[i],k-x[i]);
    ans += tmp;
    }
    cout <<ans*2<<endl;

    return 0;
}
