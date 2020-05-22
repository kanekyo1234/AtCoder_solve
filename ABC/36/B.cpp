#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n ;
    char s[n][n];
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cin >> s[i][j];
        }
    }
    for (int i=0;i<n;i++){
        for (int j=n-1;j>=0;j--){
            cout << s[j][i];
        }
        cout << endl;
    }

    return 0;
    
}