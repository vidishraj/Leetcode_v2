class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        vector<vector<int>> dp(matrix.size(),vector<int> (matrix[0].size()));
        int size=matrix[0].size();
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<size;j++){
                if( matrix[i][j]==1){
                    if(i-1>=0 && j-1>=0 && matrix[i-1][j-1]!=0 && matrix[i][j-1] !=0 &&matrix[i-1][j]!=0){
                        int x=min(dp[i-1][j-1],dp[i-1][j]);
                        int y=min(x,dp[i][j-1]);
                        dp[i][j]=y+1;
                    }
                    else{
                        dp[i][j]=1;
                    }
                }
            }
        }
        int count=0;
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
               count+=dp[i][j];
            }
        }
        return count;
    }
};