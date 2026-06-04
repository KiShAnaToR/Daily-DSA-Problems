#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        long long x, y;
        cin >> x >> y;
        
        if (2 * x == y) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
        }
    }
    
    return 0;
}