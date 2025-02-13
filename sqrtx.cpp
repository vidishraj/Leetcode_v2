class Solution {
public:
    int mySqrt(int x) {
     //can be done using bianry search 
        if(x==1){
            return 1;
        }
        long high=x;
        long low =0;
        long mid=(high+low)/2;
        long next;
        while(low<high){
            next=mid+1;
            if(mid*mid==x){//perfect square
                return mid;
            }
            if( mid-1*mid-1==x){
                return mid-1;
            }
           if(next*next==x){
                return next;
            }
            if((next*next)>x && (mid*mid)<x){//just behind
                return mid;
            }
            if( mid*mid>x && (mid-1)*(mid-1)<x){//just front 
                return mid-1;
            }
            if((mid*mid)>x){
                high=mid;
            }
            if((mid*mid)<x){
                low=mid;
            }
            mid=(high+low)/2;
        }
        return 0;
    }
};