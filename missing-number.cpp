class Solution {
public:
    int missingNumber(vector<int>& nums) {
        //remember the highest and lowest 
        //then iterate and check which one is missing
        sort(nums.begin(), nums.end());
        for(int i=0;i+1<nums.size();i++){
            if(nums[i]+1!=nums[i+1]){
                return nums[i]+1;
            }
        }
        if( nums[nums.size()-1]==nums.size()){
            return 0;
        }
        return nums.size();
    }
};