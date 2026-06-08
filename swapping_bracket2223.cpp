#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    string a, b;
    cin >> a >> b;

    int total_open = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == '(') total_open++;
        if (b[i] == '(') total_open++;
    }

    if (total_open != n) {
        cout << "NO\n";
        return;
    }

    int bal_a = 0, bal_b = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] == '(' && b[i] == '(') {
            bal_a++;
            bal_b++;
        } else if (a[i] == ')' && b[i] == ')') {
            bal_a--;
            bal_b--;
        } else {
            if (bal_a < bal_b) {
                bal_a++; 
                bal_b--; 
            } else {
                bal_b++; 
                bal_a--; 
            }
        }

        if (bal_a < 0 || bal_b < 0) {
            cout << "NO\n";
            return;
        }
    }

    cout << "YES\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}