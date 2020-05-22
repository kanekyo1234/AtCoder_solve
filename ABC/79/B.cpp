#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >>n;
    vector<long long> rui={2,1};
    for(int i=0;i<n-1;i++){
        rui.push_back(rui[i]+rui[i+1]);
    }
    /*for(int i=0;i<n+1;i++){
        cout << rui[i] << " ";
    }*/
    cout <<rui[n] << endl;
    return 0;
}
