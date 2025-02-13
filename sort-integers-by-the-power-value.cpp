class Solution {
public:
    //to decrease the computation we have to just remember the value 
    //if we have an even value, we just have to check if half its value is in the cache or not 
    //if its there , we just replace it 
    //for odd we do the same thing, ALWASYs the cache 
    int getKth(int lo, int hi, int k) {
        map<int, int> dp;
        map<int, vector<int>> dp1;
        //we have to sort in the end dont forget
        int i=lo;
        int j;
        while(i<=hi){
            j=i;
            if(j%2==0){ //even case
                if(j/2>0 && dp[j/2]!=0){
                    dp[j]=dp[j/2]+1;
                    dp1[dp[j/2]+1].push_back(i);
                }
                else{
                    int k=0;
                    while(j!=1){
                        if( j%2==0){
                            j=j/2;
                        }
                        else{
                            j=3*j+1;
                        }
                        k++;
                    }
                    dp[i]=k;
                    dp1[k].push_back(i);
                }
            }
            else{
                if(dp[j*3+1]!=0){  
                    dp[j]=dp[j*3+1]+1;
                    dp1[dp[j*3+1]+1].push_back(i);
                }
                else{
                    int k=0;
                    while(j!=1){
                        if( j%2==0){
                            j=j/2;
                        }
                        else{
                            j=3*j+1;
                        }
                        k++;
                    }
                    
                    dp[i]=k;
                    dp1[k].push_back(i);
                }
            }
            i++;
        }
        int count=0;
        //i need the k in order and if there is a collissions 
        vector<int>temp;
        for(auto it=dp1.begin();it!=dp1.end();it++){
            temp=it->second;
            if(temp.size()>1){
                sort(temp.begin(),temp.end());
                for(int i=0;i<temp.size();i++){
                    count++;
                    if( count==k){
                        return temp[i];
                    }
                }
            }
            else{
                count++;
                if( count==k){
                    return it->second[0];
                }
            }
        }
        
        return lo;
        
    }
};