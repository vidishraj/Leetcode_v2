class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        vector<int> temp;
        temp.push_back(1);
        res.push_back(temp);
        int i=1;
        vector<int> v;
        while(i<numRows){
            temp=res.back();
            int j=0;
            v.clear();
            v.push_back(1);
            while(j+1<temp.size()){
                int res=temp[j]+temp[j+1];
                v.push_back(res);
                j++;
            }
            v.push_back(1);
            res.push_back(v);
            i++;
        }
        return res;
    }
};