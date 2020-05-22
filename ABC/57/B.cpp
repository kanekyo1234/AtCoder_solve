#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,m;
    cin >> n >> m;
    vector<long> a(n);
    vector<long> b(n);
    vector<long> c(m);
    vector<long> d(m);
    
    for (int i=0;i<n;i++){
        cin >> a[i] >> b[i];
    }
    for (int i=0;i<m;i++){
        cin >> c[i] >> d[i];
    }

    for (int i=0;i<n;i++){
        long min=100000000000;
        int ans=0;
        for(int j=0;j<m;j++){
            long count=abs(a[i]-c[j])+abs(b[i]-d[j]);
            //cout << count<<" "<<min <<endl;
            if (min>count){
                min=count;
                ans=j+1;
            }
            //cout << count <<endl;
        }
        cout << ans << endl;
    }
    
    return 0;
}