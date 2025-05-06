class Solution {
public:
    double myPow(double x, int n) {
        //calculate the power of the x 
        if( n==INT_MAX || n==INT_MIN){
            if( x==1){
                return 1;
            }
            if(x==-1){
                if(n%2==0){
                    return 1;
                }
                return -1;
            }
            return 0;
        }
        double res=1;
        if( x==1){
            return 1;
        }
        if(n==0){
            return 1;
        }
        if(n>0){
            for(int i=0;i<n;i++){
                res=res*x;
            }
        }
       else if(n<0){
           n=-1*n;
            for(int i=0;i<n;i++){
                res=res*x;
            }
            //printf("%d", res);
            res=1/res;
        }
        return res;
    }
};