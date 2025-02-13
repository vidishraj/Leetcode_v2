class Solution {
public:
    int singleNumber(vector<int>& nums) {
       //sort(nums.begin(),nums.end());
        unordered_map<int,int> gmap;
        for(int i=0;i<nums.size();i++){
            gmap[nums[i]]++;  
        }
        for(auto it=gmap.begin();it!=gmap.end();it++){
            if(it->second==1){
                return it->first;
            }
        }
        return 0;
    }
};