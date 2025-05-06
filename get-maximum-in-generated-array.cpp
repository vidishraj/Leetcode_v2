class Solution {
public:
    int getMaximumGenerated(int n) {
        if( n==0){
            return 0;
        }
        vector<int>temp;
        temp.push_back(0);
        temp.push_back(1);
        int i=1;
        int j=2;
        int max=1;
        while(j<=n){
            temp.push_back(temp[i]);
            temp.push_back(temp[i]+temp[i+1]);
            j++;
            i++;
        }
        for(int i=0;i<=n;i++){
            if(max<temp[i]){
                max=temp[i];
            }
        }
        return max;
    }
};