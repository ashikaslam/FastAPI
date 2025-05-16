/*
*/
///PROBLEM LINK ->
#include <bits/stdc++.h>
using namespace std;
// this  5 lines   policy based data structures
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template <class T> using PBDS = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
//......... macros.........

#define Faster ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define yes cout<<"YES\n"
#define no cout<<"NO\n"
#define nl cout<<endl
#define sp <<" "
//
typedef long long ll;

// ........ constant.......
const long long  inf=1e18;
const long long mod = 1000000007;
const double Pi =  3.1415926535897932384626433832795;
int dx[] = {0, 0, -1, 1, -1, -1, 1, 1};  // Change in x for up, down, left, right, diagonal up-left, diagonal up-right, diagonal down-left, diagonal down-right
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};  // Change in y for up, down, left, right, diagonal up-left, diagonal up-right, diagonal down-left, diagonal down-right
//.......global.........
#ifdef LOKAL
#include "DEBUG_TEMPLATE.h"
#else
#define HERE
#define debug(args...)
#endif

double distance(double x1,double x2,double y1,double y2)  // distance of two coordination
{
    return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}
bool is_prime(ll n)// for prime
{
    if (n == 1)return false;
    if (n == 2)return true;
    if (n % 2 == 0)return false;
    for (ll i = 3; i * i <= n; i++)if (n % i == 0)return false;
    return true;
}

vector<long long> desi_to_bia(long long n)
{
    vector<long long> ans;
    while (n > 0)
    {
        ans.push_back(n & 1);
        n = n >> 1;
    }
    while(ans.size()<64)ans.push_back(0);
    reverse(ans.begin(), ans.end());
    return ans;
}

long long bia_to_desi(vector<long long> ar)
{
    long long sum = 0;
    reverse(ar.begin(), ar.end());
    for (long long i = 0; i < ar.size(); i++) if (ar[i]) sum += (1LL << i);
    return sum;
}


bool yes_good(vector<ll>ar)
{
    for(int i=1; i<ar.size()-1; i++)if(ar[i]==0 && ar[i+1]==1 && ar[i-1]==1)return false;
    return true;
}
ll sol(vector<ll>ar,int x,ll num)
{
    ll add = 1<<x;
    debug(num,add)
    num+=add;
    ar =  desi_to_bia(num);
    if(yes_good(ar))return add;

    ll flag = 0;
    ll ans = 1e18;
    for(ll i=0; i<5; i++)
    {
        ll now = sol(ar,i,num);
        if(now!=-1)
        {
            if(ans>now)ans= now;
            flag=1;
        }
    }
    if(flag)
    {
        return ans+add;
    }
    return -1;
}
void TEST_CASES()
{
    ll n;
    cin>>n;
    vector<ll>ar = desi_to_bia(n);
    if(yes_good(ar))
    {
        cout<<0<<endl;
        return ;
    }
    ll ans = 0;



    cout<<ans<<endl;
}


int t, n, x[100011], y[100011], xs, ys, xt, yt;
ll dis(int x1, int y1, int x2, int y2) {
    return 1ll * (x2 - x1) * (x2 - x1) + 1ll * (y2 - y1) * (y2 - y1);
}
int main() {
    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);

        for (int i = 1; i <= n; ++i)
            scanf("%d%d", x + i, y + i);

        scanf("%d%d%d%d", &xs, &ys, &xt, &yt);
        bool ok = 1;

        for (int i = 1; i <= n; ++i) {
            if (dis(xt, yt, x[i], y[i]) <= dis(xt, yt, xs, ys)) {
                ok = 0;
                break;
            }
        }

        printf(ok ? "YES\n" : "NO\n");
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
