//
//  main.cpp
//  akatsukivsleaf_he
//
//  Created by apple on 16/10/18.
//  Copyright © 2018 sahil. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <cstring>

#define ll long long

using namespace std;

ll n;

ll akat[20][2];
ll leaf[20][2];
ll dp[1048576][20];

ll solve(ll mask, ll curr)
{
    if (curr == n)
        return 0;
    if (dp[mask][curr] != -1)
        return dp[mask][curr];
    ll mini = 1000000007;
    for (ll i = 0; i < n; i++)
    {
        if ((mask & (1<<i)) == 0)
        {
            
            ll ans = abs(akat[i][0] - leaf[curr][0]) + abs(akat[i][1] - leaf[curr][1]) + solve(mask | (1 << i), curr+1);
        
            if (ans < mini)
                mini = ans;
        }
    }
    dp[mask][curr] = mini;
    return mini;
    
}

int main(int argc, const char * argv[])
{
    cin>>n;
    
    for (ll i = 0; i < n; i++)
        cin>>akat[i][0]>>akat[i][1];
    
    for (ll i = 0; i < n; i++)
        cin>>leaf[i][0]>>leaf[i][1];
    
    memset(dp, -1, sizeof(dp));
    cout<<solve(0, 0)<<endl;
    
    return 0;
}
