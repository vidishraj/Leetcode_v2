class Solution {
public:
    int thirdMax(vector<int>& nums) {
      sort(nums.begin(), nums.end());
        reverse(nums.begin(),nums.end());
        auto it=unique(nums.begin(), nums.end());
        nums.resize(distance(nums.begin(),it));
        if(nums.size()>=3){
          return nums[2];  
        }
        return nums[0];
    }
};