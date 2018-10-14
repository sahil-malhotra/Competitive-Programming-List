#include <iostream>
#define ll long long

using namespace std;

ll fac[200005];


ll power(ll x, ll y, ll p)
{
    ll res = 1;
    x = x % p;
    
    while (y > 0)
    {
        if (y % 2 == 1)
            res = (res*x) % p;
        
        y = y/2;
        x = (x*x) % p;
    }
    return res;
}

ll inverse(ll n, ll p)
{
    return power(n, p-2, p);
}

ll nCr(ll n, ll r, ll p)
{
    
    return (fac[n] * inverse(fac[r], p) % p * inverse(fac[n-r], p) % p) % p;
}

int main()
{
    ll p = 1000000007;
    
    fac[0] = 1;
    for (ll i=1 ; i<=200001; i++)
        fac[i] = (fac[i-1]*i)%p;
    
    ll t;
    cin>>t;
    ll x1,y1,x2,y2;
    for (ll i=0; i<t; i++)
    {
        cin>>x1>>y1>>x2>>y2;
        ll m=x2-x1;
        ll n=y2-y1;
        ll ans = 0;
        for (ll a = 0; a<= min(m,n); a++)
        {
            ll k = 1;
            k = (k*nCr(m+n-a, m, p))%p;
            k = (k*nCr(m, a, p))%p;
            ans = (ans+k)%p;
        }
        cout<<"Case "<<i+1<<": "<<ans<<endl;
    
    }
    return 0;
}
