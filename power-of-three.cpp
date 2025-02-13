class Solution {
public:
    bool isPowerOfThree(int n) {
        if( n==1 ||n==3){
            return true;
        }
        while(n>0){
            if( n%3!=0){
                return false;
            }
            if(n==3){
                return true;
            }
            n=n/3;
        }
        return false;
    }
};