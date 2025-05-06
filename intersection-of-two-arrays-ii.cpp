class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> c;
        unordered_map<int, int> gmap;
        unordered_map<int, int> gmap1;
        for(int i=0;i< nums1.size();i++){
            gmap[nums1[i]]++;
        }
        for(int i=0;i< nums2.size();i++){
            gmap1[nums2[i]]++;
        }
        for(auto it=gmap.begin();it!=gmap.end();it++){
            if(gmap1[it->first]>0){
                if( gmap1[it->first]<it->second){
                    it->second=gmap1[it->first];
                }
            }
        }
        gmap1.clear();
        for(int i=0;i< nums2.size();i++){
            if(gmap[nums2[i]]>0){
                for(int j=0;j<gmap[nums2[i]];j++){
                    c.push_back(nums2[i]);
                }
                gmap[nums2[i]]=0;
            }
        }
        return c;
    }
};