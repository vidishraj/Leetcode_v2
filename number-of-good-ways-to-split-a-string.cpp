class Solution {
public:
    int numSplits(string s) {
        int count=0;//to count the total 
        unordered_map<int,int> dp(s.size());
        vector<int> dp1(s.size());
        vector<int> dp2(s.size());
        for(int i=0;i<s.size();i++){
            if(dp[s[i]]==0){
                dp[s[i]]=1;
                count++;
            }
            dp1[i]=count;
        }
        dp.clear();
        count=0;
        for(int i=s.size()-1;i>=0;i--){
            if(dp[s[i]]==0){
                dp[s[i]]=1;
                count++;
            }
            dp2[i]=count;
        }
        count=0;
        for(int i=0;i<s.size();i++){
            if( i+1<s.size()){
                if( dp1[i]==dp2[i+1]){
                    count++;
                }
            }
        }
        return count;
    }
};