//Bottom-Up Solution

#include <iostream>
#include <string>

using namespace std;

int dp[6101][6101];

int main(int argc, const char * argv[])
{
    long t;
    cin>>t;
    
    while(t--)
    {
        string s;
        cin>>s;
        
        for(long i = s.length()-1; i >= 0; i--)
            for(long j = i+1; j < s.length(); j++)
                if(s[i]==s[j])
                    dp[i][j] = dp[i+1][j-1];
                else
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1]);
        
        cout<<dp[0][s.length()-1]<<endl;
    }
    return 0;
}
