#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    
    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        weights[i] = 100 / a; 
    }

    sort(weights.begin(), weights.end());

    if (weights[0] != 1) {
        cout << "No\n";
        return;
    }

    int current_max_score = 0;
    for (int i = 0; i < n; i++) {
        if (weights[i] > current_max_score + 1) {
            cout << "No\n";
            return;
        }
        current_max_score += 100; 
    }

    cout << "Yes\n";
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