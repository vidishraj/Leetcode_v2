class Solution {
public:
    
    bool check(string &s, string &goal, int start){
        for(int i=0;i<s.size();i++){
            if(s[i]!=goal[start]){
                return false;
            }
            start++;
            if(start==goal.size()){
                start=0;
            }
        }
        return true;
    }
    
    bool rotateString(string s, string goal) {
        if(s==goal){
            return true;
        }
        if(s.size()!= goal.size()){
            return false;
        }
        unordered_map<char, int> gmap;
        for(int i=0;i<s.size();i++){
            gmap[s[i]]++;
        }
        char start=s[0];
        vector<int> indices;
        for(int i=0;i<goal.size();i++){
            if(gmap[goal[i]]==0){
                return false; 
            }
            if(goal[i]==start){
                indices.push_back(i);
            }
            gmap[goal[i]]--;
        }
        for(int i=0;i<indices.size();i++){
            if(check(s, goal, indices[i])){
                return true;
            }
        }
        return false;
    }
};