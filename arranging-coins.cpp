class Solution {
public:
    int arrangeCoins(int n) {
       //1,3,6, 10, 15, 21, 28, 36
        int rows=0;
        int i=1;
        while(n>=i){
            rows++;
            n-=i;
            i++;
        }
        return rows;
    }
};