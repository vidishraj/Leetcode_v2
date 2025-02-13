class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>>res;
        vector<int> start={};
        res.push_back(start);
        vector<int> temp;
        int count=1;
        for(int i=0;i<nums.size();i++){
            int count1=0;
            for(int j=0;j<count;j++){
                temp=res[j];
                temp.push_back(nums[i]);
                res.push_back(temp);
                count1++;
                temp.clear();
            }
            count=count+count1;
        }
        vector<vector<int>> :: iterator it;
        int size=res.size();
        for(int i=0;i<res.size();i++){
            sort(res[i].begin(), res[i].end());
        }
        sort(res.begin(), res.end());
        it=unique(res.begin(), res.end());
        res.resize(distance(res.begin(), it));
        return res;
    }
};