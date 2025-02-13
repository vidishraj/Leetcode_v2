class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if( k==0){
            return 0;
        }
        int i =0;
        int j=0;
        int count=0;
        int product=1;
        
        while(j<nums.size()){
            product=product*nums[j];
            while(i<=j && product>=k){
                product=product/nums[i++];
            }   
            count+=j-i+ 1;
            j++;
        }/*
        for (int i = 0, j = 0; j < nums.size(); j++) {
            product *= nums[j];
            while (i <= j && product >= k) {
                product /= nums[i++];
            }
            count += j - i + 1;
        }*/
        return count;
        
    }
};