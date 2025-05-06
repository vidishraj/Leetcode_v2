class Solution {
public:
    //5 has 1, 10 has 2, 15 has 3, 20 has 4, 25 has 6 
    int trailingZeroes(int n) {
        if(n==0){
            return 0;
        }
        int ans=0;
        int check=5;
        while(n/check>0){
            ans+=n/check;
            check*=5;
        }
        return ans;
    }
};