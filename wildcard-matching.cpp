class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<int>> dp(p.size()+1, vector<int>(s.size()+1, 0));
        if( s.size()==0 && p.size()==0){
            return true;
        }
        if( p.size()==0){
            return false;
        }
        if( s.size()==0){
            int count=0;
            for(int i=0;i<p.size();i++){
                if( p[i]=='*'){
                    count++;
                }    
            }
            if(count==p.size()){
                return true;
            }
        }
        dp[p.size()][s.size()]=1;//setting the empty one as true.
        for(int i=p.size()-1;i>=0;i--){
            for(int j=s.size()-1;j>=0;j--){
                if(p[i]=='?'){
                    dp[i][j]=dp[i+1][j+1];
                }
                else if(p[i]=='*'){
                   
                        for(int k=j;k<=s.size();k++){
                        if( dp[i+1][k]==1){
                            dp[i][j]=1;
                            if(i==p.size()-1){
                                dp[i][s.size()]=1;
                            }
                            k=s.size()+1;
                        }
                    }
                    if( dp[i+1][s.size()]==1){
                                dp[i][s.size()]=1;
                            }
                }
                else if( p[i]==s[j]){
                    dp[i][j]=dp[i+1][j+1];
                } 
            }
        }
        return dp[0][0];
        
    }
};