class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(),1);
        dp[0]=1;
        int i=1;
        while(i<nums.size()){
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j] && dp[i]<dp[j]+1){
                    dp[i]=dp[j]+1;
                }
            }
            i++;
        }
        sort(dp.begin(), dp.end());
        return dp[nums.size()-1];
    }
};