
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

int main() {
    ///================ ARRAY ====================
    ll n = 10;
    ll ar1[n];
    sort(ar1, ar1 + n); // Sort array

    ///================ VECTOR ===================
    vector<ll> ar = {2, 4, 5, 4, 3, 2, 1, 5, 43, 3};
    sort(ar.begin(), ar.end()); // Ascending
    sort(ar.begin(), ar.end(), greater<ll>()); // Descending

    auto maxElement = max_element(ar.begin(), ar.end());
    auto minElement = min_element(ar.begin(), ar.end());
    ll mX = *maxElement, mN = *minElement;

    // 2D vector with 3 rows and 4 columns
    vector<vector<int>> twoDVector(3, vector<int>(4));

    // Remove duplicates from vector
    sort(ar.begin(), ar.end());
    ar.erase(unique(ar.begin(), ar.end()), ar.end());

    // lower_bound: first position >= value
    int lb = lower_bound(ar.begin(), ar.end(), 3) - ar.begin();
    cout << "Lower Bound of 3 at index: " << lb << endl;

    // upper_bound: first position > value
    int ub = upper_bound(ar.begin(), ar.end(), 3) - ar.begin();
    cout << "Upper Bound of 3 at index: " << ub << endl;

    ///================ SET ======================
    set<int> st = {1, 2, 3, 4, 5};
    int findElem = 6;
    if (st.find(findElem) == st.end())
        cout << findElem << " not found\n";
    else
        cout << findElem << " found\n";

    // Insert & erase
    st.insert(10);
    st.erase(2);

    ///============== UNORDERED SET ==============
    unordered_set<int> uset;
    uset.insert(5);

    ///============== MAP ========================
    map<int, int> mp;
    mp[1] = 10;
    if (mp.find(2) != mp.end()) cout << "Found\n";

    ///============== UNORDERED MAP ==============
    unordered_map<string, int> ump;
    ump["apple"] = 3;

    ///=========== PRIORITY QUEUE ================
    // Max heap
    priority_queue<int> maxPQ;
    maxPQ.push(10);

    // Min heap
    priority_queue<int, vector<int>, greater<int>> minPQ;
    minPQ.push(5);

    ///============== STRING =====================
    string s = "hello";
    string sub = s.substr(1, 3); // "ell"

    // Next permutation
    vector<string> perms;
    sort(s.begin(), s.end());
    do perms.push_back(s); while (next_permutation(s.begin(), s.end()));
    for (auto i : perms) cout << i << "\n";

    // Substring search
    string s2 = "world";
    if (s2.find("or") != string::npos)
        cout << "Substring found\n";

    ///============= STL ALGORITHMS ==============
    vector<int>::iterator it;
    sort(ar.begin(), ar.end()); // Must be sorted

    // Lower bound: first element >= x
    it = lower_bound(ar.begin(), ar.end(), 3);
    cout << "Lower bound index of 3: " << it - ar.begin() << "\n";

    // Upper bound: first element > x
    it = upper_bound(ar.begin(), ar.end(), 3);
    cout << "Upper bound index of 3: " << it - ar.begin() << "\n";

    ///============ BITWISE BUILT-INS =============
    ll sen = 8;

    // Count set bits (1s)
    cout << __builtin_popcountll(sen) << "\n"; // For long long
    cout << __builtin_popcount((int)sen) << "\n"; // For int

    // Count trailing zeroes
    cout << __builtin_ctzll(sen) << "\n";

    // Count leading zeroes
    cout << __builtin_clzll(sen) << "\n";

    ///============ MATH UTILITIES ================
    // GCD and LCM
    int a = 12, b = 18;
    int g = __gcd(a, b);
    int l = a * b / g;
    cout << "GCD: " << g << " LCM: " << l << "\n";

    ///============ RANDOM NUMBER ================
    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    int r = rng() % 100; // Random number between 0 and 99

    return 0;



}
