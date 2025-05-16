#include <bits/stdc++.h>
using namespace std;

// ------------------------ Policy Based Data Structures ------------------------
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template<class T>
using PBDS = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

// ---------------------------- Macros & Typedefs ----------------------------
#define Faster ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define yes cout << "YES\n"
#define no cout << "NO\n"

typedef long long ll;

// ---------------------------- Constants ----------------------------
const ll INF = 1e18;
const ll MOD = 1e9 + 7;
const double Pi =  3.1415926535897932384626433832795;
int dx[] = {0, 0, -1, 1, -1, -1, 1, 1};  // Change in x for up, down, left, right, diagonal up-left, diagonal up-right, diagonal down-left, diagonal down-right
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};  // Change in y for up, down, left, right, diagonal up-left, diagonal up-right, diagonal down-left, diagonal down-right

// ---------------------------- Debug Tools ----------------------------
#ifdef LOKAL
#include "DEBUG_TEMPLATE.h"
#else
#define debug(args...)
#define HERE
#endif

// ---------------------------- Utility Functions ----------------------------
pair<ll,ll> inceg(ll l,ll h,pair<ll,ll>pr)
{
    ll l1 = pr.first;
    ll h1 = pr.second;
    if((l1<=l && h1>=h) || l1==l || l1==h || (l1>=l && l1<=h) || h1==l || h1==h || (h1>=l && h1<=h))
    {
        return {min(l,l1),max(h,h1)};
    }
    return {l,h};
}
ll lcm(ll a, ll b)
{
    return (a * b) / gcd(a, b);
}
bool isVowel(char ch)
{
    ch = tolower(ch); // Convert to lowercase for easy checking
    return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}

ll distanceOf2Point(int x1, int y1, int x2, int y2)
{
    return 1LL * (x2 - x1) * (x2 - x1) + 1LL * (y2 - y1) * (y2 - y1);
}

ll factorial_(ll n)
{
    if (n < 0) return -1;
    ll result = 1;
    for (ll i = 2; i <= n; ++i)
    {
        result *= i;
    }
    return result;
}
bool is_prime(ll n)
{
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (ll i = 3; i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

vector<bool> sieveOfEratosthenes(ll N)
{
    vector<bool> isPrime(N + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (ll i = 2; i * i <= N; i++)
    {
        if (isPrime[i])
        {
            for (ll j = i * i; j <= N; j += i)
                isPrime[j] = false;
        }
    }
    return isPrime;
}

vector<ll> getPrimeFactors(ll num)
{
    vector<ll> primeFactors;
    while (num % 2 == 0)
    {
        primeFactors.push_back(2);
        num /= 2;
    }
    for (ll i = 3; i * i <= num; i += 2)
    {
        while (num % i == 0)
        {
            primeFactors.push_back(i);
            num /= i;
        }
    }
    if (num > 1) primeFactors.push_back(num);
    return primeFactors;
}

vector<ll> desi_to_bia(ll n)
{
    vector<ll> ans;
    while (n > 0)
    {
        ans.push_back(n & 1);
        n >>= 1;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

ll bia_to_desi(vector<ll> ar)
{
    ll sum = 0;
    reverse(ar.begin(), ar.end());
    for (size_t i = 0; i < ar.size(); i++)
    {
        if (ar[i]) sum += (1LL << i);
    }
    return sum;
}

int clock_wise(int n, int len, int src)
{
    len %= n;
    if (src + len > n)
    {
        int now = 1;
        len -= (n - src);
        return len > 0 ? len + 1 : n;
    }
    return src + len;
}

int counter_clock_wise(int n, int len, int src)
{
    len %= n;
    if (src - len < 1)
    {
        int now = n;
        len -= (src - 1);
        return len > 0 ? n - len : now;
    }
    return src - len;
}

vector<ll> prifix_sum(vector<ll> ar)
{
    vector<ll> ans = ar;
    for (size_t i = 1; i < ar.size(); i++)
        ans[i] += ans[i - 1];
    return ans;
}

vector<ll> su_fix_sum(vector<ll> ar)
{
    vector<ll> ans = ar;
    for (int i = ar.size() - 2; i >= 0; i--)
        ans[i] += ans[i + 1];
    return ans;
}


bool customCompare(pair<ll, ll> a, pair<ll, ll> b)
{
    if (a.first < b.first) return true;
    if (a.first > b.first) return false;
    return a.second > b.second;
}

bool customComparest(string s, string s1)
{
    return s.size() < s1.size() || (s.size() == s1.size() && s < s1);
}

bool is_bloked(ll n, ll m, ll x, ll y)
{
    return (x < 0 || y < 0 || x >= n || y >= m);
}

vector<ll> getDivisors(ll n)
{
    vector<ll> divisors;
    for (ll i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            divisors.push_back(i);
            if (i != n / i) divisors.push_back(n / i);
        }
    }
    return divisors;
}

vector<ll> mergeAndRemoveDuplicatesUsingSet(const vector<ll>& vec1, const vector<ll>& vec2)
{
    unordered_set<ll> uniqueElements(vec1.begin(), vec1.end());
    uniqueElements.insert(vec2.begin(), vec2.end());
    return vector<ll>(uniqueElements.begin(), uniqueElements.end());
}

void removeDuplicatesWithSort(vector<ll> &vec)
{
    sort(vec.begin(), vec.end());
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
}

void removeDuplicatesPreserveOrder(vector<ll> &vec)
{
    unordered_set<ll> seen;
    vector<ll> uniqueVec;
    for (ll x : vec)
    {
        if (!seen.count(x))
        {
            uniqueVec.push_back(x);
            seen.insert(x);
        }
    }
    vec = uniqueVec;
}

ll base_return(ll n)
{
    return pow(10, to_string(n).size() - 1);
}

int mostSignificantBitPosition(int num)
{
    return num == 0 ? -1 : (int)log2(num);
}

ll sUm(vector<ll>&ar)
{
    ll sum = 0;
    for(ll i=0; i<ar.size(); i++)sum+=ar[i];
    return sum;
}

// ---------------------------- Solution Function ----------------------------




void TEST_CASES()
{


}



// ---------------------------- Main ----------------------------
int32_t main()
{
#ifndef LOKAL
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
#endif

    int t = 1;
    cin >> t;
    while (t--)
    {
        TEST_CASES();
    }
    return 0;
}



