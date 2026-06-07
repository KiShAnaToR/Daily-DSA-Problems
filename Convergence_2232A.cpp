#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    sort(a.begin(), a.end());
    
    long long median = a[n / 2];
    int L = lower_bound(a.begin(), a.end(), median) - a.begin();
    int R = a.end() - upper_bound(a.begin(), a.end(), median);
    
    cout << max(L, R) << "\n";
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