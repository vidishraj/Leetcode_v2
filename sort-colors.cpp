class Solution {
public:
    void sortColors(vector<int>& nums) {
        //without sort and in place, we can use bubble sort
        for(int i=0;i<nums.size();i++){
            for(int j=0;j+1<nums.size();j++){
                if( nums[j]>nums[j+1]){
                    swap(nums[j], nums[j+1]);
                }
            }
        }
        //sort(nums.begin(), nums.end());
    }
};