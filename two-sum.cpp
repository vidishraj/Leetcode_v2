class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> gmap;
        gmap[nums[0]]=0;
        vector<int>result;
        for(int i=1;i<nums.size();i++){
            if(gmap.find(target-nums[i])!=gmap.end()){
                result.push_back(gmap[target-nums[i]]);
                result.push_back(i);
                return result;
            }
            gmap[nums[i]]=i;
        }
        return result;
    }
};
