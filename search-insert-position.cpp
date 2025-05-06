class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start=0;
        int end=nums.size()-1;
        int middle=(end+start)/2;
        while(start<=end){
            if(target<nums[middle]){
                end=middle-1;
            }
            if(target>nums[middle]){
                start=middle+1;
            }
            if(target==nums[middle]){
              return middle;  
            }
            middle=(end+start)/2;
        }
        return start;
    }
};