class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        auto it=unique(nums1.begin(),nums1.end());
        nums1.resize(distance(nums1.begin(), it));
        unordered_map<int,int> gmap(nums1.size());
        vector<int>res;
        for(int i=0;i< nums1.size();i++){
            gmap[nums1[i]]=1;
        }
        for(int i=0;i<nums2.size();i++){
            if(gmap[nums2[i]]==1){
                res.push_back(nums2[i]);
                gmap[nums2[i]]=0;
            }
        }
        return res;
    }
};