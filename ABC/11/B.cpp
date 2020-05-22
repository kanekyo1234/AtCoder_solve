
#include <bits/stdc++.h>
using namespace std;

int main() {
    string n;
    cin >> n;
    n[0]=toupper(n[0]);
    for (int i=1;i<n.length();i++){
        n[i]=tolower(n[i]);
    }
    cout << n << endl;
    
    return 0;
}
