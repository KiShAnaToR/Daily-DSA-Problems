#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<int> a;
vector<int> b;
vector<int> cnt;
vector<int> ops;

bool push_down(int idx) {
    if (b[idx] == k + 1) {
        return true;
    }

    int current_level = b[idx];
    int next_level = current_level + 1;

    // If the next level is already full, we must free up a spot first
    if (next_level <= k && cnt[next_level] >= a[next_level]) {
        int course_to_move = -1;
        for (int i = 0; i < n; i++) {
            if (b[i] == next_level) {
                course_to_move = i;
                break;
            }
        }
        
        // If we can't clear a spot below us, this path is blocked
        if (course_to_move == -1 || !push_down(course_to_move)) {
            return false;
        }
    }

    // Move our current course down
    cnt[current_level]--;
    b[idx]++;
    cnt[next_level]++;
    ops.push_back(idx + 1);
    return true;
}

void solve() {
    cin >> n >> k;
    
    a.assign(k + 2, 0);
    for (int i = 1; i <= k; i++) {
        cin >> a[i];
    }
    
    b.assign(n, 0);
    cnt.assign(k + 2, 0);
    for (int i = 0; i < n; i++) {
        cin >> b[i];
        cnt[b[i]]++;
    }

    ops.clear();

    // Keep pushing elements down until everything is at level k + 1
    bool progress = true;
    while (progress) {
        progress = false;
        for (int i = 0; i < n; i++) {
            if (b[i] < k + 1) {
                if (push_down(i)) {
                    progress = true;
                    break;
                }
            }
        }
    }

    // Check if everything successfully reached k + 1
    for (int i = 0; i < n; i++) {
        if (b[i] != k + 1) {
            cout << -1 << "\n";
            return;
        }
    }

    cout << ops.size() << "\n";
    for (int i = 0; i < ops.size(); i++) {
        cout << ops[i] << " ";
    }
    cout << "\n";
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