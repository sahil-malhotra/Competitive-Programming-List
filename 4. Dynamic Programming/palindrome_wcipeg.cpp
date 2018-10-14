#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[])
{
    int length;
    cin>>length;
    string s;
    cin>>s;
    
    
    int dp[3][length];
    memset(dp, 0, sizeof(dp));
    
    
    for (int l = 2; l <= length; l++)
        for (int i = 0; i<=length-l; i++)
        {
            int j = i+l-1;
            if (s[i] == s[j])
                dp[l % 3][j] = dp[(l - 2) % 3][j - 1];
            else
                dp[l % 3][j] = 1 + min(dp[(l - 1) % 3][j], dp[(l - 1) % 3][j - 1]);
    }


cout<<dp[length % 3][length - 1]<<endl;

}
