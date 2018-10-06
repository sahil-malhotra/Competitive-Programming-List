#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

#define ll long long

int main(int argc, const char * argv[])
{
    ll n, m;
    ll inp[1000005];
    ll q[1000005];
    cin>>n>>m;
    
    for (ll i = 0; i < n; i++)
        cin>>inp[i];
    sort(inp, inp+n, greater<ll>());
    
    for (ll i = 0; i < m; i++)
        cin>>q[i];
    
    queue<ll> q1, q2;
    
    for (ll i = 0; i < n; i++)
        q1.push(inp[i]);
    
    ll maximum = *max_element(q,q+m);
    ll move[maximum+1];
    memset(move, 0, sizeof(move));
    
    ll j = 1;
    
    while (j <= maximum)
    {
        ll ele;
        
        if (q2.empty())
        {
            move[j] = q1.front();
            q1.pop();
            ele = move[j] / 2;
        }
        else if (q1.empty())
        {
            move[j] = q2.front();
            q2.pop();
            ele = move[j] / 2;
        }
        else
        {
            
            if (q1.front() >= q2.front())
            {
                move[j] = q1.front();
                q1.pop();
                ele = move[j] / 2;
            }
            
            else
            {
                move[j] = q2.front();
                q2.pop();
                ele = move[j] / 2;
        }
        
        }
        q2.push(ele);

    j+=1;

}
    
    for (ll i = 0; i < m; i++)
        cout<<move[q[i]]<<endl;

return 0;
}
