class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int size=nums.size();
        int boundary=floor(size/3);
        unordered_map<int,int> gmap;
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            gmap[nums[i]]++;
        }
        for(auto it=gmap.begin();it!=gmap.end();it++){
            if(it->second>boundary){
                ans.push_back(it->first);
            }
        }
        return ans;
    }
};