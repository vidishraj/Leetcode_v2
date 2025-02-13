class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        string temp;
        vector<string>ans;
        while(s.size()>k){
            temp.clear();
            temp=s.substr(0,k);
            s.erase(0,k);
            ans.push_back(temp);
        }
        if(s.size()==k){
            ans.push_back(s);
            return ans;
        }
        while(s.size()!=k){
            s.push_back(fill);
        }
        ans.push_back(s);
        return ans;
    }
};