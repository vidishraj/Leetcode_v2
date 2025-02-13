class Solution {
public:
    int fib(int n) {
        if( n==0){
            return 0;
        }
        vector<int> dp;
        dp.push_back(1);
        dp.push_back(1);
        for(int i=2;i<n;i++){
            dp.push_back(dp[i-1]+dp[i-2]);
        }
        return dp[n-1];
    }
};