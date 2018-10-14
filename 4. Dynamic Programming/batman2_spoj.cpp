#include <iostream>
#include <climits>
#include <cstring>

using namespace std;
int room[102];
int n;
int mt[102][102][102];

int fun(int i, int last_inc, int last_dec)
{
    if (i == n)
        return 0;
    
    else if (mt[i][last_inc][last_dec] != -1)
        return mt[i][last_inc][last_dec];
    
    else if ((room[i] > room[last_inc]) && (room[i] < room[last_dec]))
        mt[i][last_inc][last_dec] = max(max(1 + fun(i+1, last_inc, i), 1 + fun(i+1, i, last_dec)), fun(i+1, last_inc, last_dec));
    
    else if (room[i] > room[last_inc])
        mt[i][last_inc][last_dec] = max(1 + fun(i+1, i, last_dec), fun(i+1, last_inc, last_dec));
    
    else if (room[i] < room[last_dec])
        mt[i][last_inc][last_dec] = max(1 + fun(i+1, last_inc, i), fun(i+1, last_inc, last_dec));
    
    else
        mt[i][last_inc][last_dec] = fun(i+1, last_inc, last_dec);
    return mt[i][last_inc][last_dec];
}


int main()
{
    
    int t;
    cin>>t;
    
    while (t--)
    {
        
        cin>>n;
        
        for (int i = 0; i < n; i++)
        {
            cin>>room[i];
        }
        
        room[n] = INT_MAX;
        room[n+1] = INT_MIN;
        
        memset(mt, -1, sizeof(mt));
        
        cout<<fun(0, n+1, n)<<endl;
    }
    
    return 0;
}
