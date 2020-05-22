
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<set> a[n];
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    
    cout << (n+1)/2 << endl;
    
    return 0;
}
