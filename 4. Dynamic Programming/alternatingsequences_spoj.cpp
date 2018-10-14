#include <iostream>
#include <cstring>

using namespace std;

int dp[5001][5001];
int s[5001];
int n;

int f(int i, int last)
{
    if (i == n)
        return 0;
    
    else if(dp[i][last] != -1)
        return dp[i][last];
    
    else if(abs(s[i]) >= abs(s[last]))
        if ((s[last] >= 0 && s[i] <= 0) || (s[last] <= 0 && s[i] >= 0))
            dp[i][last] = max(1+f(i+1, i), f(i+1, last));
        else
            dp[i][last] = f(i + 1, last);
    
    else
        dp[i][last] = f(i+1, last);
    
    return dp[i][last];
}

int main()
{
    cin>>n;
    
    for(int i = 0; i < n; i++)
    {
        cin>>s[i];
    }
    s[n] = 0;
    
    memset(dp, -1, sizeof(dp));
    
    cout<<f(0,n)<<endl;
    
    return 0;
}

