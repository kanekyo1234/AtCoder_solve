#include <bits/stdc++.h>
using namespace std;

int main() {
    int n ,ma,mi;
    mi=10000;
    ma=0;
    cin >>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin >> a.at(i);
    }
    for(int i=0;i<n;i++){
        ma=max(ma,a[i]);
        mi=min(mi,a[i]);

    }
    cout << ma-mi << endl;
    return 0;
}