class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        vector<int> temp;
        sort(intervals.begin(), intervals.end());
        for(int i=0;i<intervals.size();i++){
            int j=i+1;
            int start=intervals[i][0];
            int end=intervals[i][1];
            temp.push_back(start);
            while(j<intervals.size() && intervals[j][0]<=end){
                if(intervals[j][1]>end){
                    end=intervals[j][1];
                }
                j++;
            }
            temp.push_back(end);
            res.push_back(temp);
            i=j-1;
            temp.clear();
        }
        return res;
    }
};