#include <bits/stdc++.h>
using namespace std;
int main() {
    long long mod = 1000000000+7;
    long long a,b,c;
    cin >> a >> b >> c;
    cout << a*b%mod*c%mod;
    return 0;
}